---
name: memory-backup-repo
description: 기억 파일 백업 저장소 = github.com/tmzkxl007/memory (비공개, 2026-10-03 첫 백업 커밋 0182a0f)
metadata:
  type: reference
---

사용자가 "https://github.com/tmzkxl007/memory 여기에 저장해줘"(2026-10-03)라고 해서 이 기억 폴더의 .md 38개를 main 브랜치에 올렸다(커밋 0182a0f).
저장소는 처음에 공개였고, 이메일·채널 ID·프로젝트 ID·사용자 이름이 든 경로가 있어 확인했더니 사용자가 직접 비공개로 바꾼 뒤 올림(로그인 없이 API 404 로 비공개 확인).

**How to apply:** 백업을 다시 해 달라고 하면 이 저장소를 받아 기억 폴더의 .md 를 덮어쓰고 커밋·push. 올리기 전 비공개인지(`curl -o /dev/null -w %{http_code} https://api.github.com/repos/tmzkxl007/memory` → 404) 먼저 확인. 사용자가 말하지 않으면 자동으로 올리지 않는다([[no-github-push]]). git 작성자: -c user.name="최진영" -c user.email=a93231123@gmail.com. gh CLI 는 이 PC 에 없음(git + 자격 증명 관리자로 push 됨).
