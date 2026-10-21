import glob
import os

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import CompressedImage, Image
import cv2

EXTENSIONS = ('*.jpg', '*.jpeg', '*.png', '*.bmp')


class ImagePlayerNode(Node):
    def __init__(self):
        super().__init__('image_player_node')

        self.declare_parameter('image_dir', 'eval/base')
        self.declare_parameter('camera_topic', '/pi_camera/image_raw/compressed')
        self.declare_parameter('fps', 10.0)
        self.declare_parameter('advance_on_snapshot', True)
        self.declare_parameter('loop', True)
        image_dir = self.get_parameter('image_dir').value
        topic = self.get_parameter('camera_topic').value
        self.loop = self.get_parameter('loop').value

        self.files = sorted(
            f for ext in EXTENSIONS for f in glob.glob(os.path.join(image_dir, ext)))
        if not self.files:
            raise RuntimeError(f"No images found in '{os.path.abspath(image_dir)}'")
        self.index = 0
        self.frame = None
        self.load(0)

        self.compressed = topic.endswith('/compressed')
        msg_type = CompressedImage if self.compressed else Image
        self.image_pub = self.create_publisher(msg_type, topic, qos_profile_sensor_data)
        if self.get_parameter('advance_on_snapshot').value:
            self.create_subscription(Image, '/snapshot/image', self.snapshot_callback, 10)
        self.create_timer(1.0 / self.get_parameter('fps').value, self.publish_frame)
        self.get_logger().info(
            f"Image player: {len(self.files)} images from '{image_dir}' on {topic}.")

    def load(self, index):
        frame = cv2.imread(self.files[index])
        if frame is None:
            raise RuntimeError(f"Cannot read {self.files[index]}")
        self.index, self.frame = index, frame
        self.get_logger().info(f"Now showing [{index + 1}/{len(self.files)}] "
                               f"{os.path.basename(self.files[index])}")

    def snapshot_callback(self, _msg):
        nxt = self.index + 1
        if nxt >= len(self.files):
            if not self.loop:
                return
            nxt = 0
        self.load(nxt)

    def publish_frame(self):
        stamp = self.get_clock().now().to_msg()
        if self.compressed:
            msg = CompressedImage()
            msg.header.stamp = stamp
            msg.header.frame_id = 'image_player'
            msg.format = 'jpeg'
            jpeg = cv2.imencode('.jpg', self.frame, [cv2.IMWRITE_JPEG_QUALITY, 95])[1]
            msg.data = jpeg.tobytes()
        else:
            msg = Image()
            msg.header.stamp = stamp
            msg.header.frame_id = 'image_player'
            msg.height, msg.width = self.frame.shape[:2]
            msg.encoding = 'bgr8'
            msg.step = msg.width * 3
            msg.data = self.frame.tobytes()
        self.image_pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = ImagePlayerNode()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
