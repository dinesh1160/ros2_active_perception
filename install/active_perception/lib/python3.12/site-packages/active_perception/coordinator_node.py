import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_srvs.srv import Trigger
from active_perception_interfaces.msg import HeuristicMetrics
from active_perception_interfaces.srv import AnalyzeQuality

class CoordinatorNode(Node):
    def __init__(self):
        super().__init__('coordinator_node')

        self.state = 'IDLE'
        self.history = []
        self.eval_counter = 0
        self.latest_image = None
        self.current_frame_name = ""

        self.MIN_SHARPNESS = 5.0        
        self.MIN_ILLUMINATION = 30.0    

        # 1. Listen to the continuous webcam stream quietly in the background
        self.create_subscription(Image, '/camera/image_raw', self.image_callback, 10)
        
        # 2. The Gatekeeper: Publishes ONE frame only when triggered
        self.snapshot_pub = self.create_publisher(Image, '/snapshot/image', 10)
        
        # 3. Listen for the processed metrics returning from the snapshot pipeline
        self.create_subscription(HeuristicMetrics, '/snapshot/metrics', self.metrics_callback, 10)

        # Services
        self.vlm_client = self.create_client(AnalyzeQuality, '/analyze_view_quality')
        self.create_service(Trigger, '/evaluate_now', self.handle_evaluate_now)
        self.create_service(Trigger, '/finish_benchmark', self.handle_finish)

        self.get_logger().info("Coordinator ready. Press ENTER in the trigger terminal to snap a frame.")

    def image_callback(self, msg: Image):
        self.latest_image = msg

    def handle_evaluate_now(self, request, response):
        if self.state != 'IDLE':
            response.success = False
            return response

        if self.latest_image is None:
            response.success = False
            self.get_logger().error("No camera feed detected.")
            return response

        self.state = 'WAITING_FOR_METRICS'
        self.eval_counter += 1
        self.current_frame_name = f"Angle_{self.eval_counter}"
        
        self.get_logger().info(f"\n📸 SNAPSHOT {self.current_frame_name}: Sent to YOLO and Heuristics...")
        
        # Publish the single frame to wake up the rest of the pipeline
        self.snapshot_pub.publish(self.latest_image)
        
        response.success = True
        return response

    def metrics_callback(self, msg: HeuristicMetrics):
        # Only process metrics if we just requested a snapshot
        if self.state != 'WAITING_FOR_METRICS':
            return

        self.state = 'PROCESSING_VLM'
        
        current_eval = {
            'frame': self.current_frame_name,
            'sharpness': msg.sharpness_score,
            'illumination': msg.illumination_score,
            'vlm_occlusion': 0.0,
            'vlm_framing': 0.0,
            'total_score': 0.0,
            'reason': ''
        }

        self.get_logger().info(f"Heuristics -> Sharpness: {msg.sharpness_score:.1f}, Illum: {msg.illumination_score:.1f}")

        # 1. Fast Heuristics Check
        if current_eval['sharpness'] < self.MIN_SHARPNESS or current_eval['illumination'] < self.MIN_ILLUMINATION:
            current_eval['reason'] = "Failed Heuristics (Blurry or Dark)"
            self.history.append(current_eval)
            self.get_logger().warn(f"Discarded: {current_eval['reason']}")
            self.state = 'IDLE'
            return

        # 2. VLM Check (Async)
        self.get_logger().info("Heuristics passed! Querying VLM...")
        if not self.vlm_client.wait_for_service(timeout_sec=2.0):
            self.get_logger().error("VLM offline.")
            self.state = 'IDLE'
            return

        req = AnalyzeQuality.Request()
        req.image = self.latest_image
        future = self.vlm_client.call_async(req)
        future.add_done_callback(lambda fut: self.vlm_response_callback(fut, current_eval))

    def vlm_response_callback(self, future, current_eval):
        try:
            res = future.result()
            current_eval['vlm_occlusion'] = res.occlusion_score
            current_eval['vlm_framing'] = res.framing_score
            current_eval['reason'] = res.reasoning
            current_eval['total_score'] = (res.occlusion_score + res.framing_score) / 2.0
            
            self.history.append(current_eval)
            self.get_logger().info(f"VLM Score -> Occ: {res.occlusion_score}, Frame: {res.framing_score} ({res.reasoning})")

        except Exception as e:
            self.get_logger().error(f"VLM Call Failed: {e}")
        
        self.state = 'IDLE'
        self.get_logger().info("✅ Done. Ready for next angle.")

    def handle_finish(self, request, response):
        if not self.history:
            response.success = False
            return response

        self.get_logger().info("\n================ BENCHMARK COMPLETE ================\n")
        best_frame = None
        best_score = -1.0
        
        for item in self.history:
            self.get_logger().info(
                f"[{item['frame']}] Score: {item['total_score']:.1f} | "
                f"Heuristics: [Blur:{item['sharpness']:.1f}, Light:{item['illumination']:.1f}] | "
                f"VLM: [Occ:{item['vlm_occlusion']}, Frame:{item['vlm_framing']}] -> {item['reason']}"
            )
            if item['total_score'] > best_score:
                best_score = item['total_score']
                best_frame = item['frame']
                
        self.get_logger().info(f"\n🏆 BEST ANGLE: {best_frame} (Score: {best_score:.1f})\n")
        self.get_logger().info("====================================================\n")

        response.success = True
        return response

def main(args=None):
    rclpy.init(args=args)
    node = CoordinatorNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()