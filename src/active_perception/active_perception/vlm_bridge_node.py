import os
import json
import hashlib
import cv2

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from active_perception_interfaces.srv import AnalyzeQuality
from active_perception.image_utils import image_msg_to_bgr

from google import genai
from google.genai import types

# Structured output so Gemini always returns exactly these keys
RESPONSE_SCHEMA = types.Schema(
    type=types.Type.OBJECT,
    properties={
        'occlusion_score': types.Schema(type=types.Type.NUMBER),
        'framing_score': types.Schema(type=types.Type.NUMBER),
        'reasoning': types.Schema(type=types.Type.STRING),
    },
    required=['occlusion_score', 'framing_score', 'reasoning'],
)


def load_env_file(path: str):
    """Minimal .env loader (KEY=VALUE lines). Existing env vars win."""
    if not path or not os.path.isfile(path):
        return False
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#') or '=' not in line:
                continue
            key, value = line.split('=', 1)
            key = key.strip().removeprefix('export ').strip()
            value = value.strip().strip('"').strip("'")
            os.environ.setdefault(key, value)
    return True


class VlmBridgeNode(Node):
    def __init__(self):
        super().__init__('vlm_bridge_node')

        self.declare_parameter('model', 'gemini-3.6-flash')
        self.declare_parameter('env_file', '.env')
        self.declare_parameter('request_timeout_sec', 20.0)
        self.model = self.get_parameter('model').value
        env_file = self.get_parameter('env_file').value
        timeout_ms = int(self.get_parameter('request_timeout_sec').value * 1000)

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
            self.client = genai.Client(
                api_key=api_key, http_options=types.HttpOptions(timeout=timeout_ms))

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

            # 2. Describe the scores we want back
            prompt = (
                f"You are an active perception judge for a rover. Look at the target object ({target}) "
                "in this image. "
                f"1. occlusion_score: Is the {target} blocked by anything? "
                "(Score 0-100, where 100 is fully visible). "
                f"2. framing_score: Is the entire {target} in the frame? "
                "(Score 0-100, where 100 is perfect). "
                "3. reasoning: Provide a 1-sentence explanation of your scores."
            )

            # 3. Call Gemini with a structured JSON response
            vlm_response = self.client.models.generate_content(
                model=self.model,
                contents=[
                    types.Part.from_bytes(data=image_bytes, mime_type='image/jpeg'),
                    prompt
                ],
                config=types.GenerateContentConfig(
                    response_mime_type='application/json',
                    response_schema=RESPONSE_SCHEMA,
                )
            )

            # 4. Parse the JSON response
            result = json.loads(vlm_response.text)

            # 5. Populate the ROS 2 Service Response (clamped to 0-100)
            response.occlusion_score = min(100.0, max(0.0, float(result['occlusion_score'])))
            response.framing_score = min(100.0, max(0.0, float(result['framing_score'])))
            response.reasoning = str(result['reasoning'])
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
