import argparse
import os
import sys

import cv2

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, 'src', 'active_perception'))

from active_perception.decision import DecisionParams, decide_vlm  # noqa: E402
from active_perception.offline import Detector, evaluate_image  # noqa: E402
from active_perception.vlm import GeminiJudge, load_env_file  # noqa: E402


def report(name, bgr, detector, judge, target, params):
    res = evaluate_image(bgr, detector, p=params)
    print(f"\n== {name}")
    if not res['detected']:
        print(f"   no '{target}' detected -> {res['move']['action']} (return to best view)")
        return
    raw, scores = res['local']['raw'], res['local']['scores']
    print(f"   sharpness {raw['sharpness']:.1f}  illumination {raw['illumination']:.1f}  "
          f"confidence {raw['confidence']:.2f}  coverage {raw['coverage'] * 100:.1f}%  "
          f"centre offset {raw['center_offset_x']:+.2f}  touches '{raw['touches']}'")
    print("   scores (pass >= 0.5): " + ", ".join(f"{k} {v:.2f}" for k, v in scores.items()))
    if not res['passed']:
        m = res['move']
        print(f"   LOCAL FAIL -> {m['action']} {m['value']:+.2f}: {m['reason']}")
        return
    if judge is None:
        print("   local check passed (the robot would now ask the VLM; run with --vlm)")
        return
    ok, jpeg = cv2.imencode('.jpg', bgr)
    occlusion, framing, reasoning = judge(jpeg.tobytes(), target)
    print(f"   VLM occlusion {occlusion:.0f}  framing {framing:.0f}: {reasoning}")
    move = decide_vlm(occlusion, framing, res['_assessment'], 0.8, params)
    print("   ACCEPT" if move is None else f"   VLM FAIL -> {move.action} {move.value:+.2f}: {move.reason}")


def main():
    ap = argparse.ArgumentParser(description='Score views without ROS or a robot')
    ap.add_argument('images', nargs='*')
    ap.add_argument('--target', default='vase', help='COCO class name (default: vase)')
    ap.add_argument('--model', default=os.path.join(REPO, 'yolov8n.pt'),
                    help='YOLO weights (downloaded by ultralytics if missing)')
    ap.add_argument('--webcam', type=int, default=None, help='camera index instead of images')
    ap.add_argument('--vlm', action='store_true', help='call Gemini when the local check passes')
    ap.add_argument('--gemini-model', default='gemini-3.6-flash')
    args = ap.parse_args()
    if not args.images and args.webcam is None:
        ap.error('give image paths or --webcam N')

    detector = Detector(args.model, args.target)
    params = DecisionParams()
    judge = None
    if args.vlm:
        load_env_file(os.path.join(REPO, '.env'))
        key = os.environ.get('GEMINI_API_KEY')
        if not key:
            sys.exit('GEMINI_API_KEY is not set (export it or put it in .env, see .env.example)')
        judge = GeminiJudge(key, args.gemini_model)

    for path in args.images:
        img = cv2.imread(path)
        if img is None:
            print(f"\n== {path}: cannot read")
            continue
        report(path, img, detector, judge, args.target, params)

    if args.webcam is not None:
        cap = cv2.VideoCapture(args.webcam)
        if not cap.isOpened():
            sys.exit(f"Cannot open webcam {args.webcam}")
        print("SPACE = score the current frame, q = quit")
        n = 0
        while True:
            ok, frame = cap.read()
            if not ok:
                break
            cv2.imshow('score_images (SPACE = score, q = quit)', frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            if key == ord(' '):
                n += 1
                report(f"webcam frame {n}", frame, detector, judge, args.target, params)
        cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
