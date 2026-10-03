# 3편 목격자 증언 카드(직접 디자인): 누런 1888년 증언 기록 서류 느낌 — w1~w4 + 비교 카드
import numpy as np
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps
W = Path(__file__).parent
F = W.parent / "fonts"
BH, GB, GD = str(F / "BlackHanSans-Regular.ttf"), str(F / "GothicA1-Black.ttf"), str(F / "GothicA1-Bold.ttf")
VW, VH = 1920, 1080
INK, RED = (40, 30, 22), (168, 30, 28)


def paper(seed):
    rng = np.random.default_rng(seed)
    base = np.full((VH, VW, 3), (214, 196, 160), np.float32)
    n = rng.normal(0, 1, (VH // 6, VW // 6)).astype(np.float32)
    n = np.array(Image.fromarray(((n - n.min()) / np.ptp(n) * 255).astype(np.uint8)).resize((VW, VH), Image.BICUBIC)).astype(np.float32) / 255
    base *= (0.82 + 0.25 * n)[..., None]
    base += rng.normal(0, 6, (VH, VW, 1))
    yy, xx = np.mgrid[0:VH, 0:VW].astype(np.float32)
    r = np.sqrt(((xx - VW / 2) / (VW / 2)) ** 2 + ((yy - VH / 2) / (VH / 2)) ** 2)
    base *= np.clip(1.08 - 0.42 * r ** 2, 0.45, 1)[..., None]
    return Image.fromarray(np.clip(base, 0, 255).astype(np.uint8))


def witness(out, seed, no, name, when, where, saw, photo=None):
    im = paper(seed); d = ImageDraw.Draw(im)
    d.text((140, 120), f"목격자 증언 · {no}", font=ImageFont.truetype(GD, 44), fill=INK)
    d.line((140, 180, VW - 140, 180), fill=INK, width=4)
    x0 = 140
    if photo:
        ph = ImageOps.grayscale(Image.open(photo)).convert("RGB")
        ph.thumbnail((560, 420))                                  # 단체 사진이라 자르지 않고 통째로(누가 라웬드인지 표시 없음)
        ph = Image.blend(ph, Image.new("RGB", ph.size, (196, 170, 130)), 0.25)
        im.paste(ph, (140, 250)); d.rectangle((140, 250, 140 + ph.width, 250 + ph.height), outline=INK, width=4)
        d.text((140, 250 + ph.height + 20), "조지프 라웬드가 있는 가족 사진 (1899)", font=ImageFont.truetype(GD, 30), fill=(90, 70, 50))
        x0 = 140 + ph.width + 70
    d.text((x0, 230), name, font=ImageFont.truetype(BH, 120), fill=INK)
    d.text((x0, 390), when, font=ImageFont.truetype(GB, 52), fill=RED)
    d.text((x0, 460), where, font=ImageFont.truetype(GD, 46), fill=INK)
    d.text((x0, 570), "그가 본 남자", font=ImageFont.truetype(GD, 40), fill=(90, 70, 50))
    y = 630
    for s in saw:
        d.text((x0, y), "·  " + s, font=ImageFont.truetype(GB, 54), fill=INK); y += 78
    # 붉은 도장(직접 그림)
    st = Image.new("RGBA", (420, 160), (0, 0, 0, 0)); ds = ImageDraw.Draw(st)
    ds.rounded_rectangle((8, 8, 412, 152), 18, outline=RED + (230,), width=10)
    ds.text((210, 82), "증언 기록", font=ImageFont.truetype(BH, 78), fill=RED + (230,), anchor="mm")
    st = st.rotate(-12, expand=True, resample=Image.BICUBIC)
    im.paste(st, (VW - 560, VH - 330), st)
    im.filter(ImageFilter.SMOOTH).save(out)


def compare(out):
    im = paper(9); d = ImageDraw.Draw(im)
    d.text((VW / 2, 120), "네 명의 목격자가 기억한 남자", font=ImageFont.truetype(BH, 84), fill=INK, anchor="mm")
    d.line((140, 190, VW - 140, 190), fill=INK, width=4)
    cols = [("엘리자베스 롱", "9.8  05:30", ["사슴 사냥 모자", "어두운 외투", "점잖은 차림"]),
            ("이즈리얼 슈워츠", "9.30  00:45", ["여성을 넘어뜨린", "거친 남자"]),
            ("조지프 라웬드", "9.30  01:35", ["서른 살쯤", "밝은 콧수염", "뱃사람 같은 차림"]),
            ("조지 허친슨", "11.9  02:00", ["잘 차려입은 신사", "털 깃 외투", "금 시곗줄"])]
    cw = (VW - 280) / 4
    for k, (nm, tm, ds_) in enumerate(cols):
        cx = 140 + cw * k + cw / 2
        # 실루엣(모자 쓴 사람 — 직접 그린 단순 도형, 얼굴 없음)
        hy = 250
        d.ellipse((cx - 70, hy + 40, cx + 70, hy + 190), fill=(60, 48, 36))
        d.rectangle((cx - 95, hy + 50, cx + 95, hy + 70), fill=(60, 48, 36)); d.rounded_rectangle((cx - 60, hy - 10, cx + 60, hy + 60), 16, fill=(60, 48, 36))
        d.pieslice((cx - 150, hy + 170, cx + 150, hy + 470), 180, 360, fill=(60, 48, 36))
        d.text((cx, hy + 210), "?", font=ImageFont.truetype(BH, 120), fill=(214, 196, 160), anchor="mm")
        d.text((cx, 610), nm, font=ImageFont.truetype(BH, 54), fill=INK, anchor="mm")
        d.text((cx, 668), tm, font=ImageFont.truetype(GB, 38), fill=RED, anchor="mm")
        for j, t in enumerate(ds_):
            d.text((cx, 728 + j * 52), t, font=ImageFont.truetype(GD, 40), fill=INK, anchor="mm")
        if k:
            d.line((140 + cw * k, 260, 140 + cw * k, 980), fill=(120, 100, 80), width=2)
    im.filter(ImageFilter.SMOOTH).save(out)


(W / "cards").mkdir(exist_ok=True)
witness(W / "cards/w1.png", 1, "1", "엘리자베스 롱", "1888년 9월 8일 새벽 5시 30분", "행버리 가 29번지 앞", ["사슴 사냥 모자", "어두운 외투", "가난하지만 점잖은 차림"])
witness(W / "cards/w2.png", 2, "2", "이즈리얼 슈워츠", "1888년 9월 30일 새벽 0시 45분", "버너 가, 더트필드 야드 입구", ["여성을 거칠게 넘어뜨린 남자", "목격자는 겁에 질려 달아남"])
witness(W / "cards/w3.png", 3, "3", "조지프 라웬드", "1888년 9월 30일 새벽 1시 35분", "마이터 광장 입구", ["서른 살쯤 · 중간 키", "밝은 콧수염 · 모자", "뱃사람 같은 차림"],
        photo=W / "archive/Joseph_Lawende_Jack_the_Ripper_Suspect_1899.jpg")
witness(W / "cards/w4.png", 4, "4", "조지 허친슨", "1888년 11월 9일 새벽 2시", "도싯 가, 밀러스 코트 근처", ["잘 차려입은 신사", "털 깃 외투 · 금 시곗줄", "사흘 뒤에야 경찰에 진술"])
compare(W / "cards/compare.png")
print("ok")
