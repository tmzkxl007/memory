# 마지막 목격자 — 썸네일 2형(2026-10-02 사용자 "미스스한 이야기 채널 같은 썸네일")
# 원래 채널 형식: 실제 인물 사진 크게(오른쪽 또는 두 명 나란히) · 거의 흑백 + 거친 질감 · 왼쪽 위 채널 표시(우리 것)
#   위 연노랑 띠 + 검은 글자 · 아래 분홍빛 빨강 한 줄 · 화면 폭 흰 큰 글자(닳은 질감)
# 원래 채널의 눈 로고·문구는 쓰지 않는다.
import numpy as np
from pathlib import Path
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

CH = Path(__file__).parent
BH = str(CH / "fonts" / "BlackHanSans-Regular.ttf")
TW, TH = 1280, 720
YEL, RED = (255, 241, 84), (234, 74, 88)


def _cover(im, w, h, fx=0.5, fy=0.5):
    sc = max(w / im.width, h / im.height)
    im = im.resize((round(im.width * sc), round(im.height * sc)), Image.LANCZOS)
    x = int((im.width - w) * fx); y = int((im.height - h) * fy)
    return im.crop((x, y, x + w, y + h))


def _grade(im, color=0.12):
    g = ImageOps.grayscale(im).convert("RGB")
    im = Image.blend(g, im.convert("RGB"), color)
    im = ImageEnhance.Contrast(im).enhance(1.35)
    return im.filter(ImageFilter.UnsharpMask(2, 120, 2))


def _grunge(seed=1):
    """시멘트·긁힘 질감(0~1, 1=그대로)"""
    rng = np.random.default_rng(seed)
    n = rng.normal(0, 1, (TH // 4, TW // 4)).astype(np.float32)
    n = np.array(Image.fromarray(((n - n.min()) / (np.ptp(n) + 1e-6) * 255).astype(np.uint8)).resize((TW, TH), Image.BICUBIC)).astype(np.float32) / 255
    fine = rng.normal(0, 1, (TH, TW)).astype(np.float32) * 0.05
    m = 0.82 + 0.22 * n + fine
    for _ in range(40):                                        # 가는 긁힘
        x = int(rng.uniform(0, TW)); y0 = int(rng.uniform(0, TH)); L = int(rng.uniform(40, 260))
        m[y0:y0 + L, x:x + 1] *= rng.uniform(0.75, 1.15)
    return np.clip(m, 0.55, 1.1)[..., None]


def _distress(mask_img, seed=2, amount=0.22):
    """글자 알파에 구멍·닳음"""
    rng = np.random.default_rng(seed)
    a = np.asarray(mask_img).astype(np.float32) / 255
    n = rng.random(a.shape).astype(np.float32)
    n = np.array(Image.fromarray((n * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.2))).astype(np.float32) / 255
    a = a * np.where(n < amount * 0.55, 0.25, 1.0)
    return Image.fromarray(np.clip(a * 255, 0, 255).astype(np.uint8))


def _text_layer(text, size, fill, stroke=0, stroke_fill=(0, 0, 0), distress=0.0, seed=3):
    f = ImageFont.truetype(BH, size)
    d0 = ImageDraw.Draw(Image.new("L", (10, 10)))
    bb = d0.textbbox((0, 0), text, font=f, stroke_width=stroke)
    w, h = bb[2] - bb[0] + 20, bb[3] - bb[1] + 20
    lay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    if stroke:
        d.text((10 - bb[0], 10 - bb[1]), text, font=f, fill=stroke_fill, stroke_width=stroke, stroke_fill=stroke_fill)
    body = Image.new("L", (w, h), 0)
    ImageDraw.Draw(body).text((10 - bb[0], 10 - bb[1]), text, font=f, fill=255)
    if distress:
        body = _distress(body, seed, distress)
    lay.alpha_composite(Image.composite(Image.new("RGBA", (w, h), fill + (255,)), Image.new("RGBA", (w, h), (0, 0, 0, 0)), body))
    return lay


def _logo(im):
    d = ImageDraw.Draw(im)
    d.rectangle((24, 22, 32, 62), fill=(214, 36, 36))
    d.text((44, 42), "마지막 목격자", font=ImageFont.truetype(BH, 30), fill=(240, 240, 240), anchor="lm", stroke_width=3, stroke_fill=(0, 0, 0))


def _tape(text, size=62, h=104, angle=-4):
    """사건 현장 통제선 테이프(1편에 쓴 모양, 사용자 확정 2026-10-02): 노랑 바탕 · 위아래 검은 빗금 · 검은 글자, -4° 기울임"""
    f = ImageFont.truetype(BH, size)
    tw = ImageDraw.Draw(Image.new("L", (10, 10))).textlength(text, font=f)
    w = int(tw + 150)
    L = Image.new("RGBA", (w, h), (255, 210, 0, 255)); d = ImageDraw.Draw(L)
    for x in range(-40, w + 40, 40):
        d.polygon([(x, 0), (x + 18, 0), (x - 2, 13), (x - 20, 13)], fill=(20, 20, 20))
        d.polygon([(x, h), (x + 18, h), (x - 2, h - 13), (x - 20, h - 13)], fill=(20, 20, 20))
    d.text((70, h / 2 + 2), text, font=f, fill=(15, 15, 15), anchor="lm")
    L = L.rotate(-angle, expand=True, resample=Image.BICUBIC)
    sh = Image.new("RGBA", L.size, (0, 0, 0, 0)); sh.putalpha(L.getchannel("A").point(lambda v: int(v * 0.65)))
    return L, sh.filter(ImageFilter.GaussianBlur(9))


def _police(text, size=62, h=128, angle=-4, width=None):
    """폴리스라인 테이프(2026-10-02 사용자 요청): 노랑 바탕, 위아래 얇은 검은 선 + 작은 'POLICE LINE · DO NOT CROSS' 반복, 가운데 제목.
    text=None 이면 진짜 폴리스라인처럼 'POLICE LINE  DO NOT CROSS' 만 크게 반복(장식용). 3배로 그려 줄여 매끈하게."""
    K = 3
    fb = ImageFont.truetype(BH, size * K); fs = ImageFont.truetype(BH, 17 * K)
    tw = ImageDraw.Draw(Image.new("L", (10, 10))).textlength(text, font=fb) if text else 0
    w = (width or int(tw / K + 170)) * K; H = h * K
    L = Image.new("RGBA", (w, H), (255, 212, 0, 255)); d = ImageDraw.Draw(L)
    for y0 in (5 * K, H - 8 * K):
        d.rectangle((0, y0, w, y0 + 3 * K), fill=(18, 18, 18))
    if text:
        rep = "POLICE LINE  •  DO NOT CROSS  •  " * 12
        d.text((10 * K, 21 * K), rep, font=fs, fill=(18, 18, 18), anchor="lm")
        d.text((10 * K, H - 22 * K), rep, font=fs, fill=(18, 18, 18), anchor="lm")
        d.text((75 * K, H / 2 + 2 * K), text, font=fb, fill=(12, 12, 12), anchor="lm")
    else:
        d.text((20 * K, H / 2 + 2 * K), "POLICE LINE   DO NOT CROSS   " * 6, font=ImageFont.truetype(BH, int(h * 0.42) * K), fill=(12, 12, 12), anchor="lm")
    L = L.rotate(-angle, expand=True, resample=Image.BICUBIC)
    L = L.resize((L.width // K, L.height // K), Image.LANCZOS)
    sh = Image.new("RGBA", L.size, (0, 0, 0, 0)); sh.putalpha(L.getchannel("A").point(lambda v: int(v * 0.65)))
    return L, sh.filter(ImageFilter.GaussianBlur(9))


def _tape_flat(text, size=62, h=104, angle=0, width=None):
    """사건 현장 통제선 테이프: 노랑 바탕 · 위아래 검은 빗금 · 검은 글자.
    3배로 크게 그린 뒤 기울이고 줄여서 가장자리를 매끈하게(2026-10-02 '삐뚤빼뚤' 지적), 화면 폭 전체를 가로지른다."""
    K = 3; f = ImageFont.truetype(BH, size * K)
    w = (width or TW + 200) * K; H = h * K
    L = Image.new("RGBA", (w, H), (255, 210, 0, 255)); d = ImageDraw.Draw(L)
    band, pitch, sw = 14 * K, 44 * K, 20 * K
    for x in range(-pitch, w + pitch, pitch):
        d.polygon([(x, 0), (x + sw, 0), (x + sw - band, band), (x - band, band)], fill=(20, 20, 20))
        d.polygon([(x, H), (x + sw, H), (x + sw - band, H - band), (x - band, H - band)], fill=(20, 20, 20))
    d.text((150 * K, H / 2 + 2 * K), text, font=f, fill=(15, 15, 15), anchor="lm")
    if angle:
        L = L.rotate(angle, expand=True, resample=Image.BICUBIC)
    L = L.resize((L.width // K, L.height // K), Image.LANCZOS)
    sh = Image.new("RGBA", L.size, (0, 0, 0, 0)); sh.putalpha(L.getchannel("A").point(lambda v: int(v * 0.6)))
    return L, sh.filter(ImageFilter.GaussianBlur(9))


def make(out, yellow, red, white, bg=None, right=None, pair=None, right_fx=0.5, right_fy=0.3, seed=1, ystyle="police", tape_angle=0):   # 노란 띠 기본 = 폴리스라인(사용자 확정 2026-10-03 "썸네일은 폴리스라인으로만")
    """bg: 배경 사진(왼쪽) / right: 오른쪽 큰 인물 사진 / pair: 두 인물 사진 나란히 [(경로, fx, fy), ...]"""
    canvas = Image.new("RGB", (TW, TH), (20, 20, 20))
    if bg:
        canvas.paste(_grade(_cover(Image.open(bg).convert("RGB"), TW, TH)), (0, 0))
        canvas = ImageEnhance.Brightness(canvas).enhance(0.62)
    if right:
        pw = int(TW * 0.52)
        p = _grade(_cover(Image.open(right).convert("RGB"), pw, TH, right_fx, right_fy), 0.18)
        fade = Image.linear_gradient("L").rotate(90).resize((pw, TH))   # 왼쪽 가장자리를 배경에 녹인다
        fade = fade.point(lambda v: min(255, int((255 - v) * 3.2)))
        canvas.paste(p, (TW - pw, 0), fade)
    if pair:
        w = TW // len(pair)
        for k, (path, fx, fy) in enumerate(pair):
            p = _grade(_cover(Image.open(path).convert("RGB"), w, TH, fx, fy), 0.18)
            canvas.paste(p, (k * w, 0))
            ImageDraw.Draw(canvas).line([(k * w, 0), (k * w, TH)], fill=(10, 10, 10), width=6)
    a = np.asarray(canvas).astype(np.float32) * _grunge(seed)
    yy, xx = np.mgrid[0:TH, 0:TW].astype(np.float32)
    vig = 1 - 0.45 * np.clip(np.sqrt(((xx - TW / 2) / (TW / 2)) ** 2 + ((yy - TH / 2) / (TH / 2)) ** 2) - 0.6, 0, None)
    bottom = 1 - 0.75 * np.clip((yy - TH * 0.48) / (TH * 0.52), 0, 1) ** 1.3       # 아래쪽 어둡게(큰 글자 자리)
    a = a * vig[..., None] * bottom[..., None]
    im = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).convert("RGBA")

    _logo(im)
    # 노란 띠 — ystyle="tape" 면 사건 현장 통제선 테이프(2026-10-02 사용자 요청)
    f = ImageFont.truetype(BH, 60)
    d = ImageDraw.Draw(im)
    lines = yellow.split("\n") if ystyle == "box" else []   # 테이프·폴리스라인이면 노란 상자는 그리지 않는다
    if ystyle == "tape":
        tp, sh = _tape(yellow.replace("\n", " "))
        im.alpha_composite(sh, (-32, 82)); im.alpha_composite(tp, (-40, 70))
    if ystyle.startswith("police"):                              # 폴리스라인(같은 자리·같은 기울기)
        if ystyle == "police_x":                                  # 장식 테이프 한 줄을 오른쪽 위에 X 로 걸침
            dt, dsh = _police(None, h=70, angle=24, width=900)
            im.alpha_composite(dsh, (TW - dt.width + 260 + 8, -150 + 10)); im.alpha_composite(dt, (TW - dt.width + 260, -150))
        tp, sh = _police(yellow.replace(chr(10), " "))
        im.alpha_composite(sh, (-32, 72)); im.alpha_composite(tp, (-40, 60))
    y = 92
    for ln in lines:
        tw = d.textlength(ln, font=f)
        d.rectangle((54, y, 54 + tw + 34, y + 76), fill=YEL)
        d.text((54 + 17, y + 38), ln, font=f, fill=(12, 12, 12), anchor="lm")
        y += 76
    # 흰 큰 글자(화면 폭에 맞춤) + 빨간 줄
    size = 178
    wl = _text_layer(white, size, (246, 246, 246), 7, (0, 0, 0), 0.22, seed + 5)
    if wl.width > TW - 30:
        size = int(size * (TW - 30) / wl.width); wl = _text_layer(white, size, (246, 246, 246), 7, (0, 0, 0), 0.22, seed + 5)
    im.alpha_composite(wl, (8, TH - wl.height + 6))
    rl = _text_layer(red, 84, RED, 5, (20, 0, 0), 0.12, seed + 7)
    if rl.width > TW - 30:
        rl = rl.resize((TW - 30, int(rl.height * (TW - 30) / rl.width)), Image.LANCZOS)
    im.alpha_composite(rl, (10, TH - wl.height - rl.height + 22))
    im.convert("RGB").save(out, quality=95)
    return out
