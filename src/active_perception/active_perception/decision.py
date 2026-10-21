from dataclasses import dataclass, field, replace

FACTOR_MOVES = {
    'sharpness': 'retake',
    'exposure': 'orbit',
    'visibility': 'orbit',
    'occlusion': 'orbit',
}
FRAMING_MOVES = {'off_center': 'rotate', 'too_small': 'approach', 'too_big': 'back_off'}


@dataclass
class DecisionParams:
    orbit_step_deg: float = 30.0
    camera_hfov_deg: float = 62.2
    translate_step_m: float = 0.15
    min_range_m: float = 0.3
    max_attempts: int = 5
    vlm_min_occlusion: float = 60.0
    vlm_min_framing: float = 60.0


@dataclass
class Move:
    action: str
    value: float = 0.0  # degrees for orbit/rotate (+ = CCW), metres for approach/back_off
    radius: float = 0.0
    factor: str = ''
    reason: str = ''

    def inverse(self):
        if self.action in ('orbit', 'rotate'):
            return replace(self, value=-self.value, reason=f"undo {self.action}")
        if self.action in ('approach', 'back_off'):
            other = 'back_off' if self.action == 'approach' else 'approach'
            return replace(self, action=other, reason=f"undo {self.action}")
        return None

    def to_dict(self):
        return {'action': self.action, 'value': round(self.value, 3),
                'radius': round(self.radius, 3), 'factor': self.factor, 'reason': self.reason}


def move_for(factor, framing_issue, center_offset_x, range_m, p: DecisionParams, reason=''):
    if factor == 'framing':
        action = FRAMING_MOVES[framing_issue]
    else:
        action = FACTOR_MOVES[factor]

    if action == 'orbit':
        return Move('orbit', p.orbit_step_deg, range_m, factor, reason)
    if action == 'rotate':
        return Move('rotate', -center_offset_x * p.camera_hfov_deg, 0.0, factor, reason)
    if action == 'approach':
        step = min(p.translate_step_m, range_m - p.min_range_m)
        if step < 0.02:
            return Move('stop', 0.0, 0.0, factor, f"{reason}; already at the minimum range")
        return Move('approach', step, 0.0, factor, reason)
    if action == 'back_off':
        return Move('back_off', p.translate_step_m, 0.0, factor, reason)
    return Move(action, 0.0, 0.0, factor, reason)


def decide_local(assessment, range_m, p: DecisionParams):
    if assessment.passed:
        return None
    factor = assessment.weakest
    reason = (f"local check failed ({', '.join(assessment.failed)}); weakest: {factor} "
              f"{assessment.scores[factor]:.2f}")
    if factor == 'framing':
        reason += f" ({assessment.framing_issue})"
    if factor == 'exposure':
        reason += ' (too bright)' if assessment.raw['illumination'] > 127.5 else ' (too dark)'
    return move_for(factor, assessment.framing_issue, assessment.raw['center_offset_x'],
                    range_m, p, reason)


def decide_vlm(occlusion_score, framing_score, assessment, range_m, p: DecisionParams):
    scores = {'occlusion': 0.5 * occlusion_score / p.vlm_min_occlusion,
              'framing': 0.5 * framing_score / p.vlm_min_framing}
    failed = [f for f in ('occlusion', 'framing') if scores[f] < 0.5]
    if not failed:
        return None
    factor = min(failed, key=scores.get)
    reason = (f"VLM check failed ({', '.join(failed)}); weakest: {factor} "
              f"{occlusion_score if factor == 'occlusion' else framing_score:.0f}/100")
    if factor == 'framing':
        reason += f" ({assessment.framing_issue})"
    return move_for(factor, assessment.framing_issue, assessment.raw['center_offset_x'],
                    range_m, p, reason)


@dataclass
class View:
    name: str
    rank: tuple
    moves_before: int


def view_rank(status, total_score=0.0, assessment=None):
    if status == 'scored':
        return (2, total_score)
    if assessment is not None:
        return (1, min(assessment.scores.values()))
    return (0, 0.0)


@dataclass
class Episode:
    params: DecisionParams
    range_m: float
    views: list = field(default_factory=list)
    moves: list = field(default_factory=list)

    @property
    def attempts(self):
        return len(self.views)

    @property
    def exhausted(self):
        return self.attempts >= self.params.max_attempts

    def record_view(self, name, rank):
        self.views.append(View(name, rank, len(self.moves)))

    def record_move(self, move):
        self.moves.append(move)
        if move.action == 'approach':
            self.range_m -= move.value
        elif move.action == 'back_off':
            self.range_m += move.value

    def best_view(self):
        if not self.views:
            return None
        return max(self.views, key=lambda v: (v.rank, -self.views.index(v)))

    def retrace_to(self, view):
        undo = (m.inverse() for m in reversed(self.moves[view.moves_before:]))
        return [m for m in undo if m is not None]
