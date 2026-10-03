---
name: jeoseungkong-preset-workflow
description: 저승콩 천사콩 = ~/jeoseungkong-cheonsakong (nm2240), agy 이미지 전용, 볼케이노·EvoLink 금지, 9편 ep09_plane 준비 상태
metadata:
  type: project
---

"저승콩 천사콩" 프리셋 = `~/jeoseungkong-cheonsakong` (GitHub private nm2240/jeoseungkong-cheonsakong, 2026-09-28 클론). 지침은 저장소 SKILL.md.
- 그림은 agy(`agy_gen.py`)로만 — 사용자 지정(09-28): `--model gemini-3.8-flash-high --effort high`, 그림 모델은 agy generate_image = 나노바나나2(gemini-3.1-flash-image, 최신, agy에서 모델 선택 불가). 그림 한도는 `/usage`에 안 나오고 429 오류로만 알 수 있음. EvoLink·볼케이노 MCP 금지. 완성본은 저장소 안 `저승콩 천사콩 최종본/`.
- 이 PC의 ElevenLabs 키는 sound_generation 권한이 없음(401) → make_sfx.py 새 효과음 불가, 기존 sfx 조합으로 대체.
- agy_gen.py 에서 `--dangerously-skip-permissions` 를 뺐다(09-28 2차). 호출마다 ImageName 토큰(jsk_…)을 주고 `~/.gemini/antigravity-cli` 아래에서 결과 이미지를 찾아옴. 429 QUOTA_EXHAUSTED면 재시도 없이 멈춤. (이미지 저장 위치는 할당량 리셋 후 첫 호출로 확인 필요)
- 9편 `episodes/ep09_plane`(쇼츠 UBWqwIiB0Lw 경비행기 vs 패러글라이더) 2026-09-28 11:20 완성·푸시(ea8f16c), 22.9초. agy 그림 한도(a93231123) 소진이라 사용자 지시로 **Google Flow(flowkit)** 로 그림 생성: `IMG_BACKEND=flow` + `flow_gen.py`(NARWHAL=나노바나나2). flowkit = ~/flowkit, 서버는 `FLOW_PROJECT_ID=685f49d1-0ea9-4b72-9615-4cc8cc86b465 venv/Scripts/python -m agent.main`(8100), 크롬 확장 + flow.google.com 탭 필요.
- poses 합성이 원래 캐릭터 자리 근처(reach 61)만 붙여 크게 움직이는 포즈가 네모로 잘림 → 9편은 reach 241로 다시 붙여 해결(파이프라인엔 미반영).
- a93231123 은 이 PC에서 그림 0장인데 첫 요청부터 agy 그림 429 — 가족(울트라 6인 공유)은 agy에서 됨, 다른 PC 사용 없음(사용자 말) → 원인 미확인.
