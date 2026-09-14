import os
import json

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from vision_msgs.msg import Detection2DArray, Detection2D, ObjectHypothesisWithPose


class MockDetectorNode(Node):
    def __init__(self):
        super().__init__('mock_detector_node')

        # Updated parameter to point inside the workspace
        default_annotations = os.path.expanduser('~/active_perception_ws/src/active_perception/test_data/annotations.json')
        self.declare_parameter('annotations_file', default_annotations)
        self.annotations_file = self.get_parameter('annotations_file').get_parameter_value().string_value

        self.annotations = {}
        self._load_annotations()

        # Subscribe to camera feed
        self.image_sub = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.image_callback,
            10
        )

        # Publish bounding boxes
        self.detection_pub = self.create_publisher(
            Detection2DArray,
            '/detections/bounding_boxes',
            10
        )

        self.get_logger().info("Mock Detector ready. Listening to /camera/image_raw.")

    def _load_annotations(self):
        if os.path.exists(self.annotations_file):
            try:
                with open(self.annotations_file, 'r') as f:
                    self.annotations = json.load(f)
                self.get_logger().info(f"Loaded annotations for {len(self.annotations)} images.")
            except Exception as e:
                self.get_logger().error(f"Failed to read annotations file: {e}")
        else:
            self.get_logger().warn("Annotations file not found. Defaulting to center bounding boxes.")

    def image_callback(self, msg: Image):
        filename = msg.header.frame_id
        detection_array = Detection2DArray()
        detection_array.header = msg.header

        detection = Detection2D()
        detection.header = msg.header

        # Check if manual annotation exists for this image
        if filename in self.annotations:
            bbox_data = self.annotations[filename]
            center_x = float(bbox_data['center_x'])
            center_y = float(bbox_data['center_y'])
            size_x = float(bbox_data['size_x'])
            size_y = float(bbox_data['size_y'])
        else:
            # Fallback: estimate a centered bounding box
            center_x = float(msg.width / 2.0)
            center_y = float(msg.height / 2.0)
            size_x = float(msg.width * 0.3)
            size_y = float(msg.height * 0.5)

        # Populate BoundingBox2D
        detection.bbox.center.position.x = center_x
        detection.bbox.center.position.y = center_y
        detection.bbox.size_x = size_x
        detection.bbox.size_y = size_y

        # Populate Hypothesis
        hypothesis = ObjectHypothesisWithPose()
        hypothesis.hypothesis.class_id = "bottle"
        hypothesis.hypothesis.score = 0.95
        detection.results.append(hypothesis)

        detection_array.detections.append(detection)
        self.detection_pub.publish(detection_array)

        self.get_logger().info(
            f"Published detection for '{filename}' -> Center: ({center_x:.1f}, {center_y:.1f}), Size: ({size_x:.1f}, {size_y:.1f})"
        )


def main(args=None):
    rclpy.init(args=args)
    node = MockDetectorNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
