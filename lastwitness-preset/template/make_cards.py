# 4편 카드(직접 디자인, 1959년 수사 기록 서류 느낌): 대원 명단 · 가설 정리 · 공식 결론
import numpy as np
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont
W = Path(__file__).parent
F = W.parent / "fonts"
BH, GB, GD = str(F / "BlackHanSans-Regular.ttf"), str(F / "GothicA1-Black.ttf"), str(F / "GothicA1-Bold.ttf")
VW, VH = 1920, 1080
INK, RED, GREY = (40, 34, 28), (168, 30, 28), (100, 88, 74)


def paper(seed):
    rng = np.random.default_rng(seed)
    base = np.full((VH, VW, 3), (206, 200, 186), np.float32)            # 회색빛 소련 서류
    n = rng.normal(0, 1, (VH // 6, VW // 6)).astype(np.float32)
    n = np.array(Image.fromarray(((n - n.min()) / np.ptp(n) * 255).astype(np.uint8)).resize((VW, VH), Image.BICUBIC)).astype(np.float32) / 255
    base *= (0.84 + 0.22 * n)[..., None]; base += rng.normal(0, 6, (VH, VW, 1))
    yy, xx = np.mgrid[0:VH, 0:VW].astype(np.float32)
    r = np.sqrt(((xx - VW / 2) / (VW / 2)) ** 2 + ((yy - VH / 2) / (VH / 2)) ** 2)
    base *= np.clip(1.08 - 0.42 * r ** 2, 0.45, 1)[..., None]
    return Image.fromarray(np.clip(base, 0, 255).astype(np.uint8))


def stamp(im, text, x, y, ang=-12):
    st = Image.new("RGBA", (460, 160), (0, 0, 0, 0)); ds = ImageDraw.Draw(st)
    ds.rounded_rectangle((8, 8, 452, 152), 18, outline=RED + (230,), width=10)
    ds.text((230, 82), text, font=ImageFont.truetype(BH, 72), fill=RED + (230,), anchor="mm")
    st = st.rotate(ang, expand=True, resample=Image.BICUBIC); im.paste(st, (x, y), st)


def roster():
    im = paper(1); d = ImageDraw.Draw(im)
    d.text((140, 80), "1959년 1월 · 우랄 공대 디아틀로프 원정대", font=ImageFont.truetype(GD, 42), fill=INK)
    d.line((140, 140, VW - 140, 140), fill=INK, width=4)
    people = [("이고리 디아틀로프", "23세 · 대장"), ("유리 도로셴코", "21세"), ("류드밀라 두비니나", "20세"), ("게오르기 크리보니셴코", "23세"), ("알렉산드르 콜레바토프", "24세"),
              ("지나이다 콜모고로바", "22세"), ("루스템 슬로보딘", "23세"), ("니콜라이 티보브리뇰", "23세"), ("세묜 졸로타료프", "38세")]
    for k, (nm, ag) in enumerate(people):
        c, r = k % 3, k // 3
        x, y = 160 + c * 470, 190 + r * 170
        d.text((x, y), nm, font=ImageFont.truetype(BH, 50), fill=INK); d.text((x, y + 66), ag, font=ImageFont.truetype(GD, 36), fill=GREY)
    d.line((140, 715, VW - 140, 715), fill=GREY, width=2)
    d.text((160, 740), "유리 유딘", font=ImageFont.truetype(BH, 50), fill=RED); d.text((420, 752), "21세 · 1월 28일 무릎 통증으로 돌아감, 유일한 생존자", font=ImageFont.truetype(GB, 38), fill=RED)
    stamp(im, "대원 명단", VW - 440, 470, -8)
    im.filter(ImageFilter.SMOOTH).save(W / "cards/roster.png")


def theories():
    im = paper(2); d = ImageDraw.Draw(im)
    d.text((VW / 2, 110), "그날 밤에 대한 가설들", font=ImageFont.truetype(BH, 88), fill=INK, anchor="mm")
    d.line((140, 180, VW - 140, 180), fill=INK, width=4)
    items = [("눈사태", "텐트 위로 쏟아진 눈"), ("돌풍", "산 아래로 몰아친 강풍"), ("초저주파", "공포를 일으키는 소리"),
             ("군사 실험", "비밀 무기·낙하산 폭탄"), ("만시족 공격", "→ 조사로 배제", True), ("설인, 미확인 비행 물체", "괴담")]
    for k, it in enumerate(items):
        c, r = k % 2, k // 2
        x, y = 200 + c * 800, 240 + r * 220
        d.ellipse((x, y + 18, x + 26, y + 44), fill=RED if len(it) == 3 else INK)
        d.text((x + 50, y), it[0], font=ImageFont.truetype(BH, 66), fill=INK)
        d.text((x + 52, y + 92), it[1], font=ImageFont.truetype(GB, 40), fill=RED if len(it) == 3 else GREY)
        if len(it) == 3:
            w_ = d.textlength(it[0], font=ImageFont.truetype(BH, 66)); d.line((x + 46, y + 42, x + 56 + w_, y + 42), fill=RED, width=7)
    im.filter(ImageFilter.SMOOTH).save(W / "cards/theories.png")


def conclusion():
    im = paper(3); d = ImageDraw.Draw(im)
    d.text((140, 90), "공식 결론의 변화", font=ImageFont.truetype(GD, 44), fill=INK)
    d.line((140, 150, VW - 140, 150), fill=INK, width=4)
    rows = [("1959", "소련 검찰", "'저항할 수 없는 자연의 힘'", False), ("2020", "러시아 검찰 재조사", "공식 사인 = 눈사태", True),
            ("2021", "스위스 연구진 논문", "28도 비탈의 작은 눈판 붕괴로 설명 가능", False)]
    for k, (yr, who, what, hi) in enumerate(rows):
        y = 210 + k * 230
        d.text((160, y), yr, font=ImageFont.truetype(BH, 120), fill=RED)
        d.text((520, y + 10), who, font=ImageFont.truetype(GD, 40), fill=GREY)
        d.text((520, y + 70), what, font=ImageFont.truetype(BH, 64), fill=RED if hi else INK)
    stamp(im, "사건 종결?", VW - 600, 70, -10)
    im.filter(ImageFilter.SMOOTH).save(W / "cards/conclusion.png")


(W / "cards").mkdir(exist_ok=True)
roster(); theories(); conclusion()
print("ok")
