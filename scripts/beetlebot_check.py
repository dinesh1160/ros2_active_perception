"""BeetleBot (Lyra) sensor check for the motion node. Prints the launch settings to use.

    python3 scripts/beetlebot_check.py          # read-only: topics + lidar
    python3 scripts/beetlebot_check.py --turn   # also arms and turns LEFT for 3 s at 0.5 rad/s
    python3 scripts/beetlebot_check.py --hand   # motors OFF: you rotate the robot exactly 90 deg LEFT by hand
    python3 scripts/beetlebot_check.py --drive  # arms and drives FORWARD 3 s at 0.15 m/s (~0.45 m)

Read-only run: clear ~1 m around the robot and put a box ~0.5 m straight in front of it.
--turn run: put a tape mark on the floor along the robot's heading first, so you can
estimate the real angle turned (commanded is ~86 deg).
"""

import math
import sys
import time

import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu, LaserScan
from std_srvs.srv import Trigger

ODOMS = ('/odometry/filtered', '/wheel/odom')
IMUS = ('/imu/data', '/imu/data_raw')


def yaw_of(q):
    return math.atan2(2.0 * (q.w * q.z + q.x * q.y), 1.0 - 2.0 * (q.y * q.y + q.z * q.z))


def wrap(a):
    return math.atan2(math.sin(a), math.cos(a))


class Check(Node):
    def __init__(self):
        super().__init__('beetlebot_check')
        self.count = {}
        self.odom_turn = {}     # accumulated odom yaw change per topic
        self.last_yaw = {}
        self.gyro = {}          # per IMU: list of z samples (for bias)
        self.gyro_turn = {}     # per IMU: integrated (z - bias)
        self.gyro_t = {}
        self.bias = {}
        self.scan = None
        self.pos = {}
        for t in ODOMS:
            self.create_subscription(Odometry, t, lambda m, t=t: self.on_odom(t, m), qos_profile_sensor_data)
        for t in IMUS:
            self.create_subscription(Imu, t, lambda m, t=t: self.on_imu(t, m), qos_profile_sensor_data)
        self.create_subscription(LaserScan, '/scan', self.on_scan, qos_profile_sensor_data)
        self.cmd = self.create_publisher(Twist, '/cmd_vel_nav', 10)
        self.arm = self.create_client(Trigger, '/lyra/arm')
        self.disarm = self.create_client(Trigger, '/lyra/disarm')

    def on_odom(self, t, m):
        self.count[t] = self.count.get(t, 0) + 1
        yaw = yaw_of(m.pose.pose.orientation)
        self.pos[t] = (m.pose.pose.position.x, m.pose.pose.position.y)
        if t in self.last_yaw:
            self.odom_turn[t] = self.odom_turn.get(t, 0.0) + wrap(yaw - self.last_yaw[t])
        self.last_yaw[t] = yaw

    def on_imu(self, t, m):
        self.count[t] = self.count.get(t, 0) + 1
        z = m.angular_velocity.z
        now = m.header.stamp.sec + m.header.stamp.nanosec * 1e-9 or time.monotonic()
        self.gyro.setdefault(t, []).append(z)
        if t in self.gyro_t and t in self.bias:
            self.gyro_turn[t] = self.gyro_turn.get(t, 0.0) + (z - self.bias[t]) * (now - self.gyro_t[t])
        self.gyro_t[t] = now

    def on_scan(self, m):
        self.count['/scan'] = self.count.get('/scan', 0) + 1
        self.scan = m

    def spin_for(self, seconds, cmd=None):
        end = time.monotonic() + seconds
        while time.monotonic() < end:
            if cmd is not None:
                self.cmd.publish(cmd)
            rclpy.spin_once(self, timeout_sec=0.05)

    def call(self, client, name):
        if not client.wait_for_service(timeout_sec=3.0):
            sys.exit(f"{name} not available - is the robot bringup running?")
        fut = client.call_async(Trigger.Request())
        rclpy.spin_until_future_complete(self, fut, timeout_sec=3.0)
        print(f"{name}: {fut.result().message if fut.result() else 'no reply'}")


def report_scan(s):
    print("\nLIDAR: nearest range per 45-deg sector (lidar's own angles)")
    sectors, close, valid = {}, [], []
    for i, r in enumerate(s.ranges):
        if not (s.range_min <= r <= s.range_max):
            continue
        a = math.degrees(wrap(s.angle_min + i * s.angle_increment))
        valid.append((r, a))
        key = int(((a + 22.5) % 360) // 45) * 45
        key = key if key <= 180 else key - 360
        sectors[key] = min(sectors.get(key, math.inf), r)
        if r < 0.30:
            close.append((round(a), round(r, 3)))
    for key in sorted(sectors):
        print(f"  {key:+5d} deg : {sectors[key]:.2f} m")
    if close:
        print(f"  Readings closer than 0.30 m (= the robot's own body if nothing is that close): "
              f"{len(close)}, angles {min(a for a, _ in close)}..{max(a for a, _ in close)} deg, "
              f"farthest {max(r for _, r in close):.3f} m")
        ignore = max(r for _, r in close) + 0.02
    else:
        print("  No readings closer than 0.30 m (no self-hits).")
        ignore = 0.22
    beyond = [(r, a) for r, a in valid if r >= max(ignore, 0.30)]
    front = min(beyond)[1] if beyond else 0.0
    print(f"  Nearest object beyond the body: {min(beyond)[0]:.2f} m at {front:+.0f} deg "
          "(should be your box in front)" if beyond else
          "  No object found beyond the body - is the box in front of the robot?")
    return ignore, front


def main():
    rclpy.init()
    n = Check()
    print("Listening 3 s (keep the robot still)...")
    n.spin_for(3.0)
    print("\nTOPIC RATES (Hz):")
    for t in ODOMS + IMUS + ('/scan',):
        print(f"  {t:22s} {n.count.get(t, 0) / 3.0:6.1f}")
    for t, samples in n.gyro.items():
        n.bias[t] = sum(samples) / len(samples)
        print(f"  {t} gyro bias: {math.degrees(n.bias[t]):+.2f} deg/s")
    settings = {}
    if n.scan:
        ignore, front = report_scan(n.scan)
        settings['scan_ignore_below'] = f"{ignore:.2f}"
        settings['scan_front_angle_deg'] = f"{round(front / 5) * 5:.0f}  (only if that was your box)"

    if '--turn' in sys.argv:
        n.odom_turn, n.gyro_turn = {}, {}
        n.call(n.arm, '/lyra/arm')
        turn = Twist()
        turn.angular.z = 0.5
        try:
            print("Turning LEFT 0.5 rad/s for 3 s (commanded ~86 deg)...")
            n.spin_for(3.0, turn)
            n.spin_for(1.5, Twist())  # forced stop, keep measuring while it settles
        finally:
            for _ in range(10):
                n.cmd.publish(Twist())
            n.call(n.disarm, '/lyra/disarm')
        print("\nMEASURED TURN (positive = left/CCW):")
        for t, v in n.odom_turn.items():
            print(f"  {t + ' (odometry)':32s} {math.degrees(v):+7.1f} deg")
        for t, v in n.gyro_turn.items():
            print(f"  {t + ' (gyro)':32s} {math.degrees(v):+7.1f} deg")
        try:
            real = float(input("\nReal angle turned, from the tape mark, in degrees (e.g. 60): "))
        except (ValueError, EOFError):
            real = None
        if real:
            gyro = n.gyro_turn.get('/imu/data')
            if gyro is not None:
                g = math.degrees(gyro)
                settings['imu_yaw_sign'] = '-1.0' if g < 0 else '1.0'
                ok = abs(abs(g) - real) <= 0.1 * real
                print(f"  Gyro: {abs(g):.0f} deg vs real {real:.0f} deg -> "
                      f"{'GOOD, use turn_source:=imu' if ok else 'OFF by >10%, tell me the numbers'}")
            odom = n.odom_turn.get('/odometry/filtered')
            if odom:
                scale = math.degrees(odom) / real
                print(f"  /odometry/filtered over-reports turns by x{scale:.2f}")
                settings['odom_turn_scale'] = f"{scale:.2f}  (only needed with turn_source:=odom)"

    if '--hand' in sys.argv:
        n.gyro_turn = {}
        input("\nMotors stay OFF. Line the robot up with a tape mark, then press ENTER and within 15 s "
              "rotate it by hand exactly 90 deg LEFT (counter-clockwise from above) and hold still...")
        n.spin_for(15.0)
        print("\nGYRO DURING THE 90 deg HAND TURN (raw units integrated):")
        for t, v in n.gyro_turn.items():
            print(f"  {t:16s} {v:+10.3f}  (= {math.degrees(v):+.1f} deg if rad/s)")
        v = n.gyro_turn.get('/imu/data')
        if v:
            scale = math.radians(90.0) / abs(v)
            settings['imu_gyro_scale'] = f"{scale:.6f}" + ("  (IMU publishes deg/s)" if abs(scale - 0.017453) < 0.002 else "")
            settings['imu_yaw_sign'] = '-1.0' if v < 0 else '1.0'

    if '--drive' in sys.argv:
        start = dict(n.pos)
        n.call(n.arm, '/lyra/arm')
        fwd = Twist()
        fwd.linear.x = 0.15
        try:
            print("Driving FORWARD 0.15 m/s for 3 s (commanded ~0.45 m)...")
            n.spin_for(3.0, fwd)
            n.spin_for(1.5, Twist())
        finally:
            for _ in range(10):
                n.cmd.publish(Twist())
            n.call(n.disarm, '/lyra/disarm')
        print("\nMEASURED DISTANCE:")
        moved = {}
        for t, (x0, y0) in start.items():
            x1, y1 = n.pos[t]
            moved[t] = math.hypot(x1 - x0, y1 - y0)
            print(f"  {t:22s} {moved[t]:.3f} m")
        try:
            real = float(input("\nReal distance driven, measured with a tape, in metres (e.g. 0.40): "))
        except (ValueError, EOFError):
            real = None
        if real and moved.get('/odometry/filtered'):
            settings['odom_distance_scale'] = f"{moved['/odometry/filtered'] / real:.2f}"

    if settings:
        print("\nSUGGESTED LAUNCH SETTINGS:")
        for k, v in settings.items():
            print(f"  {k}:={v}")

    n.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
