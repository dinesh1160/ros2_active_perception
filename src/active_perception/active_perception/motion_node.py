"""Moves the BeetleBot (Lyra) to the next viewpoint on an orbit around the target.

One call to /move_to_next_view performs one orbit step of `orbit_step_deg` around a
target `orbit_radius` metres in front of the robot, ending facing the target again:

    turn (90 - step/2)  ->  drive chord 2*R*sin(step/2)  ->  turn back (90 + step/2)

The first turn deliberately points away from the target (along the chord to the next
viewpoint); the last turn brings the camera back onto it.

Turns are measured with the IMU gyro by default, because skid-steer wheel odometry
over-reports in-place rotation (the wheels slip sideways). Straight-line distance comes
from odometry. The robot is armed via /lyra/arm for the move and disarmed afterwards;
every failure path publishes zero velocity first.
"""

import math
import signal
import threading
import time

import rclpy
import rclpy.signals
from rclpy.executors import ExternalShutdownException, SingleThreadedExecutor
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from rcl_interfaces.msg import ParameterDescriptor
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu, LaserScan
from std_srvs.srv import Trigger


def wrap_angle(a):
    return math.atan2(math.sin(a), math.cos(a))


def yaw_from_quaternion(q):
    return math.atan2(2.0 * (q.w * q.z + q.x * q.y), 1.0 - 2.0 * (q.y * q.y + q.z * q.z))


class MotionError(Exception):
    pass


class MotionNode(Node):
    def __init__(self):
        super().__init__('motion_node')

        defaults = {}

        def p(name, default):
            # Dynamic typing so whole-number launch values (e.g. ':=0') work for float parameters
            defaults[name] = default
            self.declare_parameter(name, default, ParameterDescriptor(dynamic_typing=True))

        def g(name):
            value = self.get_parameter(name).value
            return float(value) if isinstance(defaults[name], float) else value
        p('cmd_vel_topic', '/cmd_vel_nav')
        p('odom_topic', '/odometry/filtered')
        p('imu_topic', '/imu/data')
        p('scan_topic', '/scan')
        p('arm_service', '/lyra/arm')
        p('disarm_service', '/lyra/disarm')
        p('use_arming', True)
        p('orbit_radius', 0.8)          # m, robot centre to target at the start
        p('orbit_step_deg', 30.0)       # how far around the target each step moves
        p('orbit_direction', 'ccw')     # 'ccw' or 'cw' around the target, seen from above
        p('linear_speed', 0.15)         # m/s
        p('angular_speed', 0.5)         # rad/s (max while turning)
        p('min_angular_speed', 0.25)    # rad/s, enough to overcome skid-steer friction
        p('yaw_tolerance_deg', 2.0)
        p('stop_hold_sec', 1.5)         # zero-velocity hold after each segment
        p('control_rate_hz', 20.0)
        p('sensor_max_age_sec', 1.0)
        # Turn measurement: 'imu' (gyro z, bias removed before each move) or 'odom'
        p('turn_source', 'imu')
        p('imu_yaw_sign', 1.0)          # -1.0 if the gyro reads negative for a LEFT turn
        p('imu_gyro_scale', 1.0)        # multiplier to rad/s (0.0174533 if the IMU publishes deg/s)
        p('odom_distance_scale', 1.0)   # odom-reported / real straight-line distance
        p('turn_timeout_sec', 30.0)     # per turn; skid-steer turns slowly in place
        p('odom_turn_scale', 1.0)       # odom-reported / real rotation (e.g. 1.6), 'odom' source only
        # Obstacle stop (distances from the lidar centre)
        p('obstacle_stop_enabled', True)
        p('scan_ignore_below', 0.23)    # m, closer readings are the robot's own body
        p('robot_front_offset', 0.19)   # m, lidar centre to front bumper (robot is 375 mm long)
        p('obstacle_clearance', 0.15)   # m, stop when something is this close to the bumper
        p('scan_front_angle_deg', 0.0)  # lidar angle that points to the robot's front
        p('scan_front_half_width_deg', 20.0)

        self.use_arming = g('use_arming')
        self.radius = g('orbit_radius')
        self.step = math.radians(g('orbit_step_deg'))
        direction = g('orbit_direction').lower()
        if direction not in ('ccw', 'cw'):
            raise ValueError("orbit_direction must be 'ccw' or 'cw'")
        # Orbiting CCW around the target moves the robot to its right, so turn right first
        self.sign = 1.0 if direction == 'ccw' else -1.0
        self.v = g('linear_speed')
        self.w_max = g('angular_speed')
        self.w_min = g('min_angular_speed')
        self.yaw_tol = math.radians(g('yaw_tolerance_deg'))
        self.stop_hold = g('stop_hold_sec')
        self.dt = 1.0 / g('control_rate_hz')
        self.max_age = g('sensor_max_age_sec')
        self.turn_source = g('turn_source').lower()
        if self.turn_source not in ('imu', 'odom'):
            raise ValueError("turn_source must be 'imu' or 'odom'")
        self.imu_sign = g('imu_yaw_sign') * g('imu_gyro_scale')
        self.distance_scale = g('odom_distance_scale')
        self.turn_timeout = g('turn_timeout_sec')
        self.odom_turn_scale = g('odom_turn_scale')
        self.obstacle_enabled = g('obstacle_stop_enabled')
        self.scan_ignore = g('scan_ignore_below')
        self.obstacle_dist = g('robot_front_offset') + g('obstacle_clearance')
        self.scan_front = math.radians(g('scan_front_angle_deg'))
        self.scan_half = math.radians(g('scan_front_half_width_deg'))

        self.lock = threading.Lock()
        self.pos = None             # (x, y) from odometry
        self.odom_yaw = None
        self.odom_time = None
        # Heading for the current move (rad, CCW positive, 0 at the start of the move)
        self.heading = 0.0
        self.gyro_bias = 0.0
        self.gyro_samples = None    # list while measuring the bias
        self.last_imu = None        # (stamp_sec, corrected gyro z)
        self.imu_time = None
        self.front_min = None       # nearest range in the front sector
        self.scan_time = None
        self.busy = False
        self.stopping = False
        self.logged_front = False

        self.cmd_pub = self.create_publisher(Twist, g('cmd_vel_topic'), 10)
        self.create_subscription(Odometry, g('odom_topic'), self.odom_callback, qos_profile_sensor_data)
        self.create_subscription(Imu, g('imu_topic'), self.imu_callback, qos_profile_sensor_data)
        self.create_subscription(LaserScan, g('scan_topic'), self.scan_callback, qos_profile_sensor_data)
        self.arm_client = self.create_client(Trigger, g('arm_service'))
        self.disarm_client = self.create_client(Trigger, g('disarm_service'))
        # The move blocks inside this service callback, so the service lives on its own node and
        # executor; this node's sensors and arm/disarm replies keep flowing on a background thread.
        # (Two single-threaded executors: rclpy's MultiThreadedExecutor burns enough CPU to
        # stall the 20 Hz command stream and trip the robot's 500 ms watchdog.)
        self.service_node = rclpy.create_node('motion_node_service')
        self.service_node.create_service(Trigger, '/move_to_next_view', self.handle_move)

        chord = 2.0 * self.radius * math.sin(self.step / 2.0)
        turn_desc = (f"IMU '{g('imu_topic')}' (x{self.imu_sign:+.4g})" if self.turn_source == 'imu'
                     else f"odometry (scale {self.odom_turn_scale})")
        self.get_logger().info(
            f"Motion node ready. Orbit {direction.upper()} {math.degrees(self.step):.0f} deg/step "
            f"around R={self.radius:.2f} m (drive {chord:.2f} m per step) on '{g('cmd_vel_topic')}'. "
            f"Turns measured with {turn_desc}; obstacle stop at {self.obstacle_dist:.2f} m from lidar.")

    # ---------------- sensors ----------------
    def odom_callback(self, msg: Odometry):
        p = msg.pose.pose
        yaw = yaw_from_quaternion(p.orientation)
        with self.lock:
            if self.turn_source == 'odom' and self.odom_yaw is not None:
                # Accumulate unwrapped yaw change, corrected for skid-steer over-reporting
                self.heading += wrap_angle(yaw - self.odom_yaw) / self.odom_turn_scale
            self.pos = (p.position.x, p.position.y)
            self.odom_yaw = yaw
            self.odom_time = time.monotonic()

    def imu_callback(self, msg: Imu):
        wz = self.imu_sign * msg.angular_velocity.z
        t = msg.header.stamp.sec + msg.header.stamp.nanosec * 1e-9
        if t == 0.0:
            t = time.monotonic()  # unstamped IMU: fall back to receive time
        with self.lock:
            if self.gyro_samples is not None:
                self.gyro_samples.append(wz)
            corrected = wz - self.gyro_bias
            if self.turn_source == 'imu' and self.last_imu is not None:
                dt = t - self.last_imu[0]
                if 0.0 < dt < 0.5:
                    # Trapezoidal integration of the bias-corrected gyro rate
                    self.heading += 0.5 * (corrected + self.last_imu[1]) * dt
            self.last_imu = (t, corrected)
            self.imu_time = time.monotonic()

    def scan_callback(self, msg: LaserScan):
        nearest = math.inf
        for i, r in enumerate(msg.ranges):
            if not (msg.range_min <= r <= msg.range_max) or r < self.scan_ignore:
                continue  # inf / nan / out of range / the robot's own body
            angle = msg.angle_min + i * msg.angle_increment
            if abs(wrap_angle(angle - self.scan_front)) <= self.scan_half:
                nearest = min(nearest, r)
        with self.lock:
            self.front_min = nearest
            self.scan_time = time.monotonic()
        if not self.logged_front:
            self.logged_front = True
            self.get_logger().info(
                f"Lidar OK. Nearest obstacle in front sector: {nearest:.2f} m "
                "(check this matches reality; if not, adjust scan_front_angle_deg).")

    def check_sensors(self):
        now = time.monotonic()
        with self.lock:
            if self.odom_time is None or now - self.odom_time > self.max_age:
                raise MotionError("No fresh odometry; refusing to move")
            if self.turn_source == 'imu' and (self.imu_time is None or now - self.imu_time > self.max_age):
                raise MotionError("No fresh IMU data; refusing to move (or set turn_source:=odom)")

    def state(self):
        """Current (x, y, heading) with fresh-data checks."""
        self.check_sensors()
        with self.lock:
            return self.pos[0], self.pos[1], self.heading

    def reset_heading(self):
        """Zero the move heading; for the IMU also re-measure the gyro bias while standing still."""
        if self.turn_source == 'imu':
            with self.lock:
                self.gyro_samples = []
            time.sleep(0.5)
            with self.lock:
                samples, self.gyro_samples = self.gyro_samples, None
                if samples:
                    self.gyro_bias = sum(samples) / len(samples)
            self.get_logger().info(f"Gyro bias {math.degrees(self.gyro_bias):+.2f} deg/s")
        with self.lock:
            self.heading = 0.0

    # ---------------- low-level helpers ----------------
    def publish(self, v=0.0, w=0.0):
        cmd = Twist()
        cmd.linear.x = float(v)
        cmd.angular.z = float(w)
        self.cmd_pub.publish(cmd)

    def hold_stop(self, duration):
        """Publish zero velocity for `duration` seconds (like the manual's forced stop)."""
        end = time.monotonic() + duration
        while time.monotonic() < end:
            self.publish()
            time.sleep(self.dt)

    def call_trigger(self, client, name, timeout=3.0):
        if not client.wait_for_service(timeout_sec=timeout):
            raise MotionError(f"Service {name} not available")
        future = client.call_async(Trigger.Request())
        end = time.monotonic() + timeout
        while not future.done():
            if time.monotonic() > end:
                raise MotionError(f"Service {name} timed out")
            time.sleep(0.01)
        result = future.result()
        if not result.success:
            raise MotionError(f"{name} refused: {result.message}")
        return result

    def check_abort(self):
        if self.stopping or not rclpy.ok():
            raise MotionError("Shutting down")

    # ---------------- motion primitives ----------------
    def rotate_to(self, target):
        """Rotate in place to a move-relative heading (rad, CCW positive)."""
        timeout = time.monotonic() + self.turn_timeout
        while True:
            self.check_abort()
            err = target - self.state()[2]
            if abs(err) <= self.yaw_tol:
                break
            if time.monotonic() > timeout:
                raise MotionError(f"Rotation timed out ({math.degrees(err):.1f} deg left)")
            # Proportional, slowing down near the target to limit overshoot
            w = max(self.w_min, min(self.w_max, 1.5 * abs(err)))
            self.publish(0.0, math.copysign(w, err))
            time.sleep(self.dt)
        self.hold_stop(self.stop_hold)
        self.get_logger().info(f"  heading now {math.degrees(self.state()[2]):+.1f} deg "
                               f"(target {math.degrees(target):+.1f})")

    def drive(self, distance, heading):
        """Drive straight `distance` metres, holding `heading` with a small yaw correction."""
        x0, y0, _ = self.state()
        timeout = time.monotonic() + distance / self.v * 2.0 + 5.0
        while True:
            self.check_abort()
            x, y, h = self.state()
            travelled = math.hypot(x - x0, y - y0) / self.distance_scale
            if travelled >= distance - 0.01:
                break
            if time.monotonic() > timeout:
                raise MotionError(f"Drive timed out ({travelled:.2f}/{distance:.2f} m)")
            if self.obstacle_enabled:
                with self.lock:
                    front, scan_time = self.front_min, self.scan_time
                if scan_time is None or time.monotonic() - scan_time > 1.0:
                    raise MotionError("No fresh lidar scan; refusing to drive "
                                      "(set obstacle_stop_enabled:=false to bypass)")
                if front < self.obstacle_dist:
                    raise MotionError(f"Obstacle {front:.2f} m ahead of the lidar; "
                                      f"stopped after {travelled:.2f} m")
            # Slow down for the last 10 cm
            v = self.v if distance - travelled > 0.10 else max(0.08, self.v * 0.5)
            w = max(-0.3, min(0.3, 1.5 * (heading - h)))
            self.publish(v, w)
            time.sleep(self.dt)
        self.hold_stop(self.stop_hold)

    # ---------------- service ----------------
    def handle_move(self, request, response):
        if self.busy:
            response.success = False
            response.message = "Already moving"
            return response
        self.busy = True
        armed = False
        try:
            self.check_sensors()
            self.reset_heading()  # robot is still: heading 0 = facing the target
            half = self.step / 2.0
            chord = 2.0 * self.radius * math.sin(half)
            heading_chord = -self.sign * (math.pi / 2.0 - half)
            heading_final = self.sign * self.step

            if self.use_arming:
                self.call_trigger(self.arm_client, '/lyra/arm')
                armed = True
                self.hold_stop(0.3)  # keep the cmd watchdog fed while the gate opens

            self.get_logger().info(
                f"Turning {math.degrees(heading_chord):+.0f} deg (away from the target, along the path)")
            self.rotate_to(heading_chord)
            self.get_logger().info(f"Driving {chord:.2f} m")
            self.drive(chord, heading_chord)
            self.get_logger().info(
                f"Turning {math.degrees(heading_final - heading_chord):+.0f} deg back to face the target")
            self.rotate_to(heading_final)

            x, y, h = self.state()
            response.success = True
            response.message = (f"Arrived at x={x:.2f} y={y:.2f}, turned {math.degrees(h):+.0f} deg "
                                "in total (net orbit step)")
            self.get_logger().info(response.message)
        except MotionError as e:
            response.success = False
            response.message = str(e)
            self.get_logger().error(f"Move aborted: {e}")
            self.hold_stop(0.5)
        except Exception as e:  # never leave the robot driving on an unexpected error
            response.success = False
            response.message = f"Unexpected error: {e}"
            self.get_logger().error(response.message)
            self.hold_stop(0.5)
        finally:
            if armed and not self.stopping:  # on shutdown emergency_stop() disarms
                try:
                    self.call_trigger(self.disarm_client, '/lyra/disarm')
                except MotionError as e:
                    self.get_logger().warn(f"Disarm failed ({e}); robot auto-disarms after 500 ms")
            self.busy = False
        return response

    def emergency_stop(self):
        """On shutdown: abort any move, send zeros and disarm (best effort)."""
        self.stopping = True
        for _ in range(10):
            self.publish()
            time.sleep(0.02)
        if self.use_arming and self.disarm_client.service_is_ready():
            future = self.disarm_client.call_async(Trigger.Request())
            end = time.monotonic() + 1.0  # the sensor executor thread completes the future
            while not future.done() and time.monotonic() < end:
                time.sleep(0.01)


def main(args=None):
    # Handle Ctrl+C / kill ourselves so the ROS context is still alive to stop the robot
    rclpy.init(args=args, signal_handler_options=rclpy.signals.SignalHandlerOptions.NO)
    signal.signal(signal.SIGINT, signal.default_int_handler)
    signal.signal(signal.SIGTERM, signal.default_int_handler)
    node = MotionNode()
    sensor_executor = SingleThreadedExecutor()
    sensor_executor.add_node(node)
    threading.Thread(target=sensor_executor.spin, daemon=True).start()
    service_executor = SingleThreadedExecutor()
    service_executor.add_node(node.service_node)
    try:
        # Short slices so Ctrl+C is noticed even when nothing is calling the service
        while rclpy.ok():
            service_executor.spin_once(timeout_sec=0.2)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.emergency_stop()
        service_executor.shutdown()
        sensor_executor.shutdown()
        node.service_node.destroy_node()
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
