import hashlib
import json
import math
import os
import shutil
import textwrap
from datetime import datetime

import cv2
import numpy as np

import rclpy
from rclpy.duration import Duration
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from rcl_interfaces.msg import ParameterDescriptor
from rclpy.time import Time
from nav_msgs.msg import Odometry
from sensor_msgs.msg import CompressedImage, Image
from std_srvs.srv import Trigger
from active_perception_interfaces.msg import HeuristicMetrics
from active_perception_interfaces.srv import AnalyzeQuality
from active_perception.image_utils import image_msg_to_bgr


class CoordinatorNode(Node):
    def __init__(self):
        super().__init__('coordinator_node')

        defaults = {}

        def p(name, default):
            # Dynamic typing so whole-number launch values (e.g. ':=0') work for float parameters
            defaults[name] = default
            self.declare_parameter(name, default, ParameterDescriptor(dynamic_typing=True))

        def g(name):
            value = self.get_parameter(name).value
            return float(value) if isinstance(defaults[name], float) else value
        p('camera_topic', '/pi_camera/image_raw/compressed')  # '/compressed' -> CompressedImage
        p('odom_topic', '/odometry/filtered')
        p('target_object', 'vase')
        p('min_sharpness', 50.0)
        p('min_illumination', 30.0)
        p('max_frame_age_sec', 2.0)
        p('metrics_timeout_sec', 15.0)
        p('vlm_timeout_sec', 30.0)
        p('enable_motion', True)        # move to the next orbit view before every snap but the first
        p('settle_sec', 1.0)            # wait after the robot stops before snapping
        p('motion_timeout_sec', 90.0)
        p('frame_wait_timeout_sec', 5.0)
        p('runs_dir', 'runs')
        p('weight_occlusion', 0.4)
        p('weight_framing', 0.4)
        p('weight_coverage', 0.2)
        p('coverage_full_ratio', 0.25)  # bbox covering this fraction of the frame = full marks

        camera_topic = g('camera_topic')
        self.target_object = g('target_object')
        self.MIN_SHARPNESS = g('min_sharpness')
        self.MIN_ILLUMINATION = g('min_illumination')
        self.max_frame_age = g('max_frame_age_sec')
        self.metrics_timeout = g('metrics_timeout_sec')
        self.vlm_timeout = g('vlm_timeout_sec')
        self.enable_motion = g('enable_motion')
        self.settle_sec = g('settle_sec')
        self.motion_timeout = g('motion_timeout_sec')
        self.frame_wait_timeout = g('frame_wait_timeout_sec')
        self.runs_dir = os.path.abspath(g('runs_dir'))
        self.weights = {
            'occlusion': g('weight_occlusion'),
            'framing': g('weight_framing'),
            'coverage': g('weight_coverage'),
        }
        self.coverage_full_ratio = g('coverage_full_ratio')

        self.state = 'IDLE'
        self.history = []
        self.eval_counter = 0
        self.latest_frame = None        # raw Image or CompressedImage message
        self.latest_frame_time = None   # local receive time
        self.latest_pose = None         # (x, y, yaw)
        self.run_dir = None             # created on the first snapshot
        # The frozen frame being evaluated (YOLO, heuristics, VLM and the saved file all use this one)
        self.snapshot_image = None
        self.snapshot_bgr = None
        self.current_eval = None
        self.deadline = None
        self.settle_until = None

        # 1. Listen to the continuous camera stream quietly in the background.
        #    Sensor-data QoS (best effort) works with both reliable and best-effort publishers.
        self.compressed = camera_topic.endswith('/compressed')
        msg_type = CompressedImage if self.compressed else Image
        self.create_subscription(msg_type, camera_topic, self.image_callback, qos_profile_sensor_data)
        self.create_subscription(Odometry, g('odom_topic'), self.odom_callback, qos_profile_sensor_data)

        # 2. The Gatekeeper: Publishes ONE frame only when triggered
        self.snapshot_pub = self.create_publisher(Image, '/snapshot/image', 10)

        # 3. Listen for the processed metrics returning from the snapshot pipeline
        self.create_subscription(HeuristicMetrics, '/snapshot/metrics', self.metrics_callback, 10)

        # Services
        self.vlm_client = self.create_client(AnalyzeQuality, '/analyze_view_quality')
        self.motion_client = self.create_client(Trigger, '/move_to_next_view')
        self.create_service(Trigger, '/evaluate_now', self.handle_evaluate_now)
        self.create_service(Trigger, '/finish_benchmark', self.handle_finish)

        # Drives settling and makes sure a lost message or hung call can never wedge the state machine
        self.create_timer(0.1, self.tick)

        self.get_logger().info(
            f"Coordinator ready. Camera: '{camera_topic}', target: '{self.target_object}', "
            f"motion: {'on' if self.enable_motion else 'off'}. "
            "Press ENTER in the trigger terminal to snap a frame.")

    # ---------------- inputs ----------------
    def image_callback(self, msg):
        if self.latest_frame is None:
            desc = msg.format if self.compressed else f"{msg.width}x{msg.height} {msg.encoding}"
            self.get_logger().info(f"Camera feed received: {desc}")
        self.latest_frame = msg
        self.latest_frame_time = self.get_clock().now()

    def odom_callback(self, msg: Odometry):
        p = msg.pose.pose
        q = p.orientation
        yaw = math.atan2(2.0 * (q.w * q.z + q.x * q.y), 1.0 - 2.0 * (q.y * q.y + q.z * q.z))
        self.latest_pose = (p.position.x, p.position.y, yaw)

    # ---------------- trigger ----------------
    def handle_evaluate_now(self, request, response):
        if self.state != 'IDLE':
            response.success = False
            response.message = f"Busy ({self.state})."
            return response

        if self.latest_frame is None:
            response.success = False
            response.message = "No camera feed detected."
            self.get_logger().error(response.message)
            return response

        # First view is taken where the robot stands; every later one moves first
        if self.enable_motion and self.eval_counter > 0:
            if not self.motion_client.service_is_ready():
                response.success = False
                response.message = "Motion node not available (/move_to_next_view)."
                self.get_logger().error(response.message)
                return response
            self.state = 'MOVING'
            self.deadline = self.get_clock().now().nanoseconds + int(self.motion_timeout * 1e9)
            self.get_logger().info("\n🚗 Moving to the next view...")
            future = self.motion_client.call_async(Trigger.Request())
            future.add_done_callback(self.motion_done_callback)
            response.success = True
            response.message = "Moving to the next view, snapshot follows."
            return response

        age = (self.get_clock().now() - self.latest_frame_time).nanoseconds / 1e9
        if age > self.max_frame_age:
            response.success = False
            response.message = f"Camera feed is stale (last frame {age:.1f}s ago)."
            self.get_logger().error(response.message)
            return response

        ok, message = self.take_snapshot()
        response.success = ok
        response.message = message
        return response

    def motion_done_callback(self, future):
        if self.state != 'MOVING':
            return  # the watchdog already gave up on this move
        try:
            res = future.result()
        except Exception as e:
            res = Trigger.Response(success=False, message=str(e))
        if not res.success:
            self.get_logger().error(
                f"Move failed: {res.message}. The robot may be off the orbit: re-place it facing the "
                f"{self.target_object} about orbit_radius away, then press ENTER for the next move.")
            self.state = 'IDLE'
            self.deadline = None
            return
        self.get_logger().info(f"Move done ({res.message}). Settling {self.settle_sec:.1f}s...")
        self.state = 'SETTLING'
        self.deadline = None
        self.settle_until = self.get_clock().now() + Duration(seconds=self.settle_sec)

    # ---------------- snapshot ----------------
    def ensure_run_dir(self):
        if self.run_dir is None:
            stamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.run_dir = os.path.join(self.runs_dir, f"run_{stamp}")
            os.makedirs(self.run_dir, exist_ok=True)
            self.get_logger().info(f"Saving this run to {self.run_dir}")
        return self.run_dir

    def take_snapshot(self):
        """Freeze the latest frame, save it and send it into the pipeline."""
        src = self.latest_frame
        try:
            if self.compressed:
                jpeg_bytes = bytes(src.data)
                bgr = cv2.imdecode(np.frombuffer(jpeg_bytes, np.uint8), cv2.IMREAD_COLOR)
                if bgr is None:
                    raise ValueError(f"cannot decode compressed frame (format '{src.format}')")
            else:
                bgr = image_msg_to_bgr(src)
                jpeg_bytes = cv2.imencode('.jpg', bgr, [cv2.IMWRITE_JPEG_QUALITY, 95])[1].tobytes()
        except ValueError as e:
            self.get_logger().error(f"Snapshot failed: {e}")
            self.state = 'IDLE'
            return False, f"Snapshot failed: {e}"

        now = self.get_clock().now()
        snapshot = Image()
        snapshot.header.frame_id = src.header.frame_id
        snapshot.header.stamp = now.to_msg()  # unique stamp so results can be matched to it
        snapshot.height, snapshot.width = bgr.shape[:2]
        snapshot.encoding = 'bgr8'
        snapshot.step = snapshot.width * 3
        pixels = bgr.tobytes()
        snapshot.data = pixels

        self.eval_counter += 1
        frame = f"Angle_{self.eval_counter}"
        image_name = f"{frame}.jpg"
        with open(os.path.join(self.ensure_run_dir(), image_name), 'wb') as f:
            f.write(jpeg_bytes)  # the exact frame that is scored (original JPEG from the robot)

        pose = self.latest_pose
        self.current_eval = {
            'frame': frame,
            'status': 'pending',
            'reason': '',
            'sharpness': 0.0,
            'illumination': 0.0,
            'coverage_ratio': 0.0,
            'coverage_score': 0.0,
            'vlm_occlusion': 0.0,
            'vlm_framing': 0.0,
            'total_score': 0.0,
            'bbox': None,
            'pose': None if pose is None else {
                'x': round(pose[0], 3), 'y': round(pose[1], 3),
                'yaw_deg': round(math.degrees(pose[2]), 1)},
            'frame_hash': hashlib.md5(pixels).hexdigest()[:12],  # VLM bridge logs the same hash
            'image': image_name,
            'annotated_image': f"{frame}_annotated.jpg",
            'time': datetime.now().isoformat(timespec='seconds'),
        }
        self.snapshot_image = snapshot
        self.snapshot_bgr = bgr
        self.state = 'WAITING_FOR_METRICS'
        self.deadline = now.nanoseconds + int(self.metrics_timeout * 1e9)

        self.get_logger().info(
            f"\n📸 SNAPSHOT {frame} (frame hash {self.current_eval['frame_hash']}): "
            "Sent to YOLO and Heuristics...")

        # Publish the single frame to wake up the rest of the pipeline
        self.snapshot_pub.publish(snapshot)
        return True, f"{frame} captured."

    # ---------------- pipeline results ----------------
    def metrics_callback(self, msg: HeuristicMetrics):
        # Only process metrics for the snapshot we are waiting on (ignore late/stale ones)
        if self.state != 'WAITING_FOR_METRICS':
            return
        if Time.from_msg(msg.header.stamp) != Time.from_msg(self.snapshot_image.header.stamp):
            self.get_logger().warn("Ignoring metrics from an older snapshot.")
            return

        if not msg.target_detected:
            self.get_logger().warn(f"Discarded: no '{self.target_object}' detected.")
            self.finish_eval('no_target', f"No {self.target_object} detected")
            return

        ev = self.current_eval
        ev['sharpness'] = msg.sharpness_score
        ev['illumination'] = msg.illumination_score
        ev['coverage_ratio'] = msg.bbox_area_ratio
        ev['coverage_score'] = min(msg.bbox_area_ratio / self.coverage_full_ratio, 1.0) * 100.0
        ev['bbox'] = [int(msg.bbox_x_min), int(msg.bbox_y_min), int(msg.bbox_x_max), int(msg.bbox_y_max)]

        self.get_logger().info(
            f"Heuristics -> Sharpness: {msg.sharpness_score:.1f}, "
            f"Illum: {msg.illumination_score:.1f}, Coverage: {msg.bbox_area_ratio * 100:.1f}%")

        # 1. Fast Heuristics Check
        if msg.sharpness_score < self.MIN_SHARPNESS or msg.illumination_score < self.MIN_ILLUMINATION:
            reason = "Failed Heuristics (Blurry or Dark)"
            self.get_logger().warn(f"Discarded: {reason}")
            self.finish_eval('rejected', reason)
            return

        # 2. VLM Check (Async) - non-blocking readiness check inside the callback
        if not self.vlm_client.service_is_ready():
            self.get_logger().error("VLM offline.")
            self.finish_eval('vlm_error', "VLM service offline")
            return

        self.get_logger().info("Heuristics passed! Querying VLM...")
        self.state = 'PROCESSING_VLM'
        self.deadline = self.get_clock().now().nanoseconds + int(self.vlm_timeout * 1e9)

        req = AnalyzeQuality.Request()
        req.image = self.snapshot_image  # the same frozen frame YOLO and the heuristics scored
        req.target_object = self.target_object
        future = self.vlm_client.call_async(req)
        eval_ref = self.current_eval
        future.add_done_callback(lambda fut: self.vlm_response_callback(fut, eval_ref))

    def vlm_response_callback(self, future, eval_ref):
        # The watchdog may have already given up on this evaluation
        if self.state != 'PROCESSING_VLM' or eval_ref is not self.current_eval:
            self.get_logger().warn(f"Late VLM response for {eval_ref['frame']} ignored.")
            return

        try:
            res = future.result()
        except Exception as e:
            self.get_logger().error(f"VLM Call Failed: {e}")
            self.finish_eval('vlm_error', f"VLM call failed: {e}")
            return

        if not res.success:
            self.get_logger().error(f"VLM returned an error: {res.reasoning}")
            self.finish_eval('vlm_error', res.reasoning)
            return

        ev = self.current_eval
        ev['vlm_occlusion'] = res.occlusion_score
        ev['vlm_framing'] = res.framing_score
        w = self.weights
        ev['total_score'] = (w['occlusion'] * res.occlusion_score
                             + w['framing'] * res.framing_score
                             + w['coverage'] * ev['coverage_score'])
        self.get_logger().info(
            f"VLM Score -> Occ: {res.occlusion_score:.0f}, Frame: {res.framing_score:.0f}, "
            f"Coverage: {ev['coverage_score']:.0f} => Total {ev['total_score']:.1f} ({res.reasoning})")
        self.finish_eval('scored', res.reasoning)

    def tick(self):
        now = self.get_clock().now()

        # After a move: snap the first frame that arrived after the settle time
        if self.state == 'SETTLING':
            if now >= self.settle_until and self.latest_frame_time >= self.settle_until:
                self.take_snapshot()
            elif (now - self.settle_until).nanoseconds / 1e9 > self.frame_wait_timeout:
                self.get_logger().error("No camera frame arrived after the move. Resetting to IDLE.")
                self.state = 'IDLE'
            return

        if self.deadline is None or now.nanoseconds < self.deadline:
            return
        if self.state == 'MOVING':
            self.get_logger().error("Timed out waiting for the move to finish. Resetting to IDLE.")
            self.state = 'IDLE'
            self.deadline = None
            return
        stage = 'heuristic metrics' if self.state == 'WAITING_FOR_METRICS' else 'VLM response'
        self.get_logger().error(
            f"Timed out waiting for {stage} on {self.current_eval['frame']}. "
            "Is every node running? Resetting to IDLE.")
        self.finish_eval('timeout', f"Timed out waiting for {stage}")

    def finish_eval(self, status, reason):
        """Record the current evaluation, save its files and return to IDLE."""
        ev = self.current_eval
        ev['status'] = status
        ev['reason'] = reason
        self.history.append(ev)
        try:
            cv2.imwrite(os.path.join(self.run_dir, ev['annotated_image']),
                        self.annotate(self.snapshot_bgr, ev))
            self.write_results()
        except Exception as e:
            self.get_logger().error(f"Could not save results for {ev['frame']}: {e}")
        self.current_eval = None
        self.snapshot_image = None
        self.snapshot_bgr = None
        self.deadline = None
        self.state = 'IDLE'
        self.get_logger().info(f"✅ {ev['frame']} done ({status}). Ready for next angle.")

    # ---------------- output files ----------------
    def annotate(self, bgr, ev):
        img = bgr.copy()
        h, w = img.shape[:2]
        scale = max(0.5, w / 1600.0)
        thick = max(1, int(round(scale * 2)))
        scored = ev['status'] == 'scored'
        colour = (0, 200, 0) if scored else (0, 0, 255)

        if ev['bbox']:
            x0, y0, x1, y1 = ev['bbox']
            cv2.rectangle(img, (x0, y0), (x1, y1), colour, thick + 1)
            cv2.putText(img, self.target_object, (x0, max(0, y0 - 8)),
                        cv2.FONT_HERSHEY_SIMPLEX, scale, colour, thick)

        lines = [f"{ev['frame']}  {ev['status'].upper()}" + (f"  TOTAL {ev['total_score']:.1f}" if scored else "")]
        if ev['bbox']:
            lines.append(f"Occlusion {ev['vlm_occlusion']:.0f}  Framing {ev['vlm_framing']:.0f}  "
                         f"Coverage {ev['coverage_score']:.0f} ({ev['coverage_ratio'] * 100:.1f}% of frame)")
            lines.append(f"Sharpness {ev['sharpness']:.0f}  Illumination {ev['illumination']:.0f}")
        chars = max(30, int(w / (scale * 20)))
        lines += textwrap.wrap(ev['reason'], chars)

        line_h = int(32 * scale)
        band_h = line_h * len(lines) + int(14 * scale)
        overlay = img.copy()
        cv2.rectangle(overlay, (0, 0), (w, band_h), (0, 0, 0), -1)
        img = cv2.addWeighted(overlay, 0.6, img, 0.4, 0)
        for i, text in enumerate(lines):
            cv2.putText(img, text, (int(10 * scale), line_h * (i + 1)),
                        cv2.FONT_HERSHEY_SIMPLEX, scale * 0.8,
                        colour if i == 0 else (255, 255, 255), thick)
        return img

    def best_eval(self):
        scored = [item for item in self.history if item['status'] == 'scored']
        return max(scored, key=lambda item: item['total_score']) if scored else None

    def write_results(self):
        best = self.best_eval()
        data = {
            'target_object': self.target_object,
            'score_formula': (f"{self.weights['occlusion']}*occlusion + {self.weights['framing']}*framing + "
                              f"{self.weights['coverage']}*coverage_score, coverage_score = "
                              f"min(bbox_area_ratio / {self.coverage_full_ratio}, 1) * 100"),
            'thresholds': {'min_sharpness': self.MIN_SHARPNESS, 'min_illumination': self.MIN_ILLUMINATION},
            'best_view': best['frame'] if best else None,
            'angles': self.history,
        }
        with open(os.path.join(self.run_dir, 'results.json'), 'w') as f:
            json.dump(data, f, indent=2)

    def handle_finish(self, request, response):
        if not self.history:
            response.success = False
            response.message = "No angles evaluated yet."
            return response

        lines = [f"BENCHMARK COMPLETE - target: {self.target_object}", ""]
        for item in self.history:
            if item['status'] == 'scored':
                lines.append(
                    f"[{item['frame']}] Score: {item['total_score']:.1f} | "
                    f"VLM: [Occ:{item['vlm_occlusion']:.0f}, Frame:{item['vlm_framing']:.0f}] | "
                    f"Coverage: {item['coverage_score']:.0f} ({item['coverage_ratio'] * 100:.1f}%) | "
                    f"Heuristics: [Blur:{item['sharpness']:.1f}, Light:{item['illumination']:.1f}] "
                    f"-> {item['reason']}")
            else:
                lines.append(f"[{item['frame']}] {item['status'].upper()} -> {item['reason']}")

        # Only frames that passed every stage are eligible for best angle
        best = self.best_eval()
        lines.append("")
        if best:
            pose = best['pose']
            where = f" at x={pose['x']} y={pose['y']} yaw={pose['yaw_deg']} deg" if pose else ""
            lines.append(f"🏆 BEST ANGLE: {best['frame']} (Score: {best['total_score']:.1f}){where}")
            shutil.copy(os.path.join(self.run_dir, best['image']),
                        os.path.join(self.run_dir, 'best_view.jpg'))
            shutil.copy(os.path.join(self.run_dir, best['annotated_image']),
                        os.path.join(self.run_dir, 'best_view_annotated.jpg'))
            response.message = f"Best angle: {best['frame']} (Score: {best['total_score']:.1f})."
        else:
            lines.append("No angle passed all checks.")
            response.message = "No angle passed all checks."
        lines.append(f"Results saved in {self.run_dir}")
        response.message += f" Results: {self.run_dir}"

        self.write_results()
        with open(os.path.join(self.run_dir, 'summary.txt'), 'w', encoding='utf-8') as f:
            f.write("\n".join(lines) + "\n")

        bar = "=" * 52
        self.get_logger().info(f"\n{bar}\n" + "\n".join(lines) + f"\n{bar}\n")
        response.success = True
        return response


def main(args=None):
    rclpy.init(args=args)
    node = CoordinatorNode()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
