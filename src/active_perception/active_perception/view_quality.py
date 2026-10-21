from dataclasses import dataclass, field

import cv2
import numpy as np

FACTORS = ('sharpness', 'exposure', 'visibility', 'framing')
TRUNCATED_SCORE = 0.25


def sharpness(bgr_roi: np.ndarray) -> float:
    gray = cv2.cvtColor(bgr_roi, cv2.COLOR_BGR2GRAY)
    return float(cv2.Laplacian(gray, cv2.CV_64F).var())


def illumination(bgr_roi: np.ndarray) -> float:
    hsv = cv2.cvtColor(bgr_roi, cv2.COLOR_BGR2HSV)
    return float(hsv[:, :, 2].mean())


def clamp_bbox(bbox, img_w, img_h):
    x0, y0, x1, y1 = bbox
    x0, y0 = max(0, int(x0)), max(0, int(y0))
    x1, y1 = min(img_w, int(x1)), min(img_h, int(y1))
    if x1 <= x0 or y1 <= y0:
        return None
    return x0, y0, x1, y1


@dataclass
class Thresholds:
    min_sharpness: float = 50.0
    min_illumination: float = 30.0
    max_illumination: float = 235.0
    min_confidence: float = 0.5
    min_coverage: float = 0.03
    max_coverage: float = 0.5
    max_center_offset: float = 0.2
    edge_margin_px: int = 2


@dataclass
class Assessment:
    scores: dict
    raw: dict
    framing_issue: str
    framing_scores: dict = field(default_factory=dict)

    @property
    def failed(self):
        return [f for f in FACTORS if self.scores[f] < 0.5]

    @property
    def passed(self):
        return not self.failed

    @property
    def weakest(self):
        return min(FACTORS, key=lambda f: self.scores[f])

    def to_dict(self):
        return {
            'scores': {k: round(v, 3) for k, v in self.scores.items()},
            'raw': {k: round(v, 4) if isinstance(v, float) else v for k, v in self.raw.items()},
            'framing_issue': self.framing_issue,
            'failed': self.failed,
        }


def _ratio_score(value, threshold):
    # 0.5 at the threshold, capped to [0, 1]
    if threshold <= 0:
        return 1.0
    return float(min(1.0, max(0.0, 0.5 * value / threshold)))


def exposure_score(value, th: Thresholds):
    dark = _ratio_score(value, th.min_illumination)
    bright = _ratio_score(255.0 - value, 255.0 - th.max_illumination)
    return min(dark, bright)


def framing_components(bbox, img_w, img_h, th: Thresholds):
    x0, y0, x1, y1 = bbox
    coverage = (x1 - x0) * (y1 - y0) / float(img_w * img_h)
    dx = ((x0 + x1) / 2.0) / img_w - 0.5
    m = th.edge_margin_px
    left, right = x0 <= m, x1 >= img_w - m
    top, bottom = y0 <= m, y1 >= img_h - m

    off_center = 1.0 if dx == 0 else _ratio_score(th.max_center_offset, abs(dx))
    too_small = _ratio_score(coverage, th.min_coverage)
    too_big = _ratio_score(th.max_coverage, coverage)
    if top or bottom or (left and right):
        too_big = min(too_big, TRUNCATED_SCORE)
    elif left or right:
        off_center = min(off_center, TRUNCATED_SCORE)
        if dx == 0:
            dx = -1e-3 if left else 1e-3

    scores = {'off_center': off_center, 'too_small': too_small, 'too_big': too_big}
    raw = {'coverage': coverage, 'center_offset_x': dx,
           'touches': ''.join(s for s, t in zip('LRTB', (left, right, top, bottom)) if t)}
    return scores, raw


def assess(sharpness_value, illumination_value, confidence, bbox, img_w, img_h,
           th: Thresholds = None) -> Assessment:
    th = th or Thresholds()
    framing, raw = framing_components(bbox, img_w, img_h, th)
    issue = min(framing, key=framing.get)
    scores = {
        'sharpness': _ratio_score(sharpness_value, th.min_sharpness),
        'exposure': exposure_score(illumination_value, th),
        'visibility': _ratio_score(confidence, th.min_confidence),
        'framing': framing[issue],
    }
    raw.update(sharpness=float(sharpness_value), illumination=float(illumination_value),
               confidence=float(confidence))
    return Assessment(scores=scores, raw=raw, framing_issue=issue, framing_scores=framing)


def measure(bgr: np.ndarray, bbox, confidence, th: Thresholds = None):
    h, w = bgr.shape[:2]
    box = clamp_bbox(bbox, w, h)
    if box is None:
        return None
    roi = bgr[box[1]:box[3], box[0]:box[2]]
    return assess(sharpness(roi), illumination(roi), confidence, box, w, h, th)
