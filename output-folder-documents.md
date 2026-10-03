---
name: output-folder-documents
description: 완성 영상은 내 문서의 두둥픽 폴더로 내보낸다
metadata:
  type: project
---

완성된 영상 파일은 `C:\Users\최진영\OneDrive\문서\두둥픽\` 에 복사해 둔다. 사용자 요청: "다운로드 받는 위치는 내컴퓨터 내문서로 경로 만들어줘"(2026-09-10).

**Why:** 작업 폴더(`~/3d_works/<영상id>`)는 중간 산출물이 섞여 있어 완성본을 찾기 어렵다. 내 문서는 탐색기에서 바로 열리는 자리다.

**How to apply:** 이 PC의 내 문서는 OneDrive로 리디렉션되어 있어 실제 경로가 `~/Documents`가 아니라 `~/OneDrive/문서`다 — 하드코딩하지 말고 `[Environment]::GetFolderPath('MyDocuments')` 로 확인한다. 작업 폴더는 그대로 두고 완성본만 복사한다. 관련: [[volcano-3d-preset-workflow]]
