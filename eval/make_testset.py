import json
import os
import sys

import cv2
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.join(HERE, 'base')
OUT_DIR = os.path.join(HERE, 'testset')

PERTURBATIONS = {
    'gaussian_blur': ([1, 2, 3, 5, 8], 'sharpness', 'retake'),          # sigma, px
    'motion_blur': ([5, 9, 15, 25, 41], 'sharpness', 'retake'),         # kernel length, px
    'underexpose': ([0.6, 0.4, 0.25, 0.15, 0.08], 'exposure', 'orbit'),  # intensity gain
    'overexpose': ([1.5, 2.0, 3.0, 4.0, 6.0], 'exposure', 'orbit'),      # intensity gain
    'zoom_out': ([0.7, 0.5, 0.35, 0.25, 0.15], 'framing', 'approach'),   # scale factor
    'zoom_in': ([1.5, 2.0, 3.0, 4.0], 'framing', 'back_off'),           # crop magnification
    'shift': ([0.15, 0.25, 0.35, 0.45], 'framing', 'rotate'),           # target centre offset / width
    'occlusion': ([0.2, 0.35, 0.5, 0.65, 0.8], 'visibility', 'orbit'),  # fraction of box width covered
}


def load_image(entry):
    path = entry['file']
    if path.startswith('ultralytics:'):
        import ultralytics
        path = os.path.join(os.path.dirname(ultralytics.__file__), 'assets', path.split(':', 1)[1])
    else:
        path = os.path.join(BASE_DIR, path)
    img = cv2.imread(path)
    if img is None:
        sys.exit(f"Cannot read {path}")
    if 'crop' in entry:
        x0, y0, x1, y1 = entry['crop']
        img = img[y0:y1, x0:x1].copy()
    return img


def gaussian_blur(img, box, sigma):
    return cv2.GaussianBlur(img, (0, 0), sigma), box


def motion_blur(img, box, length):
    kernel = np.zeros((length, length), np.float32)
    kernel[length // 2, :] = 1.0 / length
    return cv2.filter2D(img, -1, kernel), box


def gain(img, box, g):
    return np.clip(img.astype(np.float32) * g, 0, 255).astype(np.uint8), box


def zoom_out(img, box, s):
    h, w = img.shape[:2]
    small = cv2.resize(img, (max(1, int(w * s)), max(1, int(h * s))), interpolation=cv2.INTER_AREA)
    sh, sw = small.shape[:2]
    top, left = (h - sh) // 2, (w - sw) // 2
    out = cv2.copyMakeBorder(small, top, h - sh - top, left, w - sw - left, cv2.BORDER_REPLICATE)
    return out, [left + box[0] * s, top + box[1] * s, left + box[2] * s, top + box[3] * s]


def crop_resize(img, box, x0, y0, cw, ch):
    h, w = img.shape[:2]
    pad = max(w, h)
    padded = cv2.copyMakeBorder(img, pad, pad, pad, pad, cv2.BORDER_REPLICATE)
    win = padded[int(y0) + pad:int(y0 + ch) + pad, int(x0) + pad:int(x0 + cw) + pad]
    out = cv2.resize(win, (w, h), interpolation=cv2.INTER_LINEAR)
    sx, sy = w / cw, h / ch
    return out, [(box[0] - x0) * sx, (box[1] - y0) * sy, (box[2] - x0) * sx, (box[3] - y0) * sy]


def zoom_in(img, box, m):
    h, w = img.shape[:2]
    cx, cy = (box[0] + box[2]) / 2, (box[1] + box[3]) / 2
    cw, ch = w / m, h / m
    return crop_resize(img, box, cx - cw / 2, cy - ch / 2, cw, ch)


def shift(img, box, offset):
    h, w = img.shape[:2]
    cx = (box[0] + box[2]) / 2
    return crop_resize(img, box, cx - (0.5 + offset) * w, 0, w, h)


def occlusion(img, box, frac):
    out = img.copy()
    x0, y0, x1, y1 = (int(round(v)) for v in box)
    xe = x0 + int(round((x1 - x0) * frac))
    rng = np.random.default_rng(0)
    board = np.full((y1 - y0, xe - x0, 3), (60, 90, 130), np.float32)
    board += rng.normal(0, 8, board.shape)
    out[y0:y1, x0:xe] = np.clip(board, 0, 255).astype(np.uint8)
    return out, box


FUNCS = {'gaussian_blur': gaussian_blur, 'motion_blur': motion_blur, 'underexpose': gain,
         'overexpose': gain, 'zoom_out': zoom_out, 'zoom_in': zoom_in, 'shift': shift,
         'occlusion': occlusion}


def clamp(box, w, h):
    return [round(max(0.0, min(w, box[0])), 1), round(max(0.0, min(h, box[1])), 1),
            round(max(0.0, min(w, box[2])), 1), round(max(0.0, min(h, box[3])), 1)]


def main():
    with open(os.path.join(BASE_DIR, 'bases.json')) as f:
        spec = json.load(f)
    os.makedirs(OUT_DIR, exist_ok=True)
    cases = []

    def save(name, img, **info):
        cv2.imwrite(os.path.join(OUT_DIR, f"{name}.jpg"), img, [cv2.IMWRITE_JPEG_QUALITY, 95])
        cases.append({'name': name, 'image': f"{name}.jpg", **info})

    for base in spec['bases']:
        img = load_image(base)
        h, w = img.shape[:2]
        save(f"{base['name']}__clean", img, base=base['name'], target=base['target'],
             perturbation='clean', level=None, gt_bbox=base['bbox'],
             expected_factor=None, expected_move=None)
        for pert, (levels, factor, move) in PERTURBATIONS.items():
            for level in levels:
                out, box = FUNCS[pert](img, base['bbox'], level)
                save(f"{base['name']}__{pert}_{level}", out, base=base['name'], target=base['target'],
                     perturbation=pert, level=level, gt_bbox=clamp(box, w, h),
                     expected_factor=factor, expected_move=move)

    for nat in spec['natural']:
        img = load_image(nat)
        save(f"natural__{nat['name']}", img, base=nat['name'], target=nat['target'],
             perturbation='natural', level=None, gt_bbox=None,
             expected_factor=nat['expected_factor'], expected_move=nat['expected_move'],
             note=nat['note'])

    with open(os.path.join(OUT_DIR, 'manifest.json'), 'w') as f:
        json.dump({'perturbations': {k: {'levels': v[0], 'expected_factor': v[1],
                                         'expected_move': v[2]} for k, v in PERTURBATIONS.items()},
                   'cases': cases}, f, indent=1)
    print(f"Wrote {len(cases)} images to {OUT_DIR}")


if __name__ == '__main__':
    main()
