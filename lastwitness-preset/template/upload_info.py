# 마지막 목격자 4편 업로드 정보 TXT (UTF-8 BOM) — 목차 시각은 final_dy_tl.json 에서
import json
from pathlib import Path
W = Path(__file__).parent
tl = {sid: a for a, b, sid in json.load(open(W / "final_dy_tl.json"))}
src = json.load(open(W / "archive" / "sources.json", encoding="utf-8"))


def ts(x):
    return f"{int(x // 60)}:{int(x % 60):02d}"


chapters = [("a01", "텐트를 찢고 나간 아홉 명"), ("b01", "디아틀로프 원정대"), ("c01", "돌아간 한 명"), ("d01", "마지막 밤"),
            ("e01", "텅 빈 텐트"), ("f01", "소나무 아래"), ("g01", "골짜기의 네 사람"), ("h01", "수사와 결론"), ("i01", "그날 밤에 대한 가설들"), ("j01", "60년 뒤의 답")]
toc = "\n".join(f"{ts(0 if k == 0 else tl[sid])} {name}" for k, (sid, name) in enumerate(chapters))
credits = "\n".join(f"- {v['title']} ({v.get('license', '')}) {v.get('page', '')}" for k, v in src.items())

txt = f"""[제목]
'텐트를 안에서 찢고 맨발로 뛰쳐나갔다' 대학생 아홉 명이 숨진 채 발견된 소련 최대 미스터리 '디아틀로프 사건'

[다른 제목 후보]
'저항할 수 없는 자연의 힘' 60년 넘게 풀리지 않은 우랄산맥의 밤 '디아틀로프 사건'
'유일한 생존자는 돌아간 한 명뿐이었다' 영하 30도 설산의 아홉 대학생 '디아틀로프 고개 사건'

[썸네일]
썸네일A_폴리스라인_텐트를안에서찢고나갔다.jpg (폴리스라인 — 채널 기본) / 썸네일B

[설명란]
1959년 2월, 소련 우랄산맥 홀라트시아흘 비탈에서 대학생 원정대 아홉 명이 숨진 채 발견됐습니다.
텐트는 안에서 찢겨 있었고, 그들은 신발도 신지 않은 채 영하 30도의 눈밭을 1.5킬로미터나 내려갔습니다.
소련 당국의 결론은 단 한 줄, '저항할 수 없는 자연의 힘'이었습니다.

▶목차
{toc}

▶참고 자료
- 영어 위키백과 「Dyatlov Pass incident」, 1959 소련 수사 기록, 2020 러시아 검찰 발표, Gaume & Puzrin(2021) 「Communications Earth & Environment」
- 사진·지도: 위키미디어 공용 (퍼블릭 도메인 및 CC 라이선스 — 아래 저작자 표기)
{credits}

▶제작 정보
- 일부 장면은 사실을 바탕으로 AI로 만든 재연 이미지입니다.
- 음악: Erik Satie 「Gnossienne No. 1」 (연주 La Pianista, 퍼블릭 도메인, Wikimedia Commons) / 신호음: 자체 제작

[태그]
디아틀로프 사건, 디아틀로프 고개, Dyatlov Pass, 소련 미스터리, 우랄산맥, 미제사건, 눈사태, 실화, 미스터리, 마지막 목격자

[해시태그]
#디아틀로프사건 #미스터리 #마지막목격자

[고정 댓글]
여러분은 그날 밤 텐트에서 무슨 일이 있었다고 생각하시나요? 눈사태일까요, 아니면 다른 무언가였을까요?
다음에 다뤘으면 하는 사건도 댓글로 알려 주세요.

[업로드 설정 체크리스트]
- [ ] '변경되거나 합성된 콘텐츠' → 예 (실제 사건을 사실적인 AI 재연 이미지로 표현)
- [ ] 아동용 아님
- [ ] 카테고리: 교육 또는 엔터테인먼트
- [ ] 썸네일 업로드 · 고정 댓글 등록
"""
(W / "업로드정보.txt").write_text(txt, encoding="utf-8-sig")
print("ok")
