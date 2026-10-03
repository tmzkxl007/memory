---
name: vmake-skill
description: "VmakeSkill(워터마크·자막 제거, 화질 복원 유료 API) 설치 위치와 실행법 — ~/vmake, 전용 venv, UTF-8 필요"
metadata: 
  node_type: memory
  type: reference
  originSessionId: d2b57b69-f033-4505-a9b3-68def4d202fa
  modified: 2026-09-15T07:35:55.449Z
---

VmakeSkill (clawhub `vmake-skill` v2.0.0) — 2026-09-15 설치.
- 위치 `~/vmake/skills/vmake-skill/`, 파이썬 `~/vmake/venv/Scripts/python.exe`, 키 `scripts/.env`(MT_AK·MT_SK, 채팅에 다시 적지 말 것).
- 실행: `cd ~/vmake && PYTHONIOENCODING=utf-8 PYTHONUTF8=1 ./venv/Scripts/python.exe skills/vmake-skill/scripts/vmake_ai.py <catalog|run-task|spawn-run-task|query-task>`
  ★UTF-8 환경변수 없으면 카탈로그의 중국어 때문에 cp949 에러로 `config_unavailable` 이 난다.
- 카탈로그(v2): SKM0001 영상 화질복원(Fast 2K) · SKM0002 영상 자막제거(Subtitle) · SKM0003 영상 스마트 지우기 · SKM0005 Smart Pro ·
  SKM0004 이미지 화질복원 · SKM0006 이미지 워터마크 제거. `--task` 에 material_id 를 넘긴다.
- 유료(계정 쿼터 소비). 업로드·쿼터 사용 전에 사용자 승인 한 번 받는다(SKILL.md 규칙). 영상은 spawn-run-task + 폴링.
- Node.js LTS·clawhub CLI 도 이날 전역 설치.
