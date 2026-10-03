---
name: maemmaegak-fx-pairing
description: "맴매각 효과 규칙(2026-10-01) — 반응 글씨마다 소리 자동 짝, 아픔·신남 음성 허용, 경적 차 크기별+빠아아앙 물결 글씨, 동그라미는 물체를 끊김 없이 따라감, 나레이션은 블박 차 시점"
metadata:
  node_type: memory
  type: feedback
  originSessionId: d79297c4-e980-4771-ab21-11d495f04a1b
  modified: 2026-10-01T05:02:33.513Z
---

2026-10-01 사용자가 참사이다 영상(m9hj1VlkIBk·W5_-Sj_wHWk·UCRU67qSQ7c)을 보여주며 연달아 지시한 것. pipeline `pair_fx_sounds`·`horn_text`·circle `keys`·`track` 으로 구현, SKILL.md "효과 ↔ 소리 자동 짝" 절(커밋 3fc2a7a).

- "이미지 느낌표와 물음표 효과는 음성효과랑 같이" → 반응 글씨 뜰 때 소리 자동: 퍽→9. 펀치, ?→20. 카툰 팝, !→전환 병따기 - 뽁, 나머지→8. 훅.
- "아파하고 신나하는 효과음같은 음성효과음을 … 영상 만들때 넣어줘" → 으악=scream_eoeok, 으윽=groan_eueuk, 어호호=cheer_ohoho(타입캐스트 Junho happy). **이 지시로 '사람 말소리 효과음 금지'가 좁아짐**: 아픔·신남 같은 말 아닌 반응 소리는 넣고, 대사·욕·밈("아이씨" 등)은 여전히 금지.
- "빠아아앙 하는 효과를 넣을때 적용" (인트로 아님) → 경적 넣을 때마다 주황 물결 글씨. "경적소리는 소형차와 대형차 다르니 구분" → sfx "horn": small/bike/car/truck.
- "동그라미가 움직이는 물체를 이어져서 따라가야해 끊키면 안돼" → circle keys 로 매 프레임 이동, 고정 원 이어 붙이기 금지. track 명령은 넘어짐·가림에서 틀어지니 손으로 고침.
- "나레이션은 블박차량의 입장시점에서" → 블박 차 쪽에서 본 이야기로.
- 사용자는 "알아들었으면 전체영상 말고 테스트 영상 만들어서 보여줘" — 규칙이 바뀌면 짧은 테스트 영상(episodes/_test_fx, draft)으로 먼저 보여준다.

- 다른 PC 에서 "적용이 안됐다" (2026-10-01): 자동 짝 소리가 이 PC OneDrive 폴더 파일이었고 다른 PC Claude 기억(RULES_memory.md)에 새 규칙이 없었음 → 소리 4개를 assets/sfx/fx/ 로 넣고 RULES_memory.md 17~23 추가, 커밋 05c1fdd 푸시. 새 기능에 쓰는 파일은 저장소 안에 둘 것.

**How to apply:** 새 맴매각 편은 처음부터 이 규칙으로. 관련 [[maemmaegak-style-ep04b]] [[maemmaegak-no-verdict]] [[maemmaegak-preset-workflow]] [[hanmuncheol-only-when-asked]]
