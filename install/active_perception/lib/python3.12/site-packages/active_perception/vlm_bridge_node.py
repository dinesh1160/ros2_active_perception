import os
import json
import cv2
import numpy as np

import rclpy
from rclpy.node import Node
from active_perception_interfaces.srv import AnalyzeQuality

from google import genai
from google.genai import types


class VlmBridgeNode(Node):
    def __init__(self):
        super().__init__('vlm_bridge_node')

        # Verify API key exists
        self.api_key = os.environ.get("GEMINI_API_KEY")
        if not self.api_key:
            self.get_logger().error("GEMINI_API_KEY environment variable is missing! Node will fail on call.")
        else:
            self.client = genai.Client(api_key=self.api_key)

        # Create the Service Server
        self.srv = self.create_service(
            AnalyzeQuality, 
            '/analyze_view_quality', 
            self.analyze_callback
        )

        self.get_logger().info("VLM Bridge Node ready. Waiting for service calls on /analyze_view_quality.")

    def image_msg_to_cv2(self, msg) -> np.ndarray:
        """Manually converts ROS Image to OpenCV format."""
        img = np.frombuffer(msg.data, dtype=np.uint8)
        img = img.reshape((msg.height, msg.width, 3))
        return img

    def analyze_callback(self, request, response):
        self.get_logger().info("Received image for VLM analysis. Processing...")

        try:
            # 1. Convert ROS Image to JPEG bytes
            cv_image = self.image_msg_to_cv2(request.image)
            _, buffer = cv2.imencode('.jpg', cv_image)
            image_bytes = buffer.tobytes()

            # 2. Define the exact JSON schema we want back
            prompt = (
                "You are an active perception judge for a rover. Look at the target object (water bottle) in this image. "
                "1. occlusion_score: Is the bottle blocked by anything? (Score 0-100, where 100 is fully visible). "
                "2. framing_score: Is the entire bottle in the frame? (Score 0-100, where 100 is perfect). "
                "3. reasoning: Provide a 1-sentence explanation of your scores."
            )

            # 3. Call Gemini 1.5 Flash (Fastest model for robotics loops)
            vlm_response = self.client.models.generate_content(
                model='gemini-1.5-flash',
                contents=[
                    types.Part.from_bytes(data=image_bytes, mime_type='image/jpeg'),
                    prompt
                ],
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                )
            )

            # 4. Parse the JSON response
            result = json.loads(vlm_response.text)
            
            # 5. Populate the ROS 2 Service Response
            response.occlusion_score = float(result.get('occlusion_score', 0.0))
            response.framing_score = float(result.get('framing_score', 0.0))
            response.reasoning = str(result.get('reasoning', 'No reasoning provided.'))

            self.get_logger().info(f"VLM Result: {response.reasoning}")

        except Exception as e:
            self.get_logger().error(f"VLM API Call Failed: {e}")
            response.occlusion_score = 0.0
            response.framing_score = 0.0
            response.reasoning = f"Error: {str(e)}"

        return response


def main(args=None):
    rclpy.init(args=args)
    node = VlmBridgeNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
