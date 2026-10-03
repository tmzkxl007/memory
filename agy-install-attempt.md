---
name: agy-install-attempt
description: "agy(Antigravity CLI) 2026-09-28 설치·로그인 성공(a93231123 계정), 모델은 --model 플래그로 고정, 상태줄 가드 추가, TubeLens 키 2개 삭제 여부 미결"
metadata:
  type: project
---

2026-09-28 세 번째 시도에서 **성공**. %LOCALAPPDATA%\agy\bin\agy.exe v1.2.12, a93231123@gmail.com 로그인(자격 증명 `gemini:antigravity`), /usage 로 Gemini 5시간·주간 한도 확인. 규칙은 ~/CLAUDE.md 「제미나이는 agy로만」 절.

- 09-26 두 번은 fuksmanlili195 계정 지역 거부로 전부 되돌렸음 → 그 계정은 쓰지 않는다.
- 기본 모델: settings.json 의 `model` 키는 무시됨(로그 `model_config_manager` 로 확인) → 항상 `--model gemini-3.8-flash-high`. 현재 기본값도 3.8 Flash (High).
- `-p` 헤드리스에서 agy 가 명령 도구를 쓰려 하면 자동 거부되고 "no output produced" → 순수 텍스트 요청으로 보낸다.
- statusline.py refresh_agy 에 "cmdkey 에 gemini:antigravity 있을 때만" 가드를 넣었다(로그인 전 숨은 OAuth 충돌 방지).
- **미결:** TubeLens api_keys.json 두 곳(바탕 화면, Downloads/TubeLens)에 AIza 키 — 유튜브 키일 수 있어 지우지 않고 사용자에게 물음.
