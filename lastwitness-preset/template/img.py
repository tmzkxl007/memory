# 마지막 목격자 — 장면 그림 생성(Google Flow, 채널 전용 프로젝트) → img/<id>.png
# python img.py [--sample] [id ...]   : 있으면 건너뜀, id 를 주면 그것만 다시
import sys, time
from pathlib import Path
W = Path(__file__).parent
sys.path.insert(0, str(W)); sys.path.insert(0, str(W.parent))
import importlib, os, flow_img
plan = importlib.import_module(os.environ.get("LW_PLAN", "plan"))

IMG = W / getattr(plan, "IMG_DIR", "img"); IMG.mkdir(exist_ok=True)
args = [a for a in sys.argv[1:] if not a.startswith("--")]
scenes = [s for s in plan.SCENES if s.get("sample")] if "--sample" in sys.argv else plan.SCENES
if not flow_img.ready():
    sys.exit("flowkit 확장이 연결되지 않음")
for s in scenes:
    if not s.get("prompt") or s.get("use"):     # 실제 사진·영상·재사용 그림 장면은 만들지 않는다
        continue
    out = IMG / f"{s['id']}.png"
    if args and s["id"] not in args:
        continue
    if out.exists() and not args:
        continue
    if hasattr(plan, "BRIGHT") and not s.get("dark"):   # 밝은 자연광 방식(원래 채널 밝기에 맞춤) — 어두운 장면만 기존 톤
        prompt = f"{plan.BRIGHT} Scene: {s['prompt']}"
    else:
        prompt = f"{plan.STYLE}{plan.DARK if s.get('dark') else ''} Scene: {s['prompt']}"
    t = time.time()
    for attempt in range(4):                    # CAPTCHA_TIMEOUT 등으로 막히면 4분 쉬고 이어서(2026-10-02 실측: 4분 뒤 풀림)
        try:
            flow_img.generate(prompt, out)
            break
        except RuntimeError as e:
            if attempt == 3:
                raise
            print("막힘, 4분 대기", s["id"], flush=True)
            time.sleep(240)
    print("ok", s["id"], round(time.time() - t), "s", flush=True)
    time.sleep(30)          # Flow 는 연달아 많이 요청하면 UNUSUAL_ACTIVITY 로 막힌다
print("done")
