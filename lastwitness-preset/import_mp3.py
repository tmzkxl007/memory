# 마지막 목격자 — 사용자가 준 나레이션 mp3 를 대본 줄마다 잘라 tts 폴더로(2026-10-02 사용자 "tts는 내가 따로 mp3파일을 줄께")
# python import_mp3.py <편 폴더> <나레이션.mp3> [LW_PLAN 모듈]
#   1) Speechmatics 로 받아쓰기(낱말마다 시각)  2) 대본 글자와 받아쓴 글자를 맞춰 줄마다 시작·끝 시각을 찾는다
#   3) 줄 사이 쉼의 가운데에서 잘라 <TTS_DIR>/<장면>_<줄>.wav (48kHz mono, 앞뒤 무음 0.04초 남김) + durations.json
#   → 그다음은 평소처럼 build.py (줄 사이 간격은 build 가 일정하게 다시 맞춘다)
import difflib, json, os, re, subprocess, sys, time, uuid, urllib.request, importlib
from pathlib import Path

EP = Path(sys.argv[1]).resolve(); MP3 = Path(sys.argv[2]).resolve()
sys.path.insert(0, str(EP)); plan = importlib.import_module(sys.argv[3] if len(sys.argv) > 3 else os.environ.get("LW_PLAN", "plan"))
OUT = EP / getattr(plan, "TTS_DIR", "tts"); OUT.mkdir(exist_ok=True)
KEY = open(os.path.expanduser("~/.volcano/keys/speechmatics"), encoding="utf-8").read().strip()
BASE = "https://asr.api.speechmatics.com/v2"
SR = 48000


def req(url, data=None, headers=None, method=None):
    r = urllib.request.Request(url, data=data, method=method, headers={"Authorization": f"Bearer {KEY}", **(headers or {})})
    with urllib.request.urlopen(r, timeout=600) as x:
        return x.read()


def transcribe(path):
    cache = path.with_suffix(".asr.json")
    if cache.exists():
        return json.load(open(cache, encoding="utf-8"))
    wav = path.with_suffix(".16k.wav")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(path), "-ac", "1", "-ar", "16000", str(wav)], check=True)
    b = uuid.uuid4().hex
    cfg = json.dumps({"type": "transcription", "transcription_config": {"language": "ko", "operating_point": "enhanced"}})
    body = (f"--{b}\r\nContent-Disposition: form-data; name=\"config\"\r\n\r\n{cfg}\r\n--{b}\r\n"
            f"Content-Disposition: form-data; name=\"data_file\"; filename=\"a.wav\"\r\nContent-Type: audio/wav\r\n\r\n").encode() + wav.read_bytes() + f"\r\n--{b}--\r\n".encode()
    job = json.loads(req(f"{BASE}/jobs", body, {"Content-Type": f"multipart/form-data; boundary={b}"}, "POST"))["id"]
    while True:
        time.sleep(5)
        st = json.loads(req(f"{BASE}/jobs/{job}"))["job"]["status"]
        if st == "done":
            break
        if st in ("rejected", "deleted", "expired"):
            raise RuntimeError(st)
    res = json.loads(req(f"{BASE}/jobs/{job}/transcript?format=json-v2"))
    json.dump(res, open(cache, "w", encoding="utf-8"), ensure_ascii=False)
    return res


def sino(n):
    """정수 → 한자어 수 읽기(1955 → 천구백오십오)"""
    if n == 0:
        return "영"
    d = "일이삼사오육칠팔구"; out = ""
    for unit, name in ((10 ** 8, "억"), (10 ** 4, "만")):
        if n >= unit:
            out += sino(n // unit) + name; n %= unit
    for unit, name in ((1000, "천"), (100, "백"), (10, "십"), (1, "")):
        q = n // unit; n %= unit
        if q:
            out += ("" if q == 1 and unit > 1 else d[q - 1]) + name
    return out


def norm(s):
    """맞추기용 글자: 숫자는 읽는 소리로(대본 1955 와 받아쓰기 '천구백오십오'/'1955' 를 같게), 문장부호·공백 제거"""
    s = re.sub(r"\d+", lambda m: sino(int(m.group(0))), s)
    return re.sub(r"[^가-힣a-zA-Z]", "", s)


res = transcribe(MP3)
# 받아쓴 글자 하나하나에 시각을 붙인다(낱말 안에서는 고르게 나눔)
chars, times = [], []
for r in res["results"]:
    if r.get("type") != "word":
        continue
    w = norm(r["alternatives"][0]["content"]); a, e = r["start_time"], r["end_time"]
    for k, ch in enumerate(w):
        chars.append(ch); times.append((a + (e - a) * k / max(len(w), 1), a + (e - a) * (k + 1) / max(len(w), 1)))
asr = "".join(chars)

lines = [(s["id"], i, L[0]) for s in plan.SCENES for i, L in enumerate(s["lines"])]
# 대본 숫자는 읽는 소리로 바꿔 맞춘다(norm)
script = ""; owner = []
for k, (_, _, t) in enumerate(lines):
    t = norm(t)
    script += t; owner += [k] * len(t)
sm = difflib.SequenceMatcher(None, script, asr, autojunk=False)
s2a = {}
for a, b, n in sm.get_matching_blocks():
    for j in range(n):
        s2a[a + j] = b + j
spans = []
for k in range(len(lines)):
    idx = [s2a[i] for i in range(len(script)) if owner[i] == k and i in s2a]
    spans.append((times[min(idx)][0], times[max(idx)][1]) if idx else None)
# 못 맞춘 줄은 앞뒤 사이로 채운다
for k, sp in enumerate(spans):
    if sp is None:
        prev = next((spans[j][1] for j in range(k - 1, -1, -1) if spans[j]), 0.0)
        nxt = next((spans[j][0] for j in range(k + 1, len(spans)) if spans[j]), prev + 2.0)
        spans[k] = (prev, nxt); print("맞추기 실패 → 앞뒤 사이로:", lines[k][0], lines[k][1], lines[k][2][:30])
total = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(MP3)], capture_output=True, text=True).stdout)
cuts = [max(0.0, spans[0][0] - 0.25)]
for (a1, e1), (a2, e2) in zip(spans, spans[1:]):
    cuts.append((e1 + a2) / 2)                          # 쉼의 가운데에서 자른다
cuts.append(min(total, spans[-1][1] + 0.35))
dur = json.load(open(OUT / "durations.json")) if (OUT / "durations.json").exists() else {}   # 추가 녹음이면 기존 줄 기록은 그대로 두고 합친다
for k, (sid, i, _) in enumerate(lines):
    wav = OUT / f"{sid}_{i}.wav"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", f"{cuts[k]:.3f}", "-to", f"{cuts[k + 1]:.3f}", "-i", str(MP3), "-af",
                    "silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.04,areverse,"
                    "silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.04,areverse",
                    "-ar", str(SR), "-ac", "1", str(wav)], check=True)
    d = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(wav)], capture_output=True, text=True).stdout)
    dur[f"{sid}_{i}"] = round(d, 3)
json.dump(dur, open(OUT / "durations.json", "w"), indent=0)
ratio = sm.ratio()
said = sum(dur[f"{a}_{b}"] for a, b, _ in lines)
print(f"줄 {len(lines)}개 잘라 냄(전체 기록 {len(dur)}줄) → {OUT}  (대본·받아쓰기 일치율 {ratio:.1%}, 말소리 합 {said:.1f}s / mp3 {total:.1f}s)")
