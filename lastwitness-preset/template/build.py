# 마지막 목격자 — 영상 조립 (1920×1080, 30fps)
# python build.py [--sample]
# 화면 형식(원래 채널 형식을 따름): 장면 그림 + 느린 확대·이동(OpenCV warpAffine — zoompan 떨림 없음)
#   아래 흰 종이 띠 + 검은 자막(16자 한 줄) · 인용문은 띠 없이 가운데 노란 큰따옴표 글자(화면 어둡게) · 왼쪽 위 'AI 재연 이미지' 표시
# 소리: 나레(Typecast) + 직접 합성한 어두운 앰비언트 BGM(저작권 없음) + 합성 효과음, 최종 -14 LUFS
import json, math, random, re, subprocess, sys
from pathlib import Path
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W = Path(__file__).parent; CH = W.parent
sys.path.insert(0, str(W)); sys.path.insert(0, str(CH))
import importlib, os, subsplit
plan = importlib.import_module(os.environ.get("LW_PLAN", "plan"))   # LW_PLAN=plan_s1 이면 1분 샘플
subsplit.NAMES += plan.NAMES
from subsplit import wlen, break_penalty, balanced, clean, ts   # sub_check.py 가 build 에서 가져다 쓴다

SAMPLE = "--sample" in sys.argv
SCENES = [s for s in plan.SCENES if s.get("sample")] if SAMPLE else plan.SCENES
VW, VH, FPS, SR = 1920, 1080, 30, 48000
FONTS = CH / "fonts"
SUBF, QF, LBF = str(FONTS / "GothicA1-Black.ttf"), str(FONTS / "BlackHanSans-Regular.ttf"), str(FONTS / "GothicA1-Bold.ttf")
GAP_LINE, GAP_SCENE, LEAD, TAIL, QPAD = 0.32, 0.6, 0.45, 1.8, 0.3
OUTNAME = getattr(plan, "OUTNAME", "sample" if SAMPLE else "final")
TTS = W / getattr(plan, "TTS_DIR", "tts")
IMGD = W / getattr(plan, "IMG_DIR", "img")


# ── 타임라인 ─────────────────────────────────────────────
def timeline():
    dur = json.load(open(TTS / "durations.json"))
    intro = getattr(plan, "INTRO", None)
    tl, now = [], (intro.get("lead", 2.4) if intro else LEAD)   # 인트로 신호음이 있으면 말은 그 뒤에
    for k, s in enumerate(SCENES):
        st = 0.0 if k == 0 else now - GAP_SCENE / 2
        lines = []
        for i, L in enumerate(s["lines"]):
            q = len(L) > 2 and "q" in L[2]
            if q:
                now += QPAD
            d = dur[f"{s['id']}_{i}"]
            lines.append(dict(i=i, text=L[0], q=q, start=now, end=now + d))
            now += d + (QPAD if q else 0) + GAP_LINE
        now += GAP_SCENE - GAP_LINE
        tl.append(dict(s=s, start=st, lines=lines))
    for a, b in zip(tl, tl[1:]):
        a["end"] = b["start"]
    tl[-1]["end"] = now - GAP_SCENE / 2 + TAIL
    return tl


# ── 그림 ────────────────────────────────────────────────
PLACE = {}   # 사진 경로 → (x, y, 배율) : 원본 사진 좌표 → 화면 좌표


def photo_image(path):
    """실제 옛 사진: 같은 사진을 크게 흐리게 깐 배경 + 가운데 사진(그림자)"""
    ph = cv2.imdecode(np.fromfile(str(W / path), np.uint8), cv2.IMREAD_COLOR)
    h, w = ph.shape[:2]
    sc = max(VW / w, VH / h)
    bg = cv2.resize(ph, (math.ceil(w * sc), math.ceil(h * sc)))
    y0 = (bg.shape[0] - VH) // 2; x0 = (bg.shape[1] - VW) // 2
    bg = cv2.GaussianBlur(bg[y0:y0 + VH, x0:x0 + VW], (0, 0), 28)
    bg = cv2.convertScaleAbs(bg, alpha=0.42)
    fs = min(1640 / w, 960 / h)
    fg = cv2.resize(ph, (int(w * fs), int(h * fs)), interpolation=cv2.INTER_CUBIC if fs > 1 else cv2.INTER_AREA)
    fh, fw = fg.shape[:2]
    x, y = (VW - fw) // 2, (VH - fh) // 2 - 20
    sh = np.zeros((VH, VW), np.float32); sh[y + 10:y + fh + 10, x + 10:x + fw + 10] = 1
    sh = cv2.GaussianBlur(sh, (0, 0), 14)[..., None] * 0.6
    bg = (bg * (1 - sh)).astype(np.uint8)
    bg[y:y + fh, x:x + fw] = fg
    PLACE[path] = (x, y, fs)
    return bg


def base_image(sid):
    scn = next(s for s in SCENES if s["id"] == sid)
    if scn.get("photo"):
        return photo_image(scn["photo"])
    src = W / scn["use"] if scn.get("use") else IMGD / f"{sid}.png"     # use = 다른 폴더의 기존 그림 재사용
    im = cv2.imdecode(np.fromfile(str(src), np.uint8), cv2.IMREAD_COLOR)   # 한글 경로라 imread 대신
    g = im.mean(axis=(1, 2))                                  # 위아래 검은 띠(Flow 가 가끔 붙임) 잘라내기
    top = next((y for y in range(len(g)) if g[y] > 14), 0)
    bot = next((y for y in range(len(g) - 1, 0, -1) if g[y] > 14), len(g) - 1)
    im = im[top:bot + 1]
    h, w = im.shape[:2]
    sc = max(VW / w, VH / h)
    im = cv2.resize(im, (math.ceil(w * sc), math.ceil(h * sc)), interpolation=cv2.INTER_CUBIC)
    y0 = (im.shape[0] - VH) // 2; x0 = (im.shape[1] - VW) // 2
    im = im[y0:y0 + VH, x0:x0 + VW].astype(np.float32)
    yy, xx = np.mgrid[0:VH, 0:VW].astype(np.float32)          # 비네트(가장자리 어둡게)를 그림에 굽는다
    r = np.sqrt(((xx - VW / 2) / (VW / 2)) ** 2 + ((yy - VH / 2) / (VH / 2)) ** 2)
    if getattr(plan, "GRADE", False) and not str(scn.get("use", "")).startswith("cards/"):
        return archive_grade(im, sid, "teal" if scn.get("dark") else "sepia", xx, yy, r)
    vig = np.clip(1 - 0.38 * np.clip(r - 0.55, 0, None) ** 1.6, 0.55, 1)[..., None]
    return np.clip(im * vig, 0, 255).astype(np.uint8)


def archive_grade(im, sid, tone, xx, yy, r):
    """원래 채널 같은 '오래된 기록물' 톤(2026-10-02 사용자 요청): 채도 낮춤 + 세피아/청록 + 대비 + 비네트 + 빛 번짐. 밤 장면은 밝기를 조금 올린다"""
    f = im / 255.0
    g = f.mean(axis=2, keepdims=True)
    f = f * 0.38 + g * 0.62
    f = f * (np.array([0.80, 0.93, 1.10]) if tone == "sepia" else np.array([1.08, 1.00, 0.86]))
    f = np.clip((f - 0.5) * 1.18 + 0.5, 0, 1) ** 0.88                     # 대비 + 살짝 밝게
    f *= np.clip(1.12 - 0.62 * r ** 1.9, 0.28, 1)[..., None]
    return np.clip(f * 255, 0, 255).astype(np.uint8)         # 빛 번짐은 leak_layer 로 따로(렌더에서 천천히 일렁임)


_LEAK = {}


def leak_layer(sid):
    """장면마다 다른 자리의 주황 빛 번짐(0~1, BGR). 렌더에서 4초 주기로 은은하게 세기만 바뀐다 — 화면 밝기 깜빡임 아님"""
    if sid not in _LEAK:
        _LEAK.clear()
        rs = np.random.default_rng(abs(hash(sid)) % 2 ** 32)
        yy, xx = np.mgrid[0:VH, 0:VW].astype(np.float32)
        cx, cy = rs.choice([rs.uniform(0, VW * 0.25), rs.uniform(VW * 0.75, VW)]), rs.uniform(0, VH * 0.35)
        m = np.exp(-(((xx - cx) / (VW * 0.33)) ** 2 + ((yy - cy) / (VH * 0.42)) ** 2))
        _LEAK[sid] = (m[..., None] * np.array([0.06, 0.28, 0.6], np.float32) * 0.75).astype(np.float32), rs.uniform(0, 6.28)
    return _LEAK[sid]


def apply_leak(fr, sid, t, base=0.62, amp=0.38, period=4.2):
    lay, ph = leak_layer(sid)
    k = base + amp * (0.5 + 0.5 * math.sin(2 * math.pi * t / period + ph))
    f = fr.astype(np.float32) / 255
    return np.clip((1 - (1 - f) * (1 - lay * k)) * 255, 0, 255).astype(np.uint8)


def camcorder(fr, t):
    """실제 사진: 네 모서리 뷰파인더 표시 + 색 어긋남(VHS 느낌)"""
    out = fr.copy()
    out[:, 3:, 2] = fr[:, :-3, 2]; out[:, :-3, 0] = fr[:, 3:, 0]           # 빨강은 오른쪽, 파랑은 왼쪽으로 3px
    m, L, c = 46, 70, (235, 235, 235)
    for (x, y, dx, dy) in ((m, m, 1, 1), (VW - m, m, -1, 1), (m, VH - m, 1, -1), (VW - m, VH - m, -1, -1)):
        cv2.line(out, (x, y), (x + dx * L, y), c, 4, cv2.LINE_AA); cv2.line(out, (x, y), (x, y + dy * L), c, 4, cv2.LINE_AA)
    return out


def motion(k, u, d):
    """장면 진행도 u(0~1) → (확대, x이동, y이동). 모든 장면 같은 방향으로 아주 천천히 다가가기만(초당 0.8%, 일정한 속도).
    좌우 이동·멀어지기는 없앰 — 짧은 장면에서 화면이 좌우로 흔들려 보였다(2026-10-02 사용자 지적)"""
    return 1.02 + min(0.008 * d, 0.09) * u, 0, 0


def warp(img, z, dx, dy):
    M = np.float32([[z, 0, (1 - z) * VW / 2 + dx], [0, z, (1 - z) * VH / 2 + dy]])
    return cv2.warpAffine(img, M, (VW, VH), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)


# ── 애니메이션 효과 (2026-10-02 사용자 "애니메이션 효과 추가") ──
# 실제 사진: 툭 들어오기(확대→제자리) + 셔터 번쩍 + 옛 필름 결·긁힘 + 빨간 동그라미(hl)
# 재연 그림: anim/<id>_omni.mp4 가 있으면 AI 영상으로(실존 인물 사진은 AI 로 움직이지 않는다)
_rng = np.random.default_rng(11)
GRAIN = [(_rng.normal(0, 9, (VH // 2, VW // 2))).astype(np.float32) for _ in range(6)]
GRAIN = [cv2.resize(g, (VW, VH), interpolation=cv2.INTER_LINEAR)[..., None] for g in GRAIN]


def film(fr, fi):
    """옛 사진 질감: 프레임마다 바뀌는 결 + 가끔 세로 긁힘(밝기 깜빡임은 없음 — 눈 아프다는 의견 반영)"""
    out = fr.astype(np.float32) + GRAIN[fi % len(GRAIN)]
    r = np.random.default_rng(fi // 3)
    if r.random() < 0.18:
        x = int(r.uniform(80, VW - 80)); w = int(r.integers(1, 3))
        out[:, x:x + w] = out[:, x:x + w] * 0.6 + 200 * 0.4
    return np.clip(out, 0, 255).astype(np.uint8)


def draw_circle(img, box, u):
    """손으로 그린 듯한 빨간 타원을 u(0~1)만큼 그린다"""
    x0, y0, x1, y1 = box
    cx, cy, ax, ay = (x0 + x1) / 2, (y0 + y1) / 2, (x1 - x0) / 2 * 1.15, (y1 - y0) / 2 * 1.15
    n = max(int(64 * min(u, 1) * 1.08), 2)
    th = np.linspace(-2.2, -2.2 + 2 * math.pi * 1.08 * min(u, 1), n)
    wob = 1 + 0.03 * np.sin(th * 3.0)
    pts = np.stack([cx + ax * wob * np.cos(th), cy + ay * wob * np.sin(th)], 1).astype(np.int32)
    cv2.polylines(img, [pts], False, (40, 40, 225), 9, cv2.LINE_AA)


class Anim:
    """AI 영상 프레임을 장면 시간에 맞춰 앞으로만 읽는다(메모리에 다 올리지 않음)"""
    def __init__(self, path, scene_dur):
        self.cap = cv2.VideoCapture(str(path)); self.fps = self.cap.get(5) or 24
        self.n = int(self.cap.get(7)); self.idx = -1; self.cur = None
        self.rate = min(1.0, (self.n / self.fps) / max(scene_dur, 0.1))   # 영상이 짧으면 살짝 느리게
    def frame(self, tt):
        want = min(int(tt * self.rate * self.fps), self.n - 1)
        while self.idx < want:
            ok, f = self.cap.read()
            if not ok:
                break
            self.idx += 1; self.cur = f
        if self.cur is None:
            return None
        h, w = self.cur.shape[:2]
        sc = max(VW / w, VH / h)
        f = cv2.resize(self.cur, (math.ceil(w * sc), math.ceil(h * sc)), interpolation=cv2.INTER_CUBIC)
        y0 = (f.shape[0] - VH) // 2; x0 = (f.shape[1] - VW) // 2
        return f[y0:y0 + VH, x0:x0 + VW]


class Foot:
    """실제 기록 영상(퍼블릭 도메인): t0 초부터 실제 속도로, 양옆·위아래 검은 띠는 잘라내고 화면을 꽉 채운다"""
    def __init__(self, path, t0):
        self.cap = cv2.VideoCapture(str(W / path)); self.fps = self.cap.get(5) or 24
        self.cap.set(0, t0 * 1000); self.idx = -1; self.cur = None; self.box = None
    def frame(self, tt):
        want = int(tt * self.fps)
        while self.idx < want:
            ok, f = self.cap.read()
            if not ok:
                break
            self.idx += 1; self.cur = f
        if self.cur is None:
            return None
        f = self.cur
        if self.box is None:                                  # 검은 띠 찾기(첫 프레임 기준)
            g = f.mean(axis=2); cols = np.where(g.mean(0) > 18)[0]; rows = np.where(g.mean(1) > 18)[0]
            self.box = (rows[0], rows[-1] + 1, cols[0], cols[-1] + 1) if len(cols) and len(rows) else (0, f.shape[0], 0, f.shape[1])
        y0, y1, x0, x1 = self.box
        f = f[y0:y1, x0:x1]
        h, w = f.shape[:2]; sc = max(VW / w, VH / h)
        f = cv2.resize(f, (math.ceil(w * sc), math.ceil(h * sc)), interpolation=cv2.INTER_CUBIC)
        oy = (f.shape[0] - VH) // 2; ox = (f.shape[1] - VW) // 2
        return f[oy:oy + VH, ox:ox + VW]


# ── 엔딩 좋아요·구독 버튼 (의학의 역사 endcard_yt 그대로, 2026-10-02 사용자 요청) ──
def endcard_times(sc):
    """장면 안 상대 시각: 등장, 좋아요 클릭, 구독 클릭"""
    L = sc["lines"][0]; t0 = L["start"] - sc["start"]; ln = L["end"] - L["start"]
    return t0 + 0.15, t0 + max(0.9, ln * 0.45), t0 + max(1.5, ln * 0.78)


def endcard_frame(fr, tt, sc):
    import endcard_yt
    t_in, t_like, t_sub = endcard_times(sc)
    return endcard_yt.frame(fr, tt, t_in, t_like, t_sub, str(FONTS / "Jalnan2TTF.ttf"), VW)


# ── 끝: 브라운관 TV 꺼지는 효과 (2026-10-02 사용자 요청) ──
TVOFF_DUR = 0.75


def tv_off(fr, u):
    """u: 0→1. 세로로 눌려 밝은 가로줄 → 가로줄이 점으로 → 점이 사라짐"""
    out = np.zeros_like(fr)
    cx, cy = VW // 2, VH // 2
    if u < 0.4:                                            # 1) 세로로 눌리며 하얗게
        v = u / 0.4; e = v ** 2.2
        h = max(int(VH * (1 - e) + 6 * e), 6); w = int(VW * (1 + 0.06 * e))
        img = cv2.resize(fr, (w, h), interpolation=cv2.INTER_AREA)
        img = cv2.addWeighted(img, 1 - 0.85 * e, np.full_like(img, 255), 0.85 * e, 0)
        x0 = cx - w // 2; y0 = cy - h // 2
        xs, xe = max(x0, 0), min(x0 + w, VW)
        out[y0:y0 + h, xs:xe] = img[:, xs - x0:xe - x0]
    elif u < 0.75:                                         # 2) 가로줄이 점으로
        v = (u - 0.4) / 0.35; w = max(int(VW * 1.06 * (1 - v) ** 1.8), 8)
        cv2.line(out, (cx - w // 2, cy), (cx + w // 2, cy), (255, 255, 255), 5, cv2.LINE_AA)
        glow = cv2.GaussianBlur(out, (0, 0), 9)
        out = cv2.add(out, glow)
    else:                                                  # 3) 점이 사라짐
        v = (u - 0.75) / 0.25; r = max(int(7 * (1 - v)), 1)
        cv2.circle(out, (cx, cy), r, (int(255 * (1 - v)),) * 3, -1, cv2.LINE_AA)
        out = cv2.add(out, cv2.GaussianBlur(out, (0, 0), 6))
    return out


def sfx_tvoff():
    """전원 차단 '틱' + 낮은 '퉁' + 잦아드는 고음 '징'"""
    rng = np.random.default_rng(13); k = np.arange(int(1.0 * SR)) / SR
    click = rng.normal(0, 1, len(k)) * np.exp(-k / 0.004)
    thump = np.sin(2 * np.pi * (70 * np.exp(-k / 0.15) + 35) * k) * np.exp(-k / 0.12)
    whine = np.sin(2 * np.pi * np.cumsum(9000 * np.exp(-k / 0.25) + 1500) / SR) * np.exp(-k / 0.22) * 0.18
    return ((click * 0.5 + thump * 0.8 + whine) * 0.6).astype(np.float32)


def name_img(ko, en):
    """인물 이름 라벨(원래 채널처럼 빨간 한글 + 흰 영어)"""
    f1, f2 = ImageFont.truetype(QF, 92), ImageFont.truetype(LBF, 40)
    im = Image.new("RGBA", (900, 190), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.text((10, 70), ko, font=f1, fill=(240, 70, 50), anchor="lm", stroke_width=6, stroke_fill=(20, 8, 8))
    d.text((14, 150), en, font=f2, fill=(245, 245, 245), anchor="lm", stroke_width=4, stroke_fill=(10, 10, 10))
    return rgba(im)


_STAMP = None


def stamp_img():
    """빨간 화면 위 'MISSING' 도장(직접 그림, 닳은 질감)"""
    global _STAMP
    if _STAMP is None:
        f = ImageFont.truetype(QF, 170)
        im = Image.new("RGBA", (1100, 330), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
        d.rounded_rectangle((20, 20, 1080, 310), 26, outline=(255, 255, 255, 255), width=18)
        d.text((550, 168), "MISSING", font=f, fill=(255, 255, 255, 255), anchor="mm")
        a = np.asarray(im).astype(np.float32); rng = np.random.default_rng(4)
        holes = (rng.random(a.shape[:2]) > 0.16).astype(np.float32)
        holes = cv2.GaussianBlur(holes, (0, 0), 1.2)
        a[..., 3] *= holes
        im = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).rotate(14, expand=True, resample=Image.BICUBIC)
        _STAMP = im
    return _STAMP


def red_tint(fr):
    g = fr.mean(axis=2, keepdims=True).astype(np.float32)
    out = np.concatenate([g * 0.22, g * 0.22, np.clip(g * 1.05 + 40, 0, 255)], axis=2)
    return np.clip(out, 0, 255).astype(np.uint8)


def qcard_img(text):
    """흰·빨강 큰 인용문 카드(원래 채널 형식): 마지막 쉼표 앞은 흰색, 뒤는 빨강"""
    text = re.sub(r"[.]+$", "", text.strip())
    a, b = (text.rsplit(",", 1) + [""])[:2] if "," in text else (text, "")
    a = a.strip() + ("," if b else ""); b = b.strip()
    f = ImageFont.truetype(QF, 78); lh = 104
    lines = [(ln, (245, 245, 245)) for ln in wrap_quote(a, 17)] + ([(ln, (235, 60, 50)) for ln in wrap_quote(b, 17)] if b else [])
    im = Image.new("RGBA", (VW, lh * len(lines) + 160), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    w0 = d.textlength(lines[0][0], font=f)
    d.text((VW / 2 - w0 / 2 - 24, 128), "“", font=ImageFont.truetype(LBF, 200), fill=(245, 245, 245), anchor="rm")   # 여는 따옴표를 첫 줄 바로 앞에 크게
    for j, (ln, col) in enumerate(lines):
        d.text((VW / 2, 120 + j * lh), ln, font=f, fill=col, anchor="mm", stroke_width=4, stroke_fill=(10, 10, 10))
    wl = d.textlength(lines[-1][0], font=f); yl = 120 + (len(lines) - 1) * lh   # 닫는 따옴표를 마지막 줄 바로 뒤에(2026-10-03 사용자 지적: 여는 것만 있었음)
    d.text((VW / 2 + wl / 2 + 20, yl + 62), "”", font=ImageFont.truetype(LBF, 200), fill=(245, 245, 245), anchor="lm")
    return rgba(im), im.height


# ── 글자 그래픽 ──────────────────────────────────────────
def rgba(im):
    a = np.asarray(im).astype(np.float32)
    return a[..., [2, 1, 0]], a[..., 3:] / 255.0              # BGR, alpha


def blend(frame, ov, x, y):
    col, al = ov
    h, w = al.shape[:2]
    x0, y0 = max(x, 0), max(y, 0); x1, y1 = min(x + w, VW), min(y + h, VH)
    if x1 <= x0 or y1 <= y0:
        return
    c = col[y0 - y:y1 - y, x0 - x:x1 - x]; a = al[y0 - y:y1 - y, x0 - x:x1 - x]
    roi = frame[y0:y1, x0:x1].astype(np.float32)
    frame[y0:y1, x0:x1] = (roi * (1 - a) + c * a).astype(np.uint8)


BAND_W, BAND_H = 1400, 78
_band = None


def paper_band():
    """흰 종이 질감 띠 — 결 노이즈 + 찢어진 양 끝 + 그림자"""
    global _band
    if _band is not None:
        return _band
    rng = np.random.default_rng(7)
    w, h, pad = BAND_W, BAND_H, 14
    base = np.full((h, w, 3), (232, 230, 224), np.float32)
    n = cv2.GaussianBlur(rng.normal(0, 9, (h, w)).astype(np.float32), (0, 0), 1.2)
    fib = cv2.GaussianBlur(rng.normal(0, 14, (h // 3 + 1, w // 40 + 1)).astype(np.float32), (0, 0), 0.8)
    fib = cv2.resize(fib, (w, h), interpolation=cv2.INTER_CUBIC)
    base += (n + fib * 0.6)[..., None]
    base[:, :, 2] += 3; base[:, :, 0] -= 2                    # 살짝 누런 종이
    alpha = np.ones((h, w), np.float32)
    jag_l = np.cumsum(rng.normal(0, 1.6, h)); jag_r = np.cumsum(rng.normal(0, 1.6, h))
    jag_l = 10 + (jag_l - jag_l.mean()) * 0.8; jag_r = 10 + (jag_r - jag_r.mean()) * 0.8
    for y in range(h):
        alpha[y, :max(int(jag_l[y]), 0)] = 0; alpha[y, w - max(int(jag_r[y]), 0):] = 0
    top = 2 + np.cumsum(rng.normal(0, 0.4, w)) * 0.3; bot = 2 + np.cumsum(rng.normal(0, 0.4, w)) * 0.3
    for x in range(0, w):
        alpha[:max(int(abs(top[x]) % 4), 0), x] = 0; alpha[h - max(int(abs(bot[x]) % 4), 0):, x] = 0
    alpha = cv2.GaussianBlur(alpha, (0, 0), 0.7)
    full = np.zeros((h + 2 * pad, w + 2 * pad, 4), np.float32)
    sh = cv2.GaussianBlur(np.pad(alpha, pad), (0, 0), 6) * 0.45   # 그림자
    sh = np.roll(np.roll(sh, 4, 0), 3, 1)
    full[..., 3] = np.maximum(sh, np.pad(alpha, pad))
    cpad = np.pad(base, ((pad, pad), (pad, pad), (0, 0)))
    ap = np.pad(alpha, pad)[..., None]
    full[..., :3] = cpad * ap / np.maximum(full[..., 3:], 1e-3)
    full[..., 3] *= 255
    _band = Image.fromarray(np.clip(full, 0, 255).astype(np.uint8), "RGBA")
    return _band


def sub_img(text):
    im = paper_band().copy()
    d = ImageDraw.Draw(im)
    f = ImageFont.truetype(SUBF, 44)
    bb = d.textbbox((0, 0), text, font=f)
    x = (im.width - (bb[2] - bb[0])) // 2 - bb[0]
    y = (im.height - (bb[3] - bb[1])) // 2 - bb[1]
    d.text((x, y), text, font=f, fill=(18, 18, 18))
    return rgba(im)


def wrap_quote(text, maxw=15):
    """인용문 줄바꿈: 줄 수 최소 → 떼면 안 되는 자리(관형형·수+단위·이름) 피함 → 줄 길이 균형"""
    words = text.split()
    if wlen(text) <= maxw:
        return [text]
    pens = [0] + [max(break_penalty(words[i - 1], words[i]), 0) for i in range(1, len(words))]
    best = None
    def rec(start, lines, score):
        nonlocal best
        if start == len(words):
            key = (len(lines), score, max(wlen(l) for l in lines) - min(wlen(l) for l in lines))
            if best is None or key < best[0]:
                best = (key, lines)
            return
        if len(lines) >= 3:
            return
        for e in range(start + 1, len(words) + 1):
            chunk = " ".join(words[start:e])
            if wlen(chunk) > maxw + 3:
                break
            rec(e, lines + [chunk], score + (pens[e] if e < len(words) else 0))
    rec(0, [], 0)
    return best[1] if best else [text]


def quote_img(text):
    text = re.sub(r"[.]+$", "", text.strip())
    lines = wrap_quote(text)
    lines[0] = "“" + lines[0]; lines[-1] = lines[-1] + "”"
    f = ImageFont.truetype(QF, 84)
    lh = 112
    im = Image.new("RGBA", (VW, lh * len(lines) + 80), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    for j, ln in enumerate(lines):
        bb = d.textbbox((0, 0), ln, font=f)
        x = (VW - (bb[2] - bb[0])) // 2 - bb[0]; y = 40 + j * lh
        d.text((x + 4, y + 5), ln, font=f, fill=(0, 0, 0, 170), stroke_width=7, stroke_fill=(0, 0, 0, 170))
        d.text((x, y), ln, font=f, fill=(255, 205, 38), stroke_width=5, stroke_fill=(28, 20, 8))
    im = im.filter(ImageFilter.SMOOTH)
    return rgba(im), im.height


def stat_img(text):
    text = text.replace("·", "/")                             # 검은고딕(BlackHanSans)에 가운뎃점 글리프가 없다
    f = ImageFont.truetype(QF, 96)
    im = Image.new("RGBA", (VW, 190), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    bb = d.textbbox((0, 0), text, font=f)
    tw = bb[2] - bb[0]; x = (VW - tw) // 2 - bb[0]
    d.rectangle(((VW - tw) // 2 - 50, 30, (VW + tw) // 2 + 50, 165), fill=(10, 10, 10, 190))
    d.rectangle(((VW - tw) // 2 - 50, 30, (VW - tw) // 2 - 38, 165), fill=(200, 30, 30, 255))
    d.text((x, 97 - (bb[3] + bb[1]) // 2), text, font=f, fill=(255, 255, 255))
    return rgba(im)


def label_img(t):
    f = ImageFont.truetype(LBF, 24)
    tmp = ImageDraw.Draw(Image.new("RGBA", (10, 10)))
    bb = tmp.textbbox((0, 0), t, font=f)
    im = Image.new("RGBA", (bb[2] - bb[0] + 28, 40), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, im.width - 1, 39), fill=(0, 0, 0, 175))
    d.rectangle((0, 0, 3, 39), fill=(200, 30, 30, 255))
    d.text((16, 20 - (bb[3] + bb[1]) // 2), t, font=f, fill=(235, 235, 235))
    return rgba(im)


# ── 자막 이벤트 ──────────────────────────────────────────
def sub_events(tl):
    ev = []
    for sc in tl:
        for L in sc["lines"]:
            if L["q"]:
                continue
            text = re.sub(r"[.,]+$", "", L["text"].strip()).replace("'", "")
            chunks = balanced(text)
            weights = [max(len(c.replace(" ", "")), 1) for c in chunks]
            tot = sum(weights); t0 = L["start"]; span = L["end"] - L["start"]
            for c, wgt in zip(chunks, weights):
                dd = span * wgt / tot
                ev.append([t0, t0 + dd, clean(c)]); t0 += dd
    prev = 0.0
    for e in ev:                                              # G1 최소 5/6초 · K2 초당 12자 이하
        need = max(5 / 6 + 0.01, wlen(e[2]) / 11.5)
        st = max(e[0], prev); en = max(e[1], st + need)
        e[0], e[1] = st, min(en, st + 7.0); prev = e[1]
    for a, b in zip(ev, ev[1:]):
        if b[0] - a[1] < 0.35:                                # 문장 사이 짧은 틈은 이어 붙여 깜빡임 방지
            a[1] = b[0]
    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {VW}
PlayResY: {VH}
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Sub,Gothic A1 Black,44,&H00121212,&H00121212,&H00E0E6E8,&H00000000,0,0,0,0,100,100,0,0,3,0,0,2,80,80,46,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    (W / f"{OUTNAME}_subs.ass").write_text(head + "".join(f"Dialogue: 0,{ts(a)},{ts(b)},Sub,,0,0,0,,{t}\n" for a, b, t in ev), encoding="utf-8")
    return ev


# ── 소리 ────────────────────────────────────────────────
def read_wav(p):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(p), "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"], capture_output=True).stdout
    return np.frombuffer(raw, np.float32)


def reverb(x, secs=2.2, wet=0.35, seed=1):
    from scipy.signal import fftconvolve
    rng = np.random.default_rng(seed)
    n = int(secs * SR); t = np.arange(n) / SR
    ir = rng.normal(0, 1, n) * np.exp(-t / (secs / 5)); ir /= np.sqrt((ir ** 2).sum())
    return x * (1 - wet) + fftconvolve(x, ir)[:len(x)] * wet


def bgm(T):
    """어두운 앰비언트: D단조 저음 드론 + 바람 소리 + 드문드문 피아노 음(리버브)"""
    from scipy.signal import lfilter
    n = int(T * SR); t = np.arange(n) / SR
    rng = np.random.default_rng(3)
    y = np.zeros(n)
    for f, a, lf in ((73.42, 0.30, 0.031), (73.9, 0.22, 0.027), (110.0, 0.16, 0.043), (146.83, 0.10, 0.021), (174.61, 0.06, 0.017), (220.0, 0.04, 0.05)):
        y += a * np.sin(2 * np.pi * f * t + rng.uniform(0, 6)) * (0.55 + 0.45 * np.sin(2 * np.pi * lf * t + rng.uniform(0, 6)))
    wind = lfilter([0.02], [1, -0.98], rng.normal(0, 1, n)); wind = lfilter([0.05], [1, -0.95], wind)
    y += wind / (np.abs(wind).max() + 1e-9) * 0.12 * (0.6 + 0.4 * np.sin(2 * np.pi * 0.07 * t))
    notes = [293.66, 349.23, 440.0, 523.25, 329.63, 392.0, 587.33, 220.0]
    pn = np.zeros(n)
    tt = 2.0
    while tt < T - 3:
        f = rng.choice(notes); L = int(4 * SR); s0 = int(tt * SR)
        k = np.arange(min(L, n - s0)) / SR
        env = np.exp(-k / 1.6) * np.minimum(k / 0.01, 1)
        tone = np.sin(2 * np.pi * f * k) + 0.35 * np.sin(4 * np.pi * f * k) * np.exp(-k / 0.6) + 0.12 * np.sin(6 * np.pi * f * k) * np.exp(-k / 0.3)
        pn[s0:s0 + len(k)] += tone * env * rng.uniform(0.10, 0.17)
        tt += rng.choice([2.6, 3.2, 3.9, 5.2])
    y += reverb(pn, 3.0, 0.55)
    fade = np.minimum(np.minimum(t / 2.0, 1), np.minimum((T - t) / 2.5, 1))
    return (y * fade / (np.abs(y).max() + 1e-9)).astype(np.float32)


def sfx_boom():
    k = np.arange(int(1.6 * SR)) / SR
    f = 55 * np.exp(-k / 0.5) + 32
    ph = 2 * np.pi * np.cumsum(f) / SR
    rng = np.random.default_rng(5)
    x = np.sin(ph) * np.exp(-k / 0.45) + rng.normal(0, 1, len(k)) * np.exp(-k / 0.04) * 0.25
    return reverb(x, 2.0, 0.4).astype(np.float32) * 0.9


def sfx_tick():
    k = np.arange(int(0.06 * SR)) / SR
    return (np.sin(2 * np.pi * 2400 * k) * np.exp(-k / 0.006) * 0.5).astype(np.float32)


def sfx_shutter():
    rng = np.random.default_rng(9); k = np.arange(int(0.16 * SR)) / SR
    x = rng.normal(0, 1, len(k)) * (np.exp(-k / 0.008) + 0.7 * np.exp(-np.maximum(k - 0.07, 0) / 0.01) * (k > 0.07))
    from scipy.signal import lfilter
    return (lfilter([1, -0.9], [1], x) * 0.35).astype(np.float32)


def sfx_whoosh():
    from scipy.signal import lfilter
    rng = np.random.default_rng(4); k = np.arange(int(0.7 * SR)) / SR
    env = np.sin(np.pi * np.clip(k / 0.7, 0, 1)) ** 2
    x = lfilter([0.06], [1, -0.94], rng.normal(0, 1, len(k))) * env
    return (x / (np.abs(x).max() + 1e-9) * 0.5).astype(np.float32)


def sfx_sting():
    """채널 신호음(직접 작곡·합성, 약 3초): 거꾸로 빨려 드는 소리 → 1.45초에 낮은 '쿵' + D단조 종소리 화음"""
    from scipy.signal import lfilter
    rng = np.random.default_rng(21); n = int(3.4 * SR); t = np.arange(n) / SR; y = np.zeros(n)
    sw = int(1.45 * SR); k = np.arange(sw) / SR                 # 1) 빨려 드는 소리(잡음 + 높아지는 음)
    rise = (k / 1.45) ** 2.6
    noise = lfilter([0.05], [1, -0.95], rng.normal(0, 1, sw))
    tone = sum(np.sin(2 * np.pi * np.cumsum(f0 * (0.7 + 0.3 * k / 1.45)) / SR) for f0 in (146.83, 220.0, 293.66))
    y[:sw] += (noise / (np.abs(noise).max() + 1e-9) * 0.5 + tone * 0.18) * rise
    b = sfx_boom(); s0 = sw; y[s0:s0 + len(b)] += b[:n - s0] * 1.1   # 2) 쿵
    kk = np.arange(n - s0) / SR                                   # 3) 종소리 화음(비정수 배음으로 금속성)
    bell = np.zeros(n - s0)
    for f0, a in ((293.66, 1.0), (349.23, 0.7), (440.0, 0.6), (587.33, 0.45)):
        for mlt, am, dec in ((1, 1, 1.6), (2.76, 0.35, 0.6), (5.4, 0.18, 0.25)):
            bell += a * am * np.sin(2 * np.pi * f0 * mlt * kk) * np.exp(-kk / dec)
    y[s0:] += reverb(bell * np.minimum(kk / 0.004, 1), 2.6, 0.45) * 0.22
    y *= np.minimum((n - np.arange(n)) / (0.4 * SR), 1)
    return (y / (np.abs(y).max() + 1e-9) * 0.9).astype(np.float32)


def build_audio(tl, T):
    n = int(T * SR) + SR
    nar = np.zeros(n, np.float32)
    for sc in tl:
        for L in sc["lines"]:
            x = read_wav(TTS / f"{sc['s']['id']}_{L['i']}.wav"); s0 = int(L["start"] * SR)
            nar[s0:s0 + len(x)] += x[:n - s0]
    fx = np.zeros(n, np.float32)

    def put(x, t, g):
        s0 = int(t * SR); fx[s0:s0 + len(x)] += x[:n - s0] * g
    boom = sfx_boom()
    intro = getattr(plan, "INTRO", None)
    if intro:
        put(sfx_sting(), 0.0, 0.75)                           # 채널 신호음
    else:
        put(boom, 0.05, 0.55)
    sh, wh = sfx_shutter(), sfx_whoosh()
    if getattr(plan, "TVOFF", False):
        put(sfx_tvoff(), T - TVOFF_DUR, 0.8)
    for sc in tl:                                          # 엔딩 버튼 클릭 소리(의학의 역사와 같은 click.wav)
        if sc["s"].get("endcard"):
            ck = read_wav(CH / "click.wav")
            _, t_like, t_sub = endcard_times(sc)
            put(ck, sc["start"] + t_like, 0.9); put(ck, sc["start"] + t_sub, 0.9)
    for sc in tl:
        if sc["s"].get("missing"):
            put(boom, sc["start"] + 0.3, 0.5)
    for sc in tl[1:]:
        if sc["s"].get("photo"):
            put(sh, sc["start"], 0.5)
        elif (W / "anim" / f"{sc['s']['id']}_omni.mp4").exists():
            put(wh, max(sc["start"] - 0.35, 0), 0.35)
    for sc in tl:
        for L in sc["lines"]:
            if L["q"]:
                put(boom, L["start"] - QPAD, 0.28)
        for text, kind, li in sc["s"].get("ov", []):
            put(boom, sc["lines"][li]["start"], 0.7)
        if sc["s"]["id"] == "c05":
            tk = sfx_tick()
            for j in range(int(sc["end"] - sc["start"])):
                put(tk, sc["start"] + j + 0.2, 0.35)
    music = bgm(n / SR)
    rms = lambda v: float(np.sqrt(np.mean(v[np.abs(v) > 1e-4] ** 2)) + 1e-9)
    music *= 0.085 * rms(nar) / rms(music)                    # 나레보다 약 21dB 낮게
    # 나레가 나올 때 음악을 살짝 더 줄인다(덕킹)
    on = (np.abs(nar) > 0.01).astype(np.float64); win = SR // 4         # 0.25초 이동평균(누적합 — np.convolve 는 수천만 번 곱이라 10분 넘게 걸렸다)
    cs = np.concatenate([[0], np.cumsum(on)])
    idx = np.arange(n); lo = np.clip(idx - win // 2, 0, n); hi = np.clip(idx + win // 2, 0, n)
    env = ((cs[hi] - cs[lo]) / win).astype(np.float32)
    music *= (1 - 0.35 * np.clip(env * 3, 0, 1))
    if intro and intro.get("through"):                         # 그노시엔느를 끝까지(2026-10-02 사용자 "인트로 음악이 끝날 때까지") — 합성 배경음악은 뺀다
        ids = [sc["s"]["id"] for sc in tl]
        t_end = tl[ids.index(intro["end_scene"]) + 1]["start"] if intro["end_scene"] in ids[:-1] else 60.0
        at = int(intro.get("at", 1.5) * SR); need = n - at; xf = int(2.5 * SR)
        tracks = [read_wav(CH / m).astype(np.float32) for m in intro["music_list"]]
        tracks = [t_ / rms(t_) for t_ in tracks]                # 곡마다 크기 맞춤
        bed = np.zeros(0, np.float32); k = 0
        while len(bed) < need:                                  # 차례로 잇고, 모자라면 처음 곡부터 다시 — 이음새는 2.5초 겹침
            t_ = tracks[k % len(tracks)]; k += 1
            if len(bed) == 0:
                bed = t_.copy(); continue
            ramp = np.linspace(0, 1, xf, dtype=np.float32)
            bed[-xf:] = bed[-xf:] * (1 - ramp) + t_[:xf] * ramp
            bed = np.concatenate([bed, t_[xf:]])
        bed = bed[:need]
        tt_ = np.arange(need) / SR + at / SR
        T_end = n / SR - SR / SR - TVOFF_DUR if getattr(plan, "TVOFF", False) else n / SR - 1.0
        g = np.where(tt_ < t_end, intro.get("gain", 0.22), intro.get("body_gain", 0.16)).astype(np.float32)
        ramp_b = np.clip((tt_ - t_end) / 2.0, 0, 1); g = intro.get("gain", 0.22) * (1 - ramp_b) + intro.get("body_gain", 0.16) * ramp_b
        env_in = np.minimum((tt_ - at / SR) / 0.8, 1)
        env_out = np.clip((T_end + 0.4 - tt_) / 2.5, 0, 1)
        lay = np.zeros(n, np.float32); lay[at:] = bed * g * env_in * env_out * rms(nar)
        lay *= (1 - 0.25 * np.clip(env * 3, 0, 1))
        music = lay
        put(boom, t_end - 0.05, 0.45)                          # 본론으로 넘어가는 '쿵'(조금 작게)
    elif intro:                                                # 도입부 음악(원래 채널처럼 진하게) → 본론에서 평소 배경음악으로
        ids = [sc["s"]["id"] for sc in tl]
        t_end = tl[ids.index(intro["end_scene"]) + 1]["start"] if intro["end_scene"] in ids[:-1] else 60.0
        im_ = read_wav(CH / intro["music"]); off = int(intro.get("offset", 0) * SR)
        at = int(intro.get("at", 1.5) * SR); L_ = min(len(im_) - off, int((t_end + 1.0) * SR) - at, n - at)
        seg = im_[off:off + L_].astype(np.float32).copy()
        tt_ = np.arange(L_) / SR
        seg *= np.minimum(tt_ / 0.8, 1) * np.clip((t_end + 0.9 - (at / SR + tt_)) / 1.6, 0, 1)
        lay = np.zeros(n, np.float32); lay[at:at + L_] = seg
        lay *= intro.get("gain", 0.2) * rms(nar) / rms(seg)
        lay *= (1 - 0.25 * np.clip(env * 3, 0, 1))
        music *= np.clip((np.arange(n) / SR - (t_end - 0.4)) / 2.0, 0, 1)   # 평소 배경음악은 본론부터
        music += lay
        put(boom, t_end - 0.05, 0.6)                           # 본론으로 넘어가는 '쿵'
    mix = nar + music + fx
    raw = W / f"{OUTNAME}_mix_raw.wav"
    import wave
    st = np.clip(np.stack([mix, mix], 1), -1, 1)
    with wave.open(str(raw), "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((st * 32767).astype(np.int16).tobytes())
    m = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(raw), "-af", "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"],
                       capture_output=True, text=True, encoding="utf-8", errors="ignore").stderr
    j = json.loads(m[m.rindex("{"):m.rindex("}") + 1])
    out = W / f"{OUTNAME}_mix.wav"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(raw), "-af",
                    f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={j['input_i']}:measured_TP={j['input_tp']}:measured_LRA={j['input_lra']}:"
                    f"measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true", "-ar", str(SR), str(out)], check=True)
    return out


# ── 조립 ────────────────────────────────────────────────
def render(tl, ev, T):
    caps = {} if getattr(plan, "NOCAP", False) else {sc["s"]["id"]: label_img(sc["s"]["cap"]) for sc in tl if sc["s"].get("cap")}   # NOCAP: 왼쪽 위 출처 표시 없음(2026-10-03 사용자)
    names = {sc["s"]["id"]: name_img(*sc["s"]["name"]) for sc in tl if sc["s"].get("name")}
    qcards = {sc["s"]["id"]: qcard_img(sc["s"]["lines"][0][0] if isinstance(sc["s"]["lines"][0], tuple) else sc["lines"][0]["text"]) for sc in tl if sc["s"].get("qcard")}   # 실제 사진 장면만 날짜·설명 (AI 표시는 사용자 요청으로 없앰)
    subs = [(a, b, sub_img(t)) for a, b, t in ev]
    quotes = []
    for sc in tl:
        for L in sc["lines"]:
            if L["q"]:
                q, h = quote_img(L["text"])
                quotes.append((L["start"] - QPAD + 0.05, L["end"] + QPAD, q, h))
    stats = []
    for sc in tl:
        for text, kind, li in sc["s"].get("ov", []):
            stats.append((sc["lines"][li]["start"], sc["end"], stat_img(text)))
    vid = W / f"{OUTNAME}_video.mp4"
    p = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{VW}x{VH}", "-r", str(FPS), "-i", "-",
                          "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p", str(vid)], stdin=subprocess.PIPE)
    nf = int(T * FPS)
    k, cache = 0, {}
    prev_k, fade_src, last_raw, XFADE = 0, None, None, 0.35
    band_x, band_y = (VW - paper_band().width) // 2, VH - paper_band().height - 26
    si = 0
    for fi in range(nf):
        t = fi / FPS
        while k < len(tl) - 1 and t >= tl[k]["end"]:
            k += 1
        sc = tl[k]
        sid = sc["s"]["id"]; d = sc["end"] - sc["start"]; tt = t - sc["start"]
        if sid not in cache:
            av = W / "anim" / f"{sid}_omni.mp4"
            if sc["s"].get("foot"):
                cache = {sid: None, "anim": Foot(sc["s"]["foot"], sc["s"].get("t0", 0))}
            else:
                cache = {sid: base_image(sid), "anim": Anim(av, d) if av.exists() and not sc["s"].get("photo") else None}
        base = cache[sid]
        if sc["s"].get("hl"):                                 # 빨간 동그라미(원본 사진 좌표)
            base = base.copy(); px, py, fs = PLACE[sc["s"]["photo"]]
            for x0, y0, x1, y1, dl in sc["s"]["hl"]:
                if tt > dl:
                    draw_circle(base, (px + x0 * fs, py + y0 * fs, px + x1 * fs, py + y1 * fs), (tt - dl) / 0.6)
        z, dx, dy = motion(k, tt / d, d)
        if sc["s"].get("photo") and tt < 0.4:                # 사진이 툭 들어오기
            e = 1 - (1 - tt / 0.4) ** 3
            z *= 1 + 0.07 * (1 - e)
        af = cache["anim"].frame(tt) if cache.get("anim") else None
        fr = af.copy() if af is not None else warp(base, z, dx, dy)
        if k != prev_k:                                       # 장면이 바뀌면 앞 장면 마지막 화면에서 0.35초 겹쳐 넘어간다
            fade_src, prev_k = last_raw, k
        if fade_src is not None and tt < XFADE:
            a_ = tt / XFADE; fr = cv2.addWeighted(fr, a_, fade_src, 1 - a_, 0)
        last_raw = fr
        if sc["s"].get("foot") and af is not None:            # 기록 영상은 아주 살짝만 다가가기
            fr = warp(fr, 1.0 + 0.004 * tt, 0, 0)
        if getattr(plan, "GRADE", False) and not sc["s"].get("photo") and not sc["s"].get("foot") and not str(sc["s"].get("use", "")).startswith("cards/"):
            fr = film(fr, fi)                                     # 기록물 필터: 재연 그림에도 필름 결·긁힘
        if sc["s"].get("missing"):                                # 실종: 빨간 화면 + MISSING 도장 쾅
            fr = red_tint(fr)
            if tt > 0.15:
                u = min((tt - 0.15) / 0.22, 1); sc_ = 1.0 + 0.8 * (1 - u) ** 2
                st = stamp_img(); w_, h_ = int(st.width * 0.62 * sc_), int(st.height * 0.62 * sc_)
                col, al = rgba(st.resize((w_, h_), Image.LANCZOS))
                blend(fr, (col, al * min(u * 1.6, 1) * 0.92), VW // 2 - w_ // 2 + 120, int(VH * 0.40) - h_ // 2)
        if sc["s"].get("qcard"):                                  # 인용문 카드: 어둡게 + 흰·빨강 큰 글자
            fr = cv2.convertScaleAbs(cv2.GaussianBlur(fr, (0, 0), 6), alpha=0.42)
            (qc, qa_), qh = qcards[sc["s"]["id"]]
            u = min(tt / 0.35, 1)
            blend(fr, (qc, qa_ * u), 0, int(VH * 0.45 - qh / 2))
        if sc["s"]["id"] in names and tt > 0.3:                   # 이름 라벨
            col, al = names[sc["s"]["id"]]; u = min((tt - 0.3) / 0.3, 1)
            blend(fr, (col, al * u), 70 - int(40 * (1 - u)), VH - 360)
        if getattr(plan, "GRADE", False) and not sc["s"].get("foot") and not str(sc["s"].get("use", "")).startswith("cards/") and not sc["s"].get("qcard"):
            fr = apply_leak(fr, sid, t)                           # 빛 번짐이 4초 주기로 은은하게 일렁임
        if getattr(plan, "GRADE", False) and sc["s"].get("photo"):
            fr = camcorder(fr, t)
        if sc["s"].get("photo"):
            fr = film(fr, fi)
            if tt < 2 / FPS:                                  # 셔터처럼 한 번 번쩍
                fr = cv2.addWeighted(fr, 0.55, np.full_like(fr, 255), 0.45, 0)
        if fi < 12:                                           # 첫 화면 페이드 인
            fr = cv2.convertScaleAbs(fr, alpha=fi / 12)
        if getattr(plan, "TVOFF", False):                    # 끝: TV 꺼지는 효과(자막·버튼까지 얹은 뒤에 적용 — 아래)
            pass
        elif t > T - 1.2:
            fr = cv2.convertScaleAbs(fr, alpha=max(0, (T - t) / 1.2))
        if sc["s"].get("blur"):                              # 엔딩: 배경 흐리고 어둡게
            fr = cv2.convertScaleAbs(cv2.GaussianBlur(fr, (0, 0), 16), alpha=0.6)
        if sc["s"].get("endcard"):
            fr = endcard_frame(fr, tt, sc)
        if sc["s"]["id"] in caps:
            blend(fr, caps[sc["s"]["id"]], 36, 32)
        qa = [q for q in quotes if q[0] <= t < q[1]]
        if qa:
            a, b, q, h = qa[0]
            u = min((t - a) / 0.25, (b - t) / 0.25, 1)
            fr = cv2.convertScaleAbs(fr, alpha=1 - 0.5 * u)
            col, al = q
            blend(fr, (col, al * u), 0, int(VH * 0.47 - h / 2))
        for a, b, s in stats:
            if a <= t < b:
                u = min((t - a) / 0.2, 1)
                blend(fr, (s[0], s[1] * u), 0, int(VH * 0.40))
        while si < len(subs) and subs[si][1] <= t:
            si += 1
        if si < len(subs) and subs[si][0] <= t < subs[si][1] and not qa and not sc["s"].get("qcard"):
            blend(fr, subs[si][2], band_x, band_y)
        if getattr(plan, "TVOFF", False) and t >= T - TVOFF_DUR:
            fr = tv_off(fr, (t - (T - TVOFF_DUR)) / TVOFF_DUR)
        p.stdin.write(fr.tobytes())
        if fi % 900 == 0:
            print(f"frame {fi}/{nf}", flush=True)
    p.stdin.close(); p.wait()
    return vid


if __name__ == "__main__":
    tl = timeline()
    T = tl[-1]["end"]
    print(f"장면 {len(tl)} 길이 {T:.1f}s")
    ev = sub_events(tl); print("자막", len(ev))
    aud = build_audio(tl, T); print("오디오", aud.name)
    vid = render(tl, ev, T)
    out = W / f"{OUTNAME}.mp4"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(vid), "-i", str(aud), "-map", "0:v", "-map", "1:a", "-c:v", "copy",
                    "-c:a", "aac", "-b:a", "256k", "-movflags", "+faststart", "-shortest", str(out)], check=True)
    json.dump([[round(sc["start"], 2), round(sc["end"], 2), sc["s"]["id"]] for sc in tl], open(W / f"{OUTNAME}_tl.json", "w"))
    print("완료", out)
