"""마지막 목격자 채널 — Flow Omni Flash(재연 그림 → 움직이는 영상) 헬퍼. 의학의 역사 omni_video.py 의 채널 전용 사본.
python omni_video.py <편 폴더> <그림폴더> <장면id>:<초>:"<움직임 설명>" ...   → <편>/anim/<장면id>_omni.mp4
실제 인물 사진은 AI 로 움직이지 않는다(사실 왜곡) — 재연 그림에만 쓴다. 길이는 4/6/8/10초. flowkit 서버(127.0.0.1:8100) 필요.
"""
import json, sys, time, uuid, urllib.request
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent)); import flow_img

KEEP = ("Keep the exact photorealistic look, colors, lighting, place and people of the image; do not add new people or objects, "
        "no text, no blood, no gore. Smooth, slow, natural realistic motion like documentary footage, subtle camera movement. ")


def _post(path, body, timeout=300):
    r = urllib.request.Request(flow_img.API + path, json.dumps(body).encode(), {"Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(r, timeout=timeout))


def make(ep, sid, dur, motion, imgdir="img"):
    out = Path(ep) / "anim" / f"{sid}_omni.mp4"; out.parent.mkdir(exist_ok=True)
    if out.exists():
        return out
    mid = flow_img._upload(str(Path(ep) / imgdir / f"{sid}.png"))
    for attempt in range(3):
        try:
            d = _post("/api/flow/generate-video", {"start_image_media_id": mid, "project_id": flow_img.PROJECT, "scene_id": str(uuid.uuid4()),
                                                  "aspect_ratio": "VIDEO_ASPECT_RATIO_LANDSCAPE", "user_paygate_tier": "PAYGATE_TIER_TWO",
                                                  "prompt": KEEP + motion, "model_family": "omni_flash", "duration_s": dur})
            ops = d["flowkitPolling"]["operations"]; t0 = time.time()
            while time.time() - t0 < 600:
                time.sleep(10)
                res = _post("/api/flow/check-status", {"operations": ops, "project_id": flow_img.PROJECT}, 120)
                s = json.dumps(res)
                if "SUCCESSFUL" in s:
                    url = res["operations"][0]["operation"]["metadata"]["video"]["fifeUrl"]
                    q = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
                    out.write_bytes(urllib.request.urlopen(q, timeout=300).read())
                    print("ok", sid, dur, "s", int(time.time() - t0), "s", flush=True); return out
                if "FAILED" in s:
                    print("failed", sid, s[:300], flush=True); break
        except Exception as e:
            print("err", sid, e, getattr(e, "read", lambda: b"")()[:300], flush=True)
        time.sleep(10)
    raise RuntimeError(f"omni 실패 {sid}")


if __name__ == "__main__":
    ep, imgdir = sys.argv[1], sys.argv[2]
    for spec in sys.argv[3:]:
        sid, dur, motion = spec.split(":", 2)
        for k in range(3):                      # Flow 가 막히면 4분 쉬고 다시
            try:
                make(ep, sid, int(dur), motion, imgdir); break
            except RuntimeError:
                time.sleep(240)
        time.sleep(30)
    print("done")
