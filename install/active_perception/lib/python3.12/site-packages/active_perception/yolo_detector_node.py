import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from vision_msgs.msg import Detection2DArray, Detection2D, ObjectHypothesisWithPose

import numpy as np
from ultralytics import YOLO

class YoloDetectorNode(Node):
    def __init__(self):
        super().__init__('yolo_detector_node')

        # Load the lightweight YOLOv8 nano model (will auto-download on first run)
        self.get_logger().info("Loading YOLOv8n model...")
        self.model = YOLO('yolov8n.pt')
        
        # COCO dataset class ID for 'bottle' is 39
        self.TARGET_CLASS_ID = 75

        # Now listens to the snapshot topic instead of the live feed
        self.image_sub = self.create_subscription(
            Image, '/snapshot/image', self.image_callback, 10
        )
        # Publishes to a snapshot bounding box topic
        self.detection_pub = self.create_publisher(
            Detection2DArray, '/snapshot/bounding_boxes', 10
        )
        self.get_logger().info("YOLOv8 Detector ready. Waiting for images...")

    def image_msg_to_cv2(self, msg: Image) -> np.ndarray:
        """Convert ROS Image to OpenCV format safely."""
        img = np.frombuffer(msg.data, dtype=np.uint8)
        img = img.reshape((msg.height, msg.width, 3))
        return img

    def image_callback(self, msg: Image):
        cv_image = self.image_msg_to_cv2(msg)

   
        results = self.model(cv_image, verbose=False)  # Disable verbose logging for cleaner output
        
        detection_array = Detection2DArray()
        detection_array.header = msg.header

        # Parse results
        for result in results:
            boxes = result.boxes
            for box in boxes:
                class_id = int(box.cls[0])
                
                # Only process if the detected object is a bottle
                if class_id == self.TARGET_CLASS_ID:
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
                    hypothesis.hypothesis.class_id = "bottle"
                    hypothesis.hypothesis.score = confidence
                    detection.results.append(hypothesis)

                    detection_array.detections.append(detection)

                    self.get_logger().info(f"Bottle detected! Confidence: {confidence:.2f}")

        # Publish even if empty (so the heuristic node knows nothing was found)
        self.detection_pub.publish(detection_array)


def main(args=None):
    rclpy.init(args=args)
    node = YoloDetectorNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
