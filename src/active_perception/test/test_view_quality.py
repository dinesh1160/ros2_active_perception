import cv2
import numpy as np
import pytest

from active_perception.view_quality import (
    TRUNCATED_SCORE, Thresholds, assess, clamp_bbox, exposure_score, framing_components,
    illumination, measure, sharpness)


def checkerboard(size=200, square=10):
    idx = (np.indices((size, size)) // square).sum(axis=0) % 2
    gray = (idx * 255).astype(np.uint8)
    return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)


def test_sharpness_drops_with_blur():
    img = checkerboard()
    scores = [sharpness(cv2.GaussianBlur(img, (0, 0), s)) if s else sharpness(img)
              for s in (0, 1, 2, 4)]
    assert scores == sorted(scores, reverse=True)
    assert scores[-1] < 0.05 * scores[0]


def test_sharpness_of_flat_image_is_zero():
    assert sharpness(np.full((50, 50, 3), 128, np.uint8)) == 0.0


@pytest.mark.parametrize('value', [0, 40, 128, 255])
def test_illumination_is_mean_hsv_value(value):
    assert illumination(np.full((20, 20, 3), value, np.uint8)) == pytest.approx(value)


def test_illumination_uses_brightest_channel():
    img = np.zeros((10, 10, 3), np.uint8)
    img[..., 2] = 200
    assert illumination(img) == pytest.approx(200)


def test_exposure_score_is_two_sided():
    th = Thresholds(min_illumination=30, max_illumination=235)
    assert exposure_score(30, th) == pytest.approx(0.5)
    assert exposure_score(235, th) == pytest.approx(0.5)
    assert exposure_score(10, th) < 0.5
    assert exposure_score(250, th) < 0.5
    assert exposure_score(128, th) == 1.0


def test_clamp_bbox():
    assert clamp_bbox((-5, -5, 50, 60), 40, 40) == (0, 0, 40, 40)
    assert clamp_bbox((10, 10, 10, 20), 40, 40) is None
    assert clamp_bbox((50, 0, 60, 10), 40, 40) is None


def test_framing_centred_box_passes():
    scores, raw = framing_components((130, 80, 190, 160), 320, 240, Thresholds())
    assert min(scores.values()) >= 0.5
    assert raw['center_offset_x'] == pytest.approx(0.0)
    assert raw['touches'] == ''


def test_framing_too_small():
    scores, raw = framing_components((158, 118, 162, 122), 320, 240, Thresholds())
    assert raw['coverage'] < Thresholds().min_coverage
    assert min(scores, key=scores.get) == 'too_small'


def test_framing_too_big_by_area():
    scores, _ = framing_components((10, 10, 310, 230), 320, 240, Thresholds())
    assert min(scores, key=scores.get) == 'too_big'


def test_framing_cut_off_at_top_is_too_big():
    scores, raw = framing_components((140, 0, 180, 100), 320, 240, Thresholds())
    assert raw['touches'] == 'T'
    assert scores['too_big'] == TRUNCATED_SCORE
    assert min(scores, key=scores.get) == 'too_big'


def test_framing_cut_off_on_one_side_is_off_center():
    scores, raw = framing_components((290, 100, 320, 140), 320, 240, Thresholds())
    assert raw['touches'] == 'R'
    assert raw['center_offset_x'] > 0
    assert min(scores, key=scores.get) == 'off_center'


def test_framing_off_center_threshold():
    th = Thresholds(max_center_offset=0.2)
    cx = 0.7 * 320
    scores, raw = framing_components((cx - 10, 100, cx + 10, 140), 320, 240, th)
    assert raw['center_offset_x'] == pytest.approx(0.2)
    assert scores['off_center'] == pytest.approx(0.5)


def test_assess_good_view_passes():
    a = assess(200.0, 120.0, 0.8, (130, 60, 190, 200), 320, 240)
    assert a.passed
    assert a.failed == []
    assert set(a.scores) == {'sharpness', 'exposure', 'visibility', 'framing'}
    assert all(0.0 <= s <= 1.0 for s in a.scores.values())


def test_assess_picks_weakest_failing_factor():
    a = assess(40.0, 6.0, 0.8, (130, 60, 190, 200), 320, 240)
    assert set(a.failed) == {'sharpness', 'exposure'}
    assert a.weakest == 'exposure'


def test_assess_low_confidence_fails_visibility():
    a = assess(200.0, 120.0, 0.3, (130, 60, 190, 200), 320, 240)
    assert a.failed == ['visibility']
    assert a.scores['visibility'] == pytest.approx(0.3)


def test_assess_score_is_half_at_each_threshold():
    th = Thresholds()
    a = assess(th.min_sharpness, th.min_illumination, th.min_confidence, (130, 60, 190, 200),
               320, 240, th)
    for factor in ('sharpness', 'exposure', 'visibility'):
        assert a.scores[factor] == pytest.approx(0.5)


def test_measure_on_image():
    img = checkerboard(240)[:, :, :]
    a = measure(img, (60, 60, 180, 180), 0.9)
    assert a.raw['sharpness'] > 1000
    assert a.raw['illumination'] == pytest.approx(127.5, abs=1)
    assert a.passed


def test_measure_empty_box_returns_none():
    assert measure(checkerboard(), (300, 300, 400, 400), 0.9) is None


def test_to_dict_is_json_friendly():
    import json
    a = assess(200.0, 120.0, 0.8, (130, 60, 190, 200), 320, 240)
    json.dumps(a.to_dict())
