import os
import glob
import cv2
import numpy as np

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_srvs.srv import Trigger
from cv_bridge import CvBridge


class MockCameraNode(Node):
    def __init__(self):
        super().__init__('mock_camera_node')

        # Updated parameter to point inside the workspace
        default_dir = os.path.expanduser('~/active_perception_ws/src/active_perception/test_data')
        self.declare_parameter('data_dir', default_dir)
        self.data_dir = self.get_parameter('data_dir').get_parameter_value().string_value

        self.bridge = CvBridge()
        self.current_frame_index = 0

        # Load image file paths
        supported_exts = ('*.jpg', '*.jpeg', '*.png')
        self.image_paths = []
        for ext in supported_exts:
            self.image_paths.extend(glob.glob(os.path.join(self.data_dir, ext)))
        self.image_paths.sort()

        if not self.image_paths:
            self.get_logger().warn(
                f"No test images found in {self.data_dir}. Generating synthetic test frames..."
            )
            self._create_dummy_dataset()

        # Publisher for raw camera frame
        self.image_pub = self.create_publisher(Image, '/camera/image_raw', 10)

        # Service to advance to the next frame on demand
        self.step_srv = self.create_service(Trigger, '/mock/next_frame', self.handle_next_frame)

        self.get_logger().info(
            f"Mock Camera ready with {len(self.image_paths)} frames. "
            "Streaming continuously at 2 FPS."
        )

        # Simulate a real camera by publishing the current frame continuously (every 0.5 seconds)
        self.timer = self.create_timer(0.5, self.publish_current_frame)

    def _create_dummy_dataset(self):
        """Generates 3 basic images so the system works out of the box."""
        os.makedirs(self.data_dir, exist_ok=True)
        for i in range(1, 4):
            img = np.zeros((480, 640, 3), dtype=np.uint8)
            # Draw a sample rectangle representing an object
            cv2.rectangle(img, (260, 110), (380, 370), (0, 255 - (i * 40), 100 + (i * 40)), -1)
            cv2.putText(img, f"Frame {i}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 2)
            path = os.path.join(self.data_dir, f"frame_0{i}.jpg")
            cv2.imwrite(path, img)
            self.image_paths.append(path)
        self.image_paths.sort()

    def publish_current_frame(self):
        if not self.image_paths:
            return

        image_path = self.image_paths[self.current_frame_index]
        cv_image = cv2.imread(image_path)
        if cv_image is None:
            self.get_logger().error(f"Failed to read image at {image_path}")
            return

        # Manually construct the Image message to bypass the cv_bridge KeyError: 16 bug
        msg = Image()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = os.path.basename(image_path)
        
        msg.height = cv_image.shape[0]
        msg.width = cv_image.shape[1]
        msg.encoding = 'bgr8'
        msg.is_bigendian = False
        msg.step = cv_image.shape[1] * 3  # Width * 3 channels (BGR)
        msg.data = cv_image.tobytes()

        self.image_pub.publish(msg)
        self.get_logger().info(
            f"Published [{self.current_frame_index + 1}/{len(self.image_paths)}]: {os.path.basename(image_path)}"
        )

    def handle_next_frame(self, request, response):
        if self.current_frame_index + 1 < len(self.image_paths):
            self.current_frame_index += 1
            self.publish_current_frame()
            response.success = True
            response.message = f"Advanced to frame {self.current_frame_index + 1}: {self.image_paths[self.current_frame_index]}"
        else:
            response.success = False
            response.message = "Reached end of image sequence. No more frames."
            self.get_logger().warn(response.message)
        return response


def main(args=None):
    rclpy.init(args=args)
    node = MockCameraNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
