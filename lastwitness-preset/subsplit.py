# 마지막 목격자 — 자막 16자 한 줄 나누기(넷플릭스 규격). 의학의 역사 build.py 의 같은 함수를 채널 전용으로 복사한 것
import re
NAMES = []
def split16(text):
    if len(text) > 16 and len(text.replace("'", "")) <= 16:
        text = text.replace("'", "")
    words, out, cur = text.split(), [], ""
    for w in words:
        if len(cur) + len(w) + (1 if cur else 0) <= 16:
            cur = f"{cur} {w}" if cur else w
        else:
            if cur:
                out.append(cur)
            while len(w) > 16:
                out.append(w[:16]); w = w[16:]
            cur = w
    if cur:
        out.append(cur)
    # 너무 짧은 꼬리(3자 이하)는 앞과 합칠 수 있으면 합친다
    if len(out) > 1 and len(out[-1]) <= 3 and len(out[-2]) + 1 + len(out[-1]) <= 16:
        out[-2] += " " + out.pop()
    # 그래도 꼬리가 짧으면 앞 덩어리의 마지막 단어를 넘겨 균형을 맞춘다
    while len(out) > 1 and len(out[-1]) <= 4 and " " in out[-2]:
        head, last = out[-2].rsplit(" ", 1)
        if len(last) + 1 + len(out[-1]) > 16:
            break
        out[-2], out[-1] = head, f"{last} {out[-1]}"
    return out


def clean(c):
    c = c.replace("...", "…").strip()
    c = re.sub(r"(?<=[가-힣])\.\s+", ", ", c)     # K3: 한 장 안 두 문장 사이는 쉼표
    c = re.sub(r"[.,]+$", "", c)
    return c


def ts(x):
    h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def wlen(s):
    """넷플릭스 한국어 규격 K1/K2 글자 수: 라틴 문자·숫자·공백·문장부호는 0.5자"""
    return sum(1.0 if ("가" <= ch <= "힣" or "ㄱ" <= ch <= "ㅣ") else 0.5 for ch in s)


_kiwi = None


def word_tags(text):
    """어절마다 (첫 형태소 품사, 끝 형태소 품사) — Kiwi 형태소 분석"""
    global _kiwi
    if _kiwi is None:
        from kiwipiepy import Kiwi
        _kiwi = Kiwi()
    spans, pos = [], 0
    for w in text.split():
        st = text.index(w, pos); spans.append((st, st + len(w))); pos = st + len(w)
    toks = _kiwi.tokenize(text)
    out = []
    for st, en in spans:
        tg = [tk.tag for tk in toks if st <= tk.start < en and tk.tag not in ("SS", "SSO", "SSC")]
        out.append((tg[0] if tg else "", tg[-1] if tg else ""))
    return out


def boundary_pen(lw, rw, ltag, rtag):
    """lw 뒤·rw 앞에서 자막을 넘길 때 벌점 (넷플릭스 General: 떼면 안 되는 자리)"""
    if lw.rstrip(",").endswith(("라는", "다는", "라던", "이란")):
        return 4                                    # 인용형 관형사('~라는 무증상 보균자')도 꾸미는 말
    if ltag[1] in ("ETM", "MM", "XPN") or (ltag[1] == "SP" and _before_comma_etm(lw)):
        return 4                                    # 관형형 뒤는 쉼표가 있어도 떼지 않는다("놓은, / 첫 기록")
    if lw.rstrip(chr(34) + chr(39)).endswith((",", "?", "!", "…")):
        return -1                                   # 문장부호 뒤 = 가장 좋은 자리
    pair = f"{lw.strip(chr(34) + chr(39))} {rw.strip(chr(34) + chr(39))}"
    if any(pair in n for n in NAMES):
        return 5                                    # 이름과 성
    if ltag[1] in ("ETM", "MM", "XPN"):
        return 4                                    # 관형형·관형사 + 꾸밈 받는 말
    if ltag[1] in ("SN", "NR") and rtag[0] in ("NNB", "SN", "NR"):
        return 4                                    # 수와 단위
    if ltag[1] in ("NNG", "NNP", "NNB") and rtag[0] in ("NNG", "NNP", "NNB"):
        return 2                                    # 명사+명사(복합어·위치명사)는 되도록 붙인다 — 금지는 아님
    return 0


def _before_comma_etm(lw):
    """'놓은,' 처럼 쉼표 앞 형태소가 관형형 어미인지"""
    w = lw.rstrip(",")
    return bool(w) and word_tags(w)[-1][1] in ("ETM", "MM")


def break_penalty(left, right):
    tg = word_tags(f"{left} {right}")
    return boundary_pen(left, right, tg[0], tg[1])


def balanced(text):
    """16자(K1 가중) 이하 덩어리로 나눈다. 점수 = (덩어리 수, 끊는 자리 벌점, 가장 긴 덩어리)"""
    if wlen(text) <= 16:
        return [text]
    words = text.split()
    n = len(words)
    tags = word_tags(text)
    pens = [0] + [boundary_pen(words[e - 1], words[e], tags[e - 1], tags[e]) for e in range(1, n)]
    best = {n: ((0, 0, 0, 0), [])}   # 점수 = (금지 자리 수, 덩어리 수, 벌점 합, 가장 긴 덩어리)
    for s in range(n - 1, -1, -1):
        cand = None
        for e in range(s + 1, n + 1):
            chunk = " ".join(words[s:e])
            if wlen(chunk) > 16:
                break
            if e in best:
                pen = pens[e] if e < n else 0
                b = best[e][0]
                sc = (b[0] + (pen >= 3), b[1] + 1, b[2] + pen, max(wlen(chunk), b[3]))
                if cand is None or sc < cand[0]:
                    cand = (sc, [chunk] + best[e][1])
        if cand:
            best[s] = cand
    return best[0][1] if 0 in best else split16(text)

