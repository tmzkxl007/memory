---
name: hanmuncheol-only-when-asked
description: "한문철 본인 장면·판정 음성은 사용자가 그 편에 넣으라고 말할 때만 넣는다 (2026-10-01, ep07 에 넣었다가 지적받음)"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 950b9c7d-43f8-4014-ba87-f0fbdb5ebf1e
  modified: 2026-10-01T04:14:05.155Z
---

한문철 본인 장면(방송 화면·판정 음성·"한변호사>>" 자막)은 **사용자가 그 편에 넣으라고 말할 때만** 넣는다. 한문철TV 소재라고 자동으로 넣지 않는다. 말이 없으면 판정은 나레이션 팩트 한 줄로 전한다.

**Why:** 사용자 "내가 말할때만 한문철을 넣으라고 했는데 넣었네?" (2026-10-01). ep05 때 "한문철 변호사 판정 장면이 들어갔으면 좋겠어"는 그 편만의 요청이었는데, SKILL.md 사고형 공식 B 7번이 "한문철 본인 2초"를 기본 단계로 적고 있어서 ep07 세션이 자동으로 넣었다. → ep07 에서 HAN 삭제(커밋 cadade2, 18.3초), SKILL 7번을 "사용자가 말할 때만"으로 고침.

**How to apply:** 맴매각 등 블박 쇼츠 만들 때 한문철 장면은 요청이 있을 때만. 한 편의 요청을 다음 편 기본값으로 넓히지 않는다. 관련 [[maemmaegak-preset-workflow]] [[maemmaegak-style-ep04b]]

다른 PC(GitHub 15ffed4, 2026-09-29)의 SKILL 에는 "한문철은 말할 때만 = 얼굴이 나오며 실제로 말하는 순간만 원본 소리(입 모양 맞게)"로 적혀 있다. 둘 다 지킨다: 사용자가 넣으라 할 때만 + 넣으면 말하는 순간만 동기화된 원본 소리. 이 PC 클론은 그 커밋을 pull 하지 않아 몰랐다(2026-10-01 기준 로컬 ahead 50·behind 6, SKILL.md·pipeline.py 충돌).
