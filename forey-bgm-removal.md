---
name: forey-bgm-removal
description: 포레이로(drama-preset) 편은 배경음악을 뺀다 — 사용자 확정 규칙(2026-09-22), devocal.py + build.py 도장 검사
metadata:
  type: feedback
---

2026-09-22 사용자 "앞으로도 배경음악 빼줘" — 포레이로 편은 **드라마 원음의 음악을 빼고 목소리만** 깐다. 스캔들뿐 아니라 모든 포레이로 편 기본.

**Why:** 나레 밑에 드라마 음악이 깔리는 게 싫음.
**How to apply:** 절차 안에 있다 — `python presets/포레이로/devocal.py <편>`(전역 Python311 demucs.exe, CPU 410초≈3분)을 prep 다음에 돌린다. `build.py` 가 `_devocal.json` 도장 없으면 [규격 위반]으로 막고, 도장 있으면 BED_LIFT m=3 으로 낮춘다. 남길 편만 `KEEP_BGM = True`. 무음 비율이 15~20%로 오르는 건 감수. 포크 지시에도 4단계로 들어 있다. [[forey-preset-workflow]] [[forey-scandal-progress]]
