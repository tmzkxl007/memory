---
name: preset-firewall
description: 3D 프리셋과 크랩 프리셋은 규격이 정반대라 방화벽 4겹으로 분리해 뒀다
metadata:
  type: project
---

이 컴퓨터에는 영상 프리셋이 둘이고 규격이 정반대다 — 3D(두둥_픽)는 세로 1080×1920 / 43초, 크랩(KLAB)은 가로 1920×1080 / 6분 30초. 섞이지 않게 2026-09-10에 4겹을 깔았다.

**Why:** 사용자 요청 "3D프리셋과 크랩 프리셋이 서로 섞이지 않게 방화벽 만들어줘". 자산·납품 경로·저장소가 전부 달라 한 번 섞이면 결과물을 통째로 다시 만들어야 한다.

**How to apply:** 새 영상 작업 전에 `~/CLAUDE.md` 의 라우팅 표로 어느 프리셋인지 확정한다. `~/.claude/preset_firewall.py` 가 PreToolUse 훅으로 교차 조작을 실행 전에 차단하므로, 차단되면 명령을 저장소별로 나눠 실행한다 — 의도적 교차 작업일 때만 명령에 `FIREWALL_OK` 를 넣는다. 납품 전에는 해당 저장소의 `preset_guard.py <완성본.mp4>` 를 돌려 합격을 확인한다(실제로 -15.8 LUFS 미달을 잡아냈다). 관련: [[volcano-3d-preset-workflow]], [[output-folder-documents]]
