import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import Image
import cv2


class LiveCameraNode(Node):
    """Optional local webcam publisher (the demo uses the robot's /pi_camera/image_raw)."""

    def __init__(self):
        super().__init__('live_camera_node')

        self.declare_parameter('camera_topic', '/pi_camera/image_raw')
        self.declare_parameter('device_index', 0)
        self.declare_parameter('fps', 10.0)
        topic = self.get_parameter('camera_topic').value
        device = self.get_parameter('device_index').value

        self.cap = cv2.VideoCapture(device)
        if not self.cap.isOpened():
            raise RuntimeError(f"Cannot open webcam {device}. Check connection or permissions.")

        self.image_pub = self.create_publisher(Image, topic, qos_profile_sensor_data)

        self.timer = self.create_timer(1.0 / self.get_parameter('fps').value, self.publish_frame)
        self.get_logger().info(f"Live Camera Node streaming on {topic}...")

    def publish_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            self.get_logger().warn("Failed to grab frame from webcam.", throttle_duration_sec=5.0)
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

    def destroy_node(self):
        self.cap.release()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = LiveCameraNode()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
