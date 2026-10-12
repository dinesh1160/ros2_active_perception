import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from rclpy.time import Time
from sensor_msgs.msg import Image
from std_srvs.srv import Trigger
from active_perception_interfaces.msg import HeuristicMetrics
from active_perception_interfaces.srv import AnalyzeQuality


class CoordinatorNode(Node):
    def __init__(self):
        super().__init__('coordinator_node')

        self.declare_parameter('camera_topic', '/pi_camera/image_raw')
        self.declare_parameter('target_object', 'vase')
        self.declare_parameter('min_sharpness', 50.0)
        self.declare_parameter('min_illumination', 30.0)
        self.declare_parameter('max_frame_age_sec', 2.0)
        self.declare_parameter('metrics_timeout_sec', 15.0)
        self.declare_parameter('vlm_timeout_sec', 30.0)

        camera_topic = self.get_parameter('camera_topic').value
        self.target_object = self.get_parameter('target_object').value
        self.MIN_SHARPNESS = self.get_parameter('min_sharpness').value
        self.MIN_ILLUMINATION = self.get_parameter('min_illumination').value
        self.max_frame_age = self.get_parameter('max_frame_age_sec').value
        self.metrics_timeout = self.get_parameter('metrics_timeout_sec').value
        self.vlm_timeout = self.get_parameter('vlm_timeout_sec').value

        self.state = 'IDLE'
        self.history = []
        self.eval_counter = 0
        self.latest_image = None
        self.latest_image_time = None
        # The frozen frame being evaluated (YOLO, heuristics and VLM all see this one)
        self.snapshot_image = None
        self.current_eval = None
        self.deadline = None

        # 1. Listen to the continuous camera stream quietly in the background.
        #    Sensor-data QoS (best effort) works with both reliable and best-effort publishers.
        self.create_subscription(Image, camera_topic, self.image_callback, qos_profile_sensor_data)

        # 2. The Gatekeeper: Publishes ONE frame only when triggered
        self.snapshot_pub = self.create_publisher(Image, '/snapshot/image', 10)

        # 3. Listen for the processed metrics returning from the snapshot pipeline
        self.create_subscription(HeuristicMetrics, '/snapshot/metrics', self.metrics_callback, 10)

        # Services
        self.vlm_client = self.create_client(AnalyzeQuality, '/analyze_view_quality')
        self.create_service(Trigger, '/evaluate_now', self.handle_evaluate_now)
        self.create_service(Trigger, '/finish_benchmark', self.handle_finish)

        # Watchdog so a lost message or hung VLM call can never wedge the state machine
        self.create_timer(0.5, self.watchdog_callback)

        self.get_logger().info(
            f"Coordinator ready. Camera: '{camera_topic}', target: '{self.target_object}'. "
            "Press ENTER in the trigger terminal to snap a frame.")

    def image_callback(self, msg: Image):
        if self.latest_image is None:
            self.get_logger().info(
                f"Camera feed received: {msg.width}x{msg.height} {msg.encoding}")
        self.latest_image = msg
        self.latest_image_time = self.get_clock().now()

    def handle_evaluate_now(self, request, response):
        if self.state != 'IDLE':
            response.success = False
            response.message = f"Busy ({self.state}) with {self.current_eval['frame']}."
            return response

        if self.latest_image is None:
            response.success = False
            response.message = "No camera feed detected."
            self.get_logger().error(response.message)
            return response

        now = self.get_clock().now()
        age = (now - self.latest_image_time).nanoseconds / 1e9
        if age > self.max_frame_age:
            response.success = False
            response.message = f"Camera feed is stale (last frame {age:.1f}s ago)."
            self.get_logger().error(response.message)
            return response

        self.eval_counter += 1
        self.current_eval = {
            'frame': f"Angle_{self.eval_counter}",
            'status': 'pending',
            'sharpness': 0.0,
            'illumination': 0.0,
            'vlm_occlusion': 0.0,
            'vlm_framing': 0.0,
            'total_score': 0.0,
            'reason': '',
        }

        # Freeze this frame and give it a unique stamp so results can be matched to it
        src = self.latest_image
        snapshot = Image()
        snapshot.header.frame_id = src.header.frame_id
        snapshot.header.stamp = now.to_msg()
        snapshot.height = src.height
        snapshot.width = src.width
        snapshot.encoding = src.encoding
        snapshot.is_bigendian = src.is_bigendian
        snapshot.step = src.step
        snapshot.data = src.data
        self.snapshot_image = snapshot

        self.state = 'WAITING_FOR_METRICS'
        self.deadline = now.nanoseconds + int(self.metrics_timeout * 1e9)

        self.get_logger().info(
            f"\n📸 SNAPSHOT {self.current_eval['frame']}: Sent to YOLO and Heuristics...")

        # Publish the single frame to wake up the rest of the pipeline
        self.snapshot_pub.publish(snapshot)

        response.success = True
        response.message = f"{self.current_eval['frame']} captured."
        return response

    def finish_eval(self, status, reason):
        """Record the current evaluation and return to IDLE."""
        self.current_eval['status'] = status
        self.current_eval['reason'] = reason
        self.history.append(self.current_eval)
        self.current_eval = None
        self.snapshot_image = None
        self.deadline = None
        self.state = 'IDLE'

    def metrics_callback(self, msg: HeuristicMetrics):
        # Only process metrics for the snapshot we are waiting on (ignore late/stale ones)
        if self.state != 'WAITING_FOR_METRICS':
            return
        if Time.from_msg(msg.header.stamp) != Time.from_msg(self.snapshot_image.header.stamp):
            self.get_logger().warn("Ignoring metrics from an older snapshot.")
            return

        if not msg.target_detected:
            self.get_logger().warn(f"Discarded: no '{self.target_object}' detected.")
            self.finish_eval('no_target', f"No {self.target_object} detected")
            self.get_logger().info("Ready for next angle.")
            return

        self.current_eval['sharpness'] = msg.sharpness_score
        self.current_eval['illumination'] = msg.illumination_score

        self.get_logger().info(
            f"Heuristics -> Sharpness: {msg.sharpness_score:.1f}, "
            f"Illum: {msg.illumination_score:.1f}")

        # 1. Fast Heuristics Check
        if msg.sharpness_score < self.MIN_SHARPNESS or msg.illumination_score < self.MIN_ILLUMINATION:
            reason = "Failed Heuristics (Blurry or Dark)"
            self.get_logger().warn(f"Discarded: {reason}")
            self.finish_eval('rejected', reason)
            self.get_logger().info("Ready for next angle.")
            return

        # 2. VLM Check (Async) - non-blocking readiness check inside the callback
        if not self.vlm_client.service_is_ready():
            self.get_logger().error("VLM offline.")
            self.finish_eval('vlm_error', "VLM service offline")
            return

        self.get_logger().info("Heuristics passed! Querying VLM...")
        self.state = 'PROCESSING_VLM'
        self.deadline = self.get_clock().now().nanoseconds + int(self.vlm_timeout * 1e9)

        req = AnalyzeQuality.Request()
        req.image = self.snapshot_image
        req.target_object = self.target_object
        future = self.vlm_client.call_async(req)
        eval_ref = self.current_eval
        future.add_done_callback(lambda fut: self.vlm_response_callback(fut, eval_ref))

    def vlm_response_callback(self, future, eval_ref):
        # The watchdog may have already given up on this evaluation
        if self.state != 'PROCESSING_VLM' or eval_ref is not self.current_eval:
            self.get_logger().warn(f"Late VLM response for {eval_ref['frame']} ignored.")
            return

        try:
            res = future.result()
        except Exception as e:
            self.get_logger().error(f"VLM Call Failed: {e}")
            self.finish_eval('vlm_error', f"VLM call failed: {e}")
            return

        if not res.success:
            self.get_logger().error(f"VLM returned an error: {res.reasoning}")
            self.finish_eval('vlm_error', res.reasoning)
            return

        self.current_eval['vlm_occlusion'] = res.occlusion_score
        self.current_eval['vlm_framing'] = res.framing_score
        self.current_eval['total_score'] = (res.occlusion_score + res.framing_score) / 2.0
        self.get_logger().info(
            f"VLM Score -> Occ: {res.occlusion_score:.0f}, "
            f"Frame: {res.framing_score:.0f} ({res.reasoning})")
        self.finish_eval('scored', res.reasoning)
        self.get_logger().info("✅ Done. Ready for next angle.")

    def watchdog_callback(self):
        if self.deadline is None or self.get_clock().now().nanoseconds < self.deadline:
            return
        stage = 'heuristic metrics' if self.state == 'WAITING_FOR_METRICS' else 'VLM response'
        self.get_logger().error(
            f"Timed out waiting for {stage} on {self.current_eval['frame']}. "
            "Is every node running? Resetting to IDLE.")
        self.finish_eval('timeout', f"Timed out waiting for {stage}")

    def handle_finish(self, request, response):
        if not self.history:
            response.success = False
            response.message = "No angles evaluated yet."
            return response

        self.get_logger().info("\n================ BENCHMARK COMPLETE ================\n")

        for item in self.history:
            if item['status'] == 'scored':
                self.get_logger().info(
                    f"[{item['frame']}] Score: {item['total_score']:.1f} | "
                    f"Heuristics: [Blur:{item['sharpness']:.1f}, Light:{item['illumination']:.1f}] | "
                    f"VLM: [Occ:{item['vlm_occlusion']:.0f}, Frame:{item['vlm_framing']:.0f}] "
                    f"-> {item['reason']}"
                )
            else:
                self.get_logger().info(
                    f"[{item['frame']}] {item['status'].upper()} -> {item['reason']}")

        # Only frames that passed every stage are eligible for best angle
        scored = [item for item in self.history if item['status'] == 'scored']
        if scored:
            best = max(scored, key=lambda item: item['total_score'])
            response.message = f"Best angle: {best['frame']} (Score: {best['total_score']:.1f})"
            self.get_logger().info(f"\n🏆 BEST ANGLE: {best['frame']} (Score: {best['total_score']:.1f})\n")
        else:
            response.message = "No angle passed all checks."
            self.get_logger().warn(f"\n{response.message}\n")
        self.get_logger().info("====================================================\n")

        response.success = True
        return response


def main(args=None):
    rclpy.init(args=args)
    node = CoordinatorNode()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
