import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from sensor_msgs.msg import Image
from vision_msgs.msg import Detection2DArray, Detection2D, ObjectHypothesisWithPose

import numpy as np
from ultralytics import YOLO

from active_perception.image_utils import image_msg_to_bgr


class YoloDetectorNode(Node):
    def __init__(self):
        super().__init__('yolo_detector_node')

        self.declare_parameter('model_path', 'yolov8n.pt')
        self.declare_parameter('target_class', 'vase')
        self.declare_parameter('confidence_threshold', 0.25)

        model_path = self.get_parameter('model_path').value
        self.target_class = self.get_parameter('target_class').value
        self.conf_threshold = self.get_parameter('confidence_threshold').value

        # Load the YOLOv8 model (ultralytics downloads it if the path does not exist)
        self.get_logger().info(f"Loading YOLO model '{model_path}'...")
        self.model = YOLO(model_path)

        # Resolve the class name to its ID in the model's label map (COCO 'vase' is 75)
        name_to_id = {name: idx for idx, name in self.model.names.items()}
        if self.target_class not in name_to_id:
            raise ValueError(
                f"target_class '{self.target_class}' not in model classes: "
                f"{sorted(name_to_id)}")
        self.target_class_id = name_to_id[self.target_class]

        # Warm up so the first real snapshot is not slowed down by lazy init
        self.model(np.zeros((480, 640, 3), dtype=np.uint8), verbose=False)

        # Listens to the snapshot topic instead of the live feed
        self.image_sub = self.create_subscription(
            Image, '/snapshot/image', self.image_callback, 10
        )
        # Publishes to a snapshot bounding box topic
        self.detection_pub = self.create_publisher(
            Detection2DArray, '/snapshot/bounding_boxes', 10
        )
        self.get_logger().info(
            f"YOLO Detector ready. Target: '{self.target_class}' "
            f"(class {self.target_class_id}). Waiting for images...")

    def image_callback(self, msg: Image):
        detection_array = Detection2DArray()
        detection_array.header = msg.header

        try:
            cv_image = image_msg_to_bgr(msg)
        except ValueError as e:
            self.get_logger().error(f"Cannot convert snapshot: {e}")
            # Publish empty so the heuristic scorer still reports back
            self.detection_pub.publish(detection_array)
            return

        results = self.model(
            cv_image, classes=[self.target_class_id], conf=self.conf_threshold, verbose=False)

        # Parse results (ultralytics returns boxes sorted by confidence, highest first)
        for result in results:
            for box in result.boxes:
                # YOLO returns [x_center, y_center, width, height]
                xywh = box.xywh[0].cpu().numpy()
                confidence = float(box.conf[0])

                detection = Detection2D()
                detection.header = msg.header

                detection.bbox.center.position.x = float(xywh[0])
                detection.bbox.center.position.y = float(xywh[1])
                detection.bbox.size_x = float(xywh[2])
                detection.bbox.size_y = float(xywh[3])

                hypothesis = ObjectHypothesisWithPose()
                hypothesis.hypothesis.class_id = self.target_class
                hypothesis.hypothesis.score = confidence
                detection.results.append(hypothesis)

                detection_array.detections.append(detection)

        if detection_array.detections:
            best = detection_array.detections[0].results[0].hypothesis.score
            self.get_logger().info(
                f"{len(detection_array.detections)} x '{self.target_class}' detected "
                f"(best confidence {best:.2f})")
        else:
            self.get_logger().warn(f"No '{self.target_class}' detected in snapshot.")

        # Publish even if empty (so the heuristic node knows nothing was found)
        self.detection_pub.publish(detection_array)


def main(args=None):
    rclpy.init(args=args)
    node = YoloDetectorNode()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
