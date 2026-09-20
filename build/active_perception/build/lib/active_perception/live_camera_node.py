import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
import numpy as np

class LiveCameraNode(Node):
    def __init__(self):
        super().__init__('live_camera_node')
        
        # Open the default webcam (usually index 0)
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            self.get_logger().error("Cannot open webcam. Check connection or permissions.")
            
        self.image_pub = self.create_publisher(Image, '/camera/image_raw', 10)
        
        # Publish at ~10 FPS (100ms timer) to keep CPU usage low
        self.timer = self.create_timer(0.1, self.publish_frame)
        self.get_logger().info("Live Camera Node streaming on /camera/image_raw...")

    def publish_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            self.get_logger().warn("Failed to grab frame from webcam.")
            return

        # Bypass cv_bridge to avoid Python 3.12 compatibility bugs
        msg = Image()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "webcam_frame"
        msg.height, msg.width, _ = frame.shape
        msg.encoding = 'bgr8'
        msg.is_bigendian = False
        msg.step = msg.width * 3
        msg.data = frame.tobytes()

        self.image_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = LiveCameraNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.cap.release()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
