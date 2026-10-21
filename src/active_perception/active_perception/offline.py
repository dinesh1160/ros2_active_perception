from active_perception.decision import DecisionParams, decide_local
from active_perception.view_quality import Thresholds, measure


class Detector:
    def __init__(self, model_path='yolov8n.pt', target_class='vase', conf=0.25):
        from ultralytics import YOLO

        self.model = YOLO(model_path)
        name_to_id = {name: idx for idx, name in self.model.names.items()}
        if target_class not in name_to_id:
            raise ValueError(f"target_class '{target_class}' not in model classes")
        self.class_id = name_to_id[target_class]
        self.conf = conf

    def __call__(self, bgr):
        boxes = self.model(bgr, classes=[self.class_id], conf=self.conf, verbose=False)[0].boxes
        if len(boxes) == 0:
            return None
        i = int(boxes.conf.argmax())
        return [float(v) for v in boxes.xyxy[i]], float(boxes.conf[i])


def lost(reason):
    return {'detected': False, 'passed': False,
            'move': {'action': 'stop', 'factor': 'detection', 'reason': reason}}


def evaluate_image(bgr, detector, th: Thresholds = None, p: DecisionParams = None, range_m=0.8):
    p = p or DecisionParams()
    det = detector(bgr)
    if det is None:
        return lost('target not detected')
    bbox, conf = det
    assessment = measure(bgr, bbox, conf, th)
    if assessment is None:
        return lost('empty bounding box')
    move = decide_local(assessment, range_m, p)
    return {
        'detected': True,
        'bbox': [round(v, 1) for v in bbox],
        'passed': assessment.passed,
        'weakest': assessment.weakest,
        'local': assessment.to_dict(),
        'move': None if move is None else move.to_dict(),
        '_assessment': assessment,
    }
