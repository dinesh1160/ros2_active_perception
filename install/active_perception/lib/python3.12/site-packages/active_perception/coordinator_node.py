import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_srvs.srv import Trigger

from active_perception_interfaces.msg import HeuristicMetrics
from active_perception_interfaces.srv import AnalyzeQuality


class CoordinatorNode(Node):
    def __init__(self):
        super().__init__('coordinator_node')

        # State & Configuration
        self.state = 'WAITING_FOR_FRAME'
        self.retry_count = 0
        self.MAX_RETRIES = 5
        self.latest_image = None

        # Evaluation Thresholds
        self.MIN_SHARPNESS = 5.0        # Set low for synthetic dummy images
        self.MIN_ILLUMINATION = 30.0    # Set low for synthetic dummy images
        self.MIN_OCCLUSION = 80.0
        self.MIN_FRAMING = 80.0

        # Subscriptions
        self.image_sub = self.create_subscription(
            Image, '/camera/image_raw', self.image_callback, 10
        )
        self.metrics_sub = self.create_subscription(
            HeuristicMetrics, '/metrics/heuristics', self.metrics_callback, 10
        )

        # Service Clients
        self.vlm_client = self.create_client(AnalyzeQuality, '/analyze_view_quality')
        self.move_client = self.create_client(Trigger, '/mock/next_frame')

        self.get_logger().info("Coordinator Brain is online. Waiting for telemetry...")

    def image_callback(self, msg: Image):
        # Cache the latest image so we can send it to the VLM when requested
        self.latest_image = msg

    def metrics_callback(self, msg: HeuristicMetrics):
        # Only process if we are waiting for a new evaluation
        if self.state != 'WAITING_FOR_FRAME':
            return

        self.state = 'PROCESSING'
        self.get_logger().info(f"--- [Attempt {self.retry_count + 1}] Evaluating Frame ---")

        # 1. Evaluate Heuristics (Fast/Cheap)
        if msg.sharpness_score < self.MIN_SHARPNESS:
            self.trigger_reposition(f"Heuristics Failed: Too blurry ({msg.sharpness_score:.1f} < {self.MIN_SHARPNESS})")
            return
        
        if msg.illumination_score < self.MIN_ILLUMINATION:
            self.trigger_reposition(f"Heuristics Failed: Too dark ({msg.illumination_score:.1f} < {self.MIN_ILLUMINATION})")
            return

        self.get_logger().info("Heuristics Passed. Querying VLM for semantic occlusion...")
        self.query_vlm()

    def query_vlm(self):
        if not self.vlm_client.wait_for_service(timeout_sec=3.0):
            self.get_logger().error("VLM Service not available! Aborting.")
            return

        if self.latest_image is None:
            self.get_logger().error("No image available to send to VLM!")
            return

        req = AnalyzeQuality.Request()
        req.image = self.latest_image
        
        # Async call prevents the node from locking up while waiting for the internet
        future = self.vlm_client.call_async(req)
        future.add_done_callback(self.vlm_response_callback)
        self.state = 'WAITING_FOR_VLM'

    def vlm_response_callback(self, future):
        try:
            res = future.result()
            
            # 2. Evaluate VLM (Semantic/Expensive)
            if res.occlusion_score < self.MIN_OCCLUSION or res.framing_score < self.MIN_FRAMING:
                reason = f"VLM Failed [O:{res.occlusion_score} F:{res.framing_score}]: {res.reasoning}"
                self.trigger_reposition(reason)
            else:
                self.get_logger().info(f"SUCCESS! Golden view found. VLM reasoning: {res.reasoning}")
                self.state = 'DONE'

        except Exception as e:
            self.get_logger().error(f"Service call failed: {e}")
            self.trigger_reposition("VLM Service Call Failed.")

    def trigger_reposition(self, reason: str):
        self.get_logger().warn(f"Action triggered: Requesting Next-Best-View. Reason: {reason}")
        
        if self.retry_count >= self.MAX_RETRIES:
            self.get_logger().error("Max retries reached. Hysteresis triggered. Accepting suboptimal frame.")
            self.state = 'DONE'
            return

        self.retry_count += 1
        
        # Call the mock navigation to advance the dataset
        if self.move_client.wait_for_service(timeout_sec=2.0):
            future = self.move_client.call_async(Trigger.Request())
            future.add_done_callback(self.move_response_callback)
        else:
            self.get_logger().error("Mock Move Service not available!")

    def move_response_callback(self, future):
        res = future.result()
        if res.success:
            self.get_logger().info("Rover moved successfully. Awaiting new telemetry...")
            self.state = 'WAITING_FOR_FRAME'
        else:
            self.get_logger().error(f"Move failed/End of data: {res.message}")
            self.state = 'DONE'


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
