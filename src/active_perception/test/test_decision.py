import pytest

from active_perception.decision import (
    DecisionParams, Episode, Move, decide_local, decide_vlm, view_rank)
from active_perception.view_quality import assess

GOOD_BOX = (130, 60, 190, 200)


def view(sharp=200.0, illum=120.0, conf=0.8, box=GOOD_BOX):
    return assess(sharp, illum, conf, box, 320, 240)


P = DecisionParams()


def test_local_pass_gives_no_move():
    assert decide_local(view(), 0.8, P) is None


@pytest.mark.parametrize('kwargs, factor, action', [
    ({'sharp': 10.0}, 'sharpness', 'retake'),
    ({'illum': 5.0}, 'exposure', 'orbit'),
    ({'illum': 252.0}, 'exposure', 'orbit'),
    ({'conf': 0.2}, 'visibility', 'orbit'),
    ({'box': (158, 118, 162, 122)}, 'framing', 'approach'),
    ({'box': (140, 0, 180, 240)}, 'framing', 'back_off'),
    ({'box': (270, 80, 310, 160)}, 'framing', 'rotate'),
])
def test_single_failure_maps_to_its_move(kwargs, factor, action):
    move = decide_local(view(**kwargs), 0.8, P)
    assert move.factor == factor
    assert move.action == action


def test_weakest_of_several_failures_wins():
    move = decide_local(view(sharp=40.0, illum=6.0), 0.8, P)
    assert move.factor == 'exposure'
    assert 'sharpness' in move.reason and 'exposure' in move.reason


def test_exposure_reason_says_dark_or_bright():
    assert 'too dark' in decide_local(view(illum=5.0), 0.8, P).reason
    assert 'too bright' in decide_local(view(illum=252.0), 0.8, P).reason


def test_rotate_turns_towards_the_target():
    right = decide_local(view(box=(270, 80, 310, 160)), 0.8, P)
    left = decide_local(view(box=(10, 80, 50, 160)), 0.8, P)
    assert right.value < 0
    assert left.value > 0
    assert right.value == pytest.approx(-0.40625 * P.camera_hfov_deg)


def test_orbit_uses_current_range():
    move = decide_local(view(conf=0.2), 1.1, P)
    assert move.action == 'orbit'
    assert move.value == P.orbit_step_deg
    assert move.radius == 1.1


def test_approach_is_limited_by_min_range():
    tiny = view(box=(158, 118, 162, 122))
    assert decide_local(tiny, 0.8, P).value == pytest.approx(P.translate_step_m)
    assert decide_local(tiny, 0.4, P).value == pytest.approx(0.1)
    assert decide_local(tiny, 0.31, P).action == 'stop'


def test_vlm_pass_accepts():
    assert decide_vlm(90, 85, view(), 0.8, P) is None
    assert decide_vlm(P.vlm_min_occlusion, P.vlm_min_framing, view(), 0.8, P) is None


def test_vlm_occlusion_orbits():
    move = decide_vlm(30, 90, view(), 0.8, P)
    assert (move.factor, move.action) == ('occlusion', 'orbit')


def test_vlm_weakest_of_two_failures():
    move = decide_vlm(50, 20, view(), 0.8, P)
    assert move.factor == 'framing'


def test_vlm_framing_uses_local_framing_direction():
    cx = 0.65 * 320
    move = decide_vlm(90, 30, view(box=(cx - 20, 60, cx + 20, 200)), 0.8, P)
    assert move.action == 'rotate'
    assert move.value < 0


def test_inverse_moves():
    assert Move('orbit', 30, 0.8).inverse().value == -30
    assert Move('orbit', 30, 0.8).inverse().radius == 0.8
    assert Move('rotate', -12).inverse().value == 12
    assert Move('approach', 0.15).inverse().action == 'back_off'
    assert Move('back_off', 0.15).inverse().action == 'approach'
    assert Move('retake').inverse() is None


def test_episode_tracks_range():
    ep = Episode(P, 0.8)
    ep.record_move(Move('approach', 0.15))
    ep.record_move(Move('approach', 0.15))
    ep.record_move(Move('back_off', 0.1))
    assert ep.range_m == pytest.approx(0.6)


def test_attempt_limit():
    ep = Episode(DecisionParams(max_attempts=3), 0.8)
    for i in range(3):
        assert not ep.exhausted
        ep.record_view(f"v{i}", (1, 0.1))
    assert ep.exhausted


def test_view_rank_order():
    scored_low = view_rank('scored', 10.0)
    local_fail = view_rank('rejected', assessment=view(sharp=10.0))
    no_target = view_rank('no_target')
    assert scored_low > local_fail > no_target


def test_best_view_prefers_rank_then_earliest():
    ep = Episode(P, 0.8)
    ep.record_view('a', (1, 0.3))
    ep.record_view('b', (2, 70.0))
    ep.record_view('c', (2, 70.0))
    ep.record_view('d', (1, 0.45))
    assert ep.best_view().name == 'b'


def test_retrace_undoes_moves_after_best_in_reverse():
    ep = Episode(P, 0.8)
    ep.record_view('v1', (1, 0.2))
    ep.record_move(Move('orbit', 30, 0.8))
    ep.record_view('v2', (2, 80.0))
    ep.record_move(Move('approach', 0.15))
    ep.record_view('v3', (1, 0.3))
    ep.record_move(Move('retake'))
    ep.record_view('v4', (1, 0.35))
    ep.record_move(Move('orbit', 30, 0.65))
    ep.record_view('v5', (2, 40.0))
    ep.record_move(Move('rotate', -10))
    ep.record_view('v6', (0, 0.0))

    best = ep.best_view()
    assert best.name == 'v2'
    path = ep.retrace_to(best)
    assert [(m.action, m.value) for m in path] == [
        ('rotate', 10), ('orbit', -30), ('back_off', 0.15)]
    assert path[1].radius == 0.65


def test_retrace_to_current_view_is_empty():
    ep = Episode(P, 0.8)
    ep.record_move(Move('orbit', 30, 0.8))
    ep.record_view('v1', (2, 90.0))
    assert ep.retrace_to(ep.best_view()) == []


def test_full_loop_simulation():
    ep = Episode(P, 0.8)
    snaps = [
        (view(sharp=20.0), None),
        (view(box=(250, 60, 310, 200)), None),
        (view(), (30, 90)),
        (view(), (85, 90)),
    ]
    actions = []
    for i, (a, vlm) in enumerate(snaps):
        move = decide_local(a, ep.range_m, P)
        if move is None:
            move = decide_vlm(*vlm, a, ep.range_m, P)
        status = 'scored' if vlm else 'rejected'
        ep.record_view(f"v{i}", view_rank(status, sum(vlm or (0,)) / 2, a))
        if move is None:
            break
        actions.append(move.action)
        ep.record_move(move)
    assert actions == ['retake', 'rotate', 'orbit']
    assert ep.attempts == 4
    assert ep.best_view().name == 'v3'
