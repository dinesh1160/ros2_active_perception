import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from sensor_msgs.msg import Image
from vision_msgs.msg import Detection2DArray
import message_filters

from active_perception_interfaces.msg import HeuristicMetrics
from active_perception.image_utils import image_msg_to_bgr
from active_perception.view_quality import illumination, sharpness


class HeuristicScorerNode(Node):
    def __init__(self):
        super().__init__('heuristic_scorer_node')

        # Synchronize the SNAPSHOT image and bounding box topics.
        # YOLO copies the image header, so the stamps match exactly.
        self.image_sub = message_filters.Subscriber(self, Image, '/snapshot/image')
        self.bbox_sub = message_filters.Subscriber(self, Detection2DArray, '/snapshot/bounding_boxes')
        self.ts = message_filters.TimeSynchronizer([self.image_sub, self.bbox_sub], queue_size=10)
        self.ts.registerCallback(self.sync_callback)

        # Publish to the snapshot metrics topic
        self.metrics_pub = self.create_publisher(HeuristicMetrics, '/snapshot/metrics', 10)

        self.get_logger().info("Heuristic Scorer ready. Waiting for snapshots...")

    def publish_no_target(self, image_msg: Image, reason: str):
        """Always report back so the coordinator never waits forever."""
        self.get_logger().warn(f"{reason} Skipping heuristics.")
        metrics_msg = HeuristicMetrics()
        metrics_msg.header = image_msg.header
        metrics_msg.target_detected = False
        self.metrics_pub.publish(metrics_msg)

    def sync_callback(self, image_msg: Image, detection_msg: Detection2DArray):
        if not detection_msg.detections:
            self.publish_no_target(image_msg, "No target detected in snapshot.")
            return

        # Highest-confidence detection is our target object
        detection = max(
            detection_msg.detections,
            key=lambda d: d.results[0].hypothesis.score if d.results else 0.0)
        confidence = detection.results[0].hypothesis.score if detection.results else 0.0
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
            self.publish_no_target(image_msg, "Invalid bounding box dimensions.")
            return

        try:
            cv_image = image_msg_to_bgr(image_msg)
        except ValueError as e:
            self.publish_no_target(image_msg, f"Cannot convert snapshot: {e}.")
            return
        roi = cv_image[y_min:y_max, x_min:x_max]

        # 1. Calculate Coverage Area Ratio (of the visible, clamped box)
        area_ratio = float((x_max - x_min) * (y_max - y_min) / (img_w * img_h))

        # 2. Calculate Illumination (Mean of HSV 'Value' channel on ROI)
        illumination_score = illumination(roi)

        # 3. Calculate Sharpness (Variance of Laplacian on grayscale ROI)
        sharpness_score = sharpness(roi)

        # Publish the results
        metrics_msg = HeuristicMetrics()
        metrics_msg.header = image_msg.header
        metrics_msg.target_detected = True
        metrics_msg.sharpness_score = sharpness_score
        metrics_msg.illumination_score = illumination_score
        metrics_msg.bbox_area_ratio = area_ratio
        metrics_msg.detection_confidence = float(confidence)
        metrics_msg.bbox_x_min = float(x_min)
        metrics_msg.bbox_y_min = float(y_min)
        metrics_msg.bbox_x_max = float(x_max)
        metrics_msg.bbox_y_max = float(y_max)

        self.metrics_pub.publish(metrics_msg)

        self.get_logger().info(
            f"Scored -> Sharpness: {sharpness_score:.1f}, "
            f"Illumination: {illumination_score:.1f}, Coverage: {area_ratio:.2f}"
        )


def main(args=None):
    rclpy.init(args=args)
    node = HeuristicScorerNode()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
