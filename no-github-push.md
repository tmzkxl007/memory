---
name: no-github-push
description: 깃허브에 올리지 말 것 — 사용자가 직접 말하기 전엔 git push 금지 (2026-09-29)
metadata:
  node_type: memory
  type: feedback
  originSessionId: 00422c73-9d88-4d13-8b31-d61430fa52fd
  modified: 2026-09-29T05:41:27.277Z
---

작업 결과를 GitHub 에 push 하지 않는다. 사용자 원문: "깃허브에 올리지는 마" (2026-09-29, 맴매각 저장소에 참사이다 나레이션 분석 문서를 푸시했다고 보고한 직후).

**Why:** 사용자는 GitHub 업로드를 원하지 않았다. 그 문서 커밋(cc3b95a)은 원격에서 되돌렸고(force-with-lease, 원격 4a49fc5), 파일은 로컬 `.git/info/exclude` 로 빼 둠. 그 전에 푸시한 ep04~06·pipeline 커밋(f0e7151, 4a49fc5)은 그대로 원격에 있음 — 사용자가 따로 말하지 않았음.

**How to apply:** 파일 저장·로컬 커밋까지만 하고 push 는 사용자가 "올려줘"라고 할 때만. [[proceed-without-asking]] 의 "푸시도 묻지 말고" 보다 이 규칙이 우선. 관련: [[maemmaegak-preset-workflow]]
