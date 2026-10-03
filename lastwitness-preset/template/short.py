# 마지막 목격자 — 쇼츠(1080×1920): 완성 본편 영상(final_eg.mp4)에서 구간만 잘라 세로로 배치(새로 렌더하지 않음, 2026-10-02 사용자 지시)
# python short.py <시작초> <끝초> <이름> "<위 제목(\n 줄바꿈, 마지막 줄 노랑)>"
# 배치: 흐린 배경(같은 영상) · 가운데 본편 화면(가운데 4:3 = 1440×1080 → 1080×810, 아래 자막 띠까지 들어감) · 위 제목 · 끝 3초 '전체 이야기는 채널에서 ▶'
import subprocess, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W = Path(__file__).parent
SRC = W / "final_dy.mp4"
BH = str(W.parent / "fonts" / "BlackHanSans-Regular.ttf")
SW, SH, FY = 1080, 1920, 520          # 가운데 화면 위쪽 y
FULL = "--full" in sys.argv; sys.argv = [a for a in sys.argv if a != "--full"]   # 카드처럼 글자가 넓은 구간은 16:9 전체
CTA_POLICE = "--cta-button" not in sys.argv   # 끝 안내 = 폴리스라인 테이프(수평)가 기본(사용자 확정 2026-10-03). 예전 빨간 버튼은 --cta-button
sys.argv = [a for a in sys.argv if a not in ("--cta-police", "--cta-button")]
t0, t1, name, title = float(sys.argv[1]), float(sys.argv[2]), sys.argv[3], sys.argv[4].replace("\\n", "\n")
dur = t1 - t0
OUT = W / "shorts"; OUT.mkdir(exist_ok=True)

top = Image.new("RGBA", (SW, SH), (0, 0, 0, 0)); d = ImageDraw.Draw(top)
f = ImageFont.truetype(BH, 104); lines = title.split("\n"); y = 190
for i, ln in enumerate(lines):
    d.text((SW / 2, y), ln, font=f, anchor="mt", fill=(255, 241, 84) if i == len(lines) - 1 else (255, 255, 255), stroke_width=9, stroke_fill=(10, 10, 10))
    y += 128
d.rectangle((SW / 2 - 150, 92, SW / 2 - 142, 136), fill=(214, 36, 36))
d.text((SW / 2 - 128, 114), "마지막 목격자", font=ImageFont.truetype(BH, 40), anchor="lm", fill=(235, 235, 235), stroke_width=3, stroke_fill=(0, 0, 0))
top.save(OUT / "_top.png")
cta = Image.new("RGBA", (SW, SH), (0, 0, 0, 0)); d = ImageDraw.Draw(cta)
f2 = ImageFont.truetype(BH, 64); txt = "전체 이야기는 채널에서"
tw = d.textlength(txt, font=f2); tri = 46                      # ▶ 는 검은고딕에 없어서 도형으로 그린다
x0 = SW / 2 - (tw + 24 + tri) / 2
d.rounded_rectangle((x0 - 44, 1395, x0 + tw + 24 + tri + 44, 1395 + 110), 55, fill=(214, 36, 36, 235))
d.text((x0, 1450), txt, font=f2, anchor="lm", fill=(255, 255, 255))
tx = x0 + tw + 24; d.polygon([(tx, 1450 - tri / 2), (tx, 1450 + tri / 2), (tx + tri * 0.85, 1450)], fill=(255, 255, 255))
if CTA_POLICE:                                   # 폴리스라인 테이프: 화면을 가로지르는 노란 테이프, 위아래 'POLICE LINE · DO NOT CROSS', 가운데 문구 + ▶
    K = 3; th = 150 * K; tw_ = (SW + 400) * K
    tape = Image.new("RGBA", (tw_, th), (255, 212, 0, 255)); dt = ImageDraw.Draw(tape)
    for y0 in (6 * K, th - 10 * K):
        dt.rectangle((0, y0, tw_, y0 + 4 * K), fill=(18, 18, 18))
    small = ImageFont.truetype(BH, 22 * K); rep = "POLICE LINE   •   DO NOT CROSS   •   " * 10
    dt.text((0, 27 * K), rep, font=small, fill=(18, 18, 18), anchor="lm"); dt.text((-60 * K, th - 28 * K), rep, font=small, fill=(18, 18, 18), anchor="lm")
    fb = ImageFont.truetype(BH, 62 * K); ww = dt.textlength(txt, font=fb); tri_ = 44 * K
    xs = tw_ / 2 - (ww + 26 * K + tri_) / 2
    dt.text((xs, th / 2 + 3 * K), txt, font=fb, fill=(12, 12, 12), anchor="lm")
    tx_ = xs + ww + 26 * K
    dt.polygon([(tx_, th / 2 - tri_ / 2), (tx_, th / 2 + tri_ / 2), (tx_ + tri_ * 0.85, th / 2)], fill=(12, 12, 12))
    # 기울이지 않고 수평(사용자 요청 2026-10-03)
    tape = tape.resize((tape.width // K, tape.height // K), Image.LANCZOS)
    cta = Image.new("RGBA", (SW, SH), (0, 0, 0, 0))
    sh_ = Image.new("RGBA", tape.size, (0, 0, 0, 0)); sh_.putalpha(tape.getchannel("A").point(lambda v: int(v * 0.6)))
    from PIL import ImageFilter
    sh_ = sh_.filter(ImageFilter.GaussianBlur(10))
    cx_, cy_ = (SW - tape.width) // 2, 1450 - tape.height // 2
    cta.alpha_composite(sh_, (cx_ + 8, cy_ + 12)); cta.alpha_composite(tape, (cx_, cy_))
cta.save(OUT / "_cta.png")

# 가운데 4:3 으로 자르면 본편 왼쪽 위 날짜·설명 표시가 잘린다 → 같은 모양으로 다시 그려 그 자리에 덮는다
import json, os, importlib
sys.path.insert(0, str(W)); os.environ.setdefault("LW_PLAN", "plan_dy")
plan = importlib.import_module(os.environ["LW_PLAN"])
caps = {} if getattr(plan, "NOCAP", False) else {sc["id"]: sc["cap"] for sc in plan.SCENES if sc.get("cap")}
names = {sc["id"]: sc["name"] for sc in plan.SCENES if sc.get("name")}
LBF = str(W.parent / "fonts" / "GothicA1-Bold.ttf")
lab_inputs, lab_filters = [], []
for a, b, sid in json.load(open(W / "final_dy_tl.json")):
    if sid not in caps or b <= t0 or a >= t1 or FULL:
        continue
    fl = ImageFont.truetype(LBF, 22); dd = ImageDraw.Draw(Image.new("RGBA", (10, 10)))
    bb = dd.textbbox((0, 0), caps[sid], font=fl)
    im = Image.new("RGBA", (bb[2] - bb[0] + 34, 40), (0, 0, 0, 0)); d3 = ImageDraw.Draw(im)
    d3.rectangle((0, 0, im.width - 1, 39), fill=(0, 0, 0, 200)); d3.rectangle((0, 0, 3, 39), fill=(200, 30, 30, 255))
    d3.text((16, 20 - (bb[3] + bb[1]) // 2), caps[sid], font=fl, fill=(235, 235, 235))
    pth = OUT / f"_cap_{sid}.png"; im.save(pth)
    lab_inputs += ["-i", str(pth)]
    lab_filters.append((max(a - t0, 0), min(b - t0, t1 - t0), 0, FY + 18))
for a, b, sid in json.load(open(W / "final_dy_tl.json")):          # 이름 라벨(4:3 으로 자르면 왼쪽이 끊김)
    if sid not in names or b <= t0 or a >= t1 or FULL:
        continue
    ko, en = names[sid]; im = Image.new("RGBA", (660, 168), (0, 0, 0, 0)); d4 = ImageDraw.Draw(im)
    d4.rounded_rectangle((-30, 0, 640, 168), 24, fill=(10, 10, 10, 225))          # 어두운 바탕으로 잘린 원래 라벨을 가린다
    d4.text((22, 60), ko, font=ImageFont.truetype(BH, 76), fill=(240, 70, 50), anchor="lm", stroke_width=5, stroke_fill=(20, 8, 8))
    d4.text((24, 128), en, font=ImageFont.truetype(LBF, 31), fill=(245, 245, 245), anchor="lm")
    pth = OUT / f"_name_{sid}.png"; im.save(pth); lab_inputs += ["-i", str(pth)]
    lab_filters.append((max(a - t0 + 0.3, 0), min(b - t0, t1 - t0), 0, FY + 525))   # 본편 라벨 자리(y=720×0.75=540) 그대로 덮는다

out = OUT / f"{name}.mp4"
fc = (f"[0:v]split=2[a][b];"
      f"[a]scale=-2:{SH},crop={SW}:{SH},boxblur=28:2,eq=brightness=-0.18[bg];"
      + (f"[b]scale={SW}:608[fg];" if FULL else f"[b]crop=1440:1080:240:0,scale={SW}:810[fg];") +
      f"[bg][fg]overlay=0:{FY + (100 if FULL else 0)}[v1];[v1][1:v]overlay=0:0[v2];"
      + "".join(f"[v2{'' if k == 0 else f'_{k}'}][{3 + k}:v]overlay={x}:{y}:enable='between(t,{a:.2f},{b:.2f})'[v2_{k + 1}];" for k, (a, b, x, y) in enumerate(lab_filters))
      + f"[v2{'' if not lab_filters else f'_{len(lab_filters)}'}][2:v]overlay=0:0:enable='gte(t,{dur - 3:.2f})'[v3];"
      f"[v3]fade=t=in:st=0:d=0.25,fade=t=out:st={dur - 0.3:.2f}:d=0.3[v]")
subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", f"{t0:.3f}", "-t", f"{dur:.3f}", "-i", str(SRC), "-i", str(OUT / "_top.png"), "-i", str(OUT / "_cta.png"), *lab_inputs,
                "-filter_complex", fc, "-map", "[v]", "-map", "0:a", "-af", f"afade=t=in:d=0.2,afade=t=out:st={dur - 0.4:.2f}:d=0.4",
                "-c:v", "libx264", "-crf", "19", "-preset", "medium", "-pix_fmt", "yuv420p", "-r", "30", "-c:a", "aac", "-b:a", "192k",
                "-movflags", "+faststart", str(out)], check=True)
print("ok", out, f"{dur:.1f}s")
