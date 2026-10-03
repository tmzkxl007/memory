---
name: volcano-3d-preset-workflow
description: "3d 프리셋" 요청은 볼케이노 MCP가 아니라 nm2240/3D-preset 저장소의 ffmpeg 파이프라인을 뜻한다
metadata:
  type: project
---

사용자가 "3d 프리셋 영상"이라고 하면 볼케이노 MCP 프리셋이 아니라 `https://github.com/nm2240/3D-preset` (로컬 `~/3D-preset`) 저장소의 두둥_픽 스타일 파이프라인을 말한다. 볼케이노 MCP의 preset 목록에는 없다.

**Why:** 2026-09-10 세션에서 volcano MCP `setup`부터 시작했다가 사용자가 저장소를 알려주며 바로잡았다.

**How to apply:** `3D.md`(스타일 지침) → `SETUP.md`(환경) 순으로 읽고 `scripts/narration_variant/`를 작업 폴더로 복사해 대본만 갈아끼운다. 작업 폴더는 저장소 밖(`~/3d_works/<영상id>`)에 둔다. 복사한 스크립트의 `REPO_ROOT = Path(__file__).resolve().parents[2]`는 `Path.home()/"3D-preset"`으로 고쳐야 자산 경로가 맞는다. 파이썬은 PIL이 있는 `~/.volcano/venv/Scripts/python.exe`를 쓰고, 한글이 든 heredoc 패치는 `PYTHONUTF8=1`로 실행한다. 관련: [[proceed-without-asking]]
