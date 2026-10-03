---
name: rama-preset-workflow
description: rama-preset(라마) = ~/rama-preset(git) + ~/rama_work 작업 폴더. 포레이로 엔진에서 2026-09-18 갈라낸 드라마 숏폼 프리셋 — 엘플릭스 템플릿 + 상황 설명 나레. drama-preset과 절대 섞지 않는다
metadata: 
  node_type: memory
  type: project
  originSessionId: 5dcc0232-5905-41e7-8b50-71a21830d1aa
  modified: 2026-09-18T09:14:37.842Z
---

"rama-preset" / "라마 프리셋" = 저장소 `~/rama-preset`(로컬 git, 2026-09-18 생성, GitHub 미푸시) + 작업 폴더 `~/rama_work`(엔진 `presets/라마`, 완성본 `rama_work/라마/`).
사용자 지시: **"기존 프리셋(drama-preset)이랑 절대 겹치면 안 돼"** → 폴더·채널명·완성본 폴더 전부 별도. 지침은 `~/rama_work/CLAUDE.md` → `docs/라마-지침서.md`.

- 다른 것: ①템플릿 = 유튜브 쇼츠 GMDwCzB1mBI(엘플릭스) 실측 — 잘난체 2 제목 흰/빨강(#F70102), 그림 1080×1086 y416, 자막 Gmarket Sans Bold 잉크 60 y1393, 아래 띠에 작품 로고 PNG(`episode.LOGO`, build.py 가 얹음)
  ②나레 = **상황 설명 한 문장**(~죠/~는데/~은), 물음표 나레(「~은?」「~데?」) 금지(사용자 09-18 "그냥 상황 설명"), 마지막만 반말 촌평. `|` 덩이 = 컷. build.py 가 물음표·본문 `~다` 를 막는다
  ③세로 쇼츠 편집본 소재: prep.py 가 그림 칸만 자동으로 오림, 남의 나레 음성은 `scripts/mute_vocals.py`(demucs, 시스템 python311) 로 지움
- 목소리는 포레이로와 같은 "드라마" `uc_6aa8eb42…` 1.3배(Junho 로 바꿨다가 사용자가 되돌림). venv·API 키 공유.
- 첫 편 `examples/sb01_신병4_해병보고`(신병4, 남의 채널 편집본 6wbyVBP1idI — 올릴 땐 권한 확인). 완성 52.9초.
- 벤치 `docs/벤치-라마의드라마-나레분석-20260918.md` 는 참고용 — 그 채널의 「~데?」 말투는 사용자가 뺐다.

**How to apply:** 라마 편은 `~/rama_work` 에서 `presets/라마` 로만 굽고 `~/rama-preset` 에만 커밋한다. 포레이로 문서·examples 를 끌어오지 않는다. [[forey-preset-workflow]] [[proceed-without-asking]]
