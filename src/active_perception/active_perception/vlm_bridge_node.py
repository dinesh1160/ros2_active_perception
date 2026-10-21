import os
import hashlib
import cv2

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from active_perception_interfaces.srv import AnalyzeQuality
from active_perception.image_utils import image_msg_to_bgr
from active_perception.vlm import GeminiJudge, load_env_file


class VlmBridgeNode(Node):
    def __init__(self):
        super().__init__('vlm_bridge_node')

        self.declare_parameter('model', 'gemini-3.6-flash')
        self.declare_parameter('env_file', '.env')
        self.declare_parameter('request_timeout_sec', 20.0)
        self.model = self.get_parameter('model').value
        env_file = self.get_parameter('env_file').value
        timeout_sec = self.get_parameter('request_timeout_sec').value

        # Load GEMINI_API_KEY from the .env file if it isn't already exported
        if 'GEMINI_API_KEY' not in os.environ and load_env_file(env_file):
            self.get_logger().info(f"Loaded environment from '{os.path.abspath(env_file)}'")

        # Verify API key exists
        self.client = None
        api_key = os.environ.get('GEMINI_API_KEY')
        if not api_key:
            self.get_logger().error(
                "GEMINI_API_KEY is missing (not exported and not found in env_file "
                f"'{env_file}'). Every VLM call will fail.")
        else:
            self.client = GeminiJudge(api_key, self.model, timeout_sec)

        # Create the Service Server
        self.srv = self.create_service(
            AnalyzeQuality,
            '/analyze_view_quality',
            self.analyze_callback
        )

        self.get_logger().info(
            f"VLM Bridge Node ready (model '{self.model}'). "
            "Waiting for service calls on /analyze_view_quality.")

    def analyze_callback(self, request, response):
        # Same hash the coordinator records in results.json -> proves it is the same frame
        frame_hash = hashlib.md5(bytes(request.image.data)).hexdigest()[:12]
        self.get_logger().info(f"Received image for VLM analysis (frame hash {frame_hash}). Processing...")
        target = request.target_object or 'object'

        try:
            if self.client is None:
                raise RuntimeError('GEMINI_API_KEY not set')

            # 1. Convert ROS Image to JPEG bytes
            cv_image = image_msg_to_bgr(request.image)
            ok, buffer = cv2.imencode('.jpg', cv_image)
            if not ok:
                raise RuntimeError('JPEG encoding failed')
            image_bytes = buffer.tobytes()

            # 2. Ask Gemini (scores clamped to 0-100)
            occlusion, framing, reasoning = self.client(image_bytes, target)

            # 3. Populate the ROS 2 Service Response
            response.occlusion_score = occlusion
            response.framing_score = framing
            response.reasoning = reasoning
            response.success = True

            self.get_logger().info(f"VLM Result: {response.reasoning}")

        except Exception as e:
            self.get_logger().error(f"VLM API Call Failed: {e}")
            response.success = False
            response.occlusion_score = 0.0
            response.framing_score = 0.0
            response.reasoning = f"Error: {e}"

        return response


def main(args=None):
    rclpy.init(args=args)
    node = VlmBridgeNode()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
