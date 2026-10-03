# 마지막 목격자 — 썸네일 (1280×720)
# 배치(원래 채널 형식): 어두운 흑백 사진 · 왼쪽 위 채널 표시 · 노란 띠 + 검은 글자 · 빨간 글자 한 줄 · 아래 흰 큰 글자
# 채널 표시는 우리 것(빨간 막대 + '마지막 목격자'), 원래 채널의 눈 로고는 쓰지 않는다
# python thumb.py <그림> <출력> "<노란 띠>" "<빨간 줄>" "<흰 큰 글자>" [초점x 0~1]
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageEnhance, ImageFont, ImageFilter, ImageOps

CH = Path(__file__).parent
BH = str(CH / "fonts" / "BlackHanSans-Regular.ttf")
TW, TH = 1280, 720


def fit(im, fx):
    sc = max(TW / im.width, TH / im.height)
    im = im.resize((round(im.width * sc), round(im.height * sc)), Image.LANCZOS)
    x = int((im.width - TW) * fx)
    return im.crop((x, (im.height - TH) // 2, x + TW, (im.height - TH) // 2 + TH))


def text_w(d, t, f):
    b = d.textbbox((0, 0), t, font=f)
    return b[2] - b[0], b


def make(src, out, yellow, red, white, fx=0.5):
    im = fit(Image.open(src).convert("RGB"), fx)
    g = ImageOps.grayscale(im).convert("RGB")
    im = Image.blend(im, g, 0.85)                                   # 거의 흑백
    im = ImageEnhance.Contrast(im).enhance(1.25)
    im = ImageEnhance.Brightness(im).enhance(0.72)
    # 아래쪽을 어둡게(큰 글자 자리)
    grad = Image.linear_gradient("L").resize((TW, TH))
    shade = Image.new("RGB", (TW, TH), (0, 0, 0))
    im = Image.composite(shade, im, grad.point(lambda v: int(max(0, v - 90) * 1.25)))
    d = ImageDraw.Draw(im)

    # 채널 표시
    lf = ImageFont.truetype(BH, 30)
    d.rectangle((26, 24, 34, 64), fill=(210, 30, 30))
    d.text((46, 44), "마지막 목격자", font=lf, fill=(240, 240, 240), anchor="lm", stroke_width=3, stroke_fill=(0, 0, 0))

    # 노란 띠
    yf = ImageFont.truetype(BH, 58)
    w, b = text_w(d, yellow, yf)
    x0, y0 = 40, 92
    d.rectangle((x0, y0, x0 + w + 36, y0 + 82), fill=(255, 214, 10))
    d.text((x0 + 18, y0 + 41), yellow, font=yf, fill=(10, 10, 10), anchor="lm")

    # 빨간 줄 + 흰 큰 글자(아래)
    wf = ImageFont.truetype(BH, 150)
    ww, wb = text_w(d, white, wf)
    if ww > TW - 60:
        wf = ImageFont.truetype(BH, int(150 * (TW - 60) / ww)); ww, wb = text_w(d, white, wf)
    rf = ImageFont.truetype(BH, 76)
    yw = TH - 30
    d.text((34, yw), white, font=wf, fill=(255, 255, 255), anchor="ls", stroke_width=6, stroke_fill=(0, 0, 0))
    yr = yw - (wb[3] - wb[1]) - 18
    d.text((38, yr), red, font=rf, fill=(235, 40, 40), anchor="ls", stroke_width=5, stroke_fill=(0, 0, 0))
    im.save(out, quality=95)
    return out


if __name__ == "__main__":
    a = sys.argv[1:]
    make(a[0], a[1], a[2], a[3], a[4], float(a[5]) if len(a) > 5 else 0.5)
    print("ok", a[1])
