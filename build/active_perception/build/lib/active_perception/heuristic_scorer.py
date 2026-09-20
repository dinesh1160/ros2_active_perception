import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from vision_msgs.msg import Detection2DArray
import message_filters

import cv2
import numpy as np

# Import the custom message you built in Phase 1
from active_perception_interfaces.msg import HeuristicMetrics


class HeuristicScorerNode(Node):
    def __init__(self):
        super().__init__('heuristic_scorer_node')

       # Synchronize the SNAPSHOT image and bounding box topics
        self.image_sub = message_filters.Subscriber(self, Image, '/snapshot/image')
        self.bbox_sub = message_filters.Subscriber(self, Detection2DArray, '/snapshot/bounding_boxes')
        self.ts = message_filters.TimeSynchronizer([self.image_sub, self.bbox_sub], queue_size=10)
        self.ts.registerCallback(self.sync_callback)

        # Publish to the snapshot metrics topic
        self.metrics_pub = self.create_publisher(HeuristicMetrics, '/snapshot/metrics', 10)

    def image_msg_to_cv2(self, msg: Image) -> np.ndarray:
        """Manually converts ROS Image to OpenCV format, bypassing cv_bridge bugs."""
        img = np.frombuffer(msg.data, dtype=np.uint8)
        img = img.reshape((msg.height, msg.width, 3))
        return img

    def sync_callback(self, image_msg: Image, detection_msg: Detection2DArray):
        if not detection_msg.detections:
            self.get_logger().warn(f"No detections in frame {image_msg.header.frame_id}. Skipping heuristics.")
            return

        # Extract the first detection (our target object)
        detection = detection_msg.detections[0]
        cx = detection.bbox.center.position.x
        cy = detection.bbox.center.position.y
        w = detection.bbox.size_x
        h = detection.bbox.size_y

        # Convert to image pixel coordinates and clamp to boundaries
        img_w, img_h = image_msg.width, image_msg.height
        x_min = max(0, int(cx - w / 2))
        y_min = max(0, int(cy - h / 2))
        x_max = min(img_w, int(cx + w / 2))
        y_max = min(img_h, int(cy + h / 2))

        # Guard against invalid bounding boxes
        if x_max <= x_min or y_max <= y_min:
            self.get_logger().error("Invalid bounding box dimensions. Skipping.")
            return

        cv_image = self.image_msg_to_cv2(image_msg)
        roi = cv_image[y_min:y_max, x_min:x_max]

        # 1. Calculate Coverage Area Ratio
        bbox_area = w * h
        total_area = img_w * img_h
        area_ratio = float(bbox_area / total_area)

        # 2. Calculate Illumination (Mean of HSV 'Value' channel on ROI)
        hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        illumination_score = float(hsv_roi[:, :, 2].mean())

        # 3. Calculate Sharpness (Variance of Laplacian on grayscale ROI)
        gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        sharpness_score = float(cv2.Laplacian(gray_roi, cv2.CV_64F).var())

        # Publish the results
        metrics_msg = HeuristicMetrics()
        metrics_msg.sharpness_score = sharpness_score
        metrics_msg.illumination_score = illumination_score
        metrics_msg.bbox_area_ratio = area_ratio

        self.metrics_pub.publish(metrics_msg)

        self.get_logger().info(
            f"[{image_msg.header.frame_id}] Scored -> "
            f"Sharpness: {sharpness_score:.1f}, Illumination: {illumination_score:.1f}, Coverage: {area_ratio:.2f}"
        )


def main(args=None):
    rclpy.init(args=args)
    node = HeuristicScorerNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
