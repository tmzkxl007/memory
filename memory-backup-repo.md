---
name: memory-backup-repo
description: 기억 파일 백업 저장소 = github.com/tmzkxl007/memory (2026-10-03 기준 공개 상태, 사용자가 공개로 올려도 된다고 함; 커밋 0182a0f → a12366e → 54f52cc)
metadata:
  type: reference
---

사용자가 "https://github.com/tmzkxl007/memory 여기에 저장해줘"(2026-10-03)라고 해서 이 기억 폴더의 .md 38개를 main 브랜치에 올렸다(커밋 0182a0f).
저장소는 처음에 공개였고, 이메일·채널 ID·프로젝트 ID·사용자 이름이 든 경로가 있어 확인했더니 사용자가 직접 비공개로 바꾼 뒤 올림(로그인 없이 API 404 로 비공개 확인).

**How to apply:** 백업을 다시 해 달라고 하면 이 저장소를 받아 기억 폴더의 .md 를 덮어쓰고 커밋·push. 올리기 전 비공개인지(`curl -o /dev/null -w %{http_code} https://api.github.com/repos/tmzkxl007/memory` → 404) 먼저 확인. 사용자가 말하지 않으면 자동으로 올리지 않는다([[no-github-push]]). git 작성자: -c user.name="최진영" -c user.email=a93231123@gmail.com. gh CLI 는 이 PC 에 없음(git + 자격 증명 관리자로 push 됨).

두 번째 백업(2026-10-03, 커밋 a12366e): 새 편 표준·폴리스라인·이 메모 추가. pull 은 자격 증명 창 때문에 멈춘 적이 있어 쓰지 않고, push 는 `GIT_TERMINAL_PROMPT=0 timeout 90 git push origin main` 으로.

세 번째 백업(2026-10-03, 커밋 54f52cc): 저장소가 공개(API 200)로 바뀌어 있어 멈추고 알렸더니 사용자가 "그냥 올려 괜찮아". 앞으로 이 저장소는 공개여도 사용자가 허락한 상태 — 다만 백업할 때 공개 여부는 한 줄로 알려 준다.
네 번째(2026-10-03, 커밋 be5eccb): 사용자 "다른 컴퓨터에서 깃허브 주소만 보내면 이 프리셋으로?" → 같은 저장소에 `lastwitness-preset/` 폴더(스크립트·검은고딕/고딕A1 OFL 폰트·그노시엔느1 PD·click.wav·template=4편 스크립트·examples=1~3편 plan·SETUP.md) 추가, 9.1MB. 잘난체는 재배포 조건 때문에 빼고 받는 법만 적음. 키(speechmatics)·flowkit(crisng95/flowkit)+크롬 확장 로그인은 새 PC 에서 직접. 프리셋을 고치면 이 폴더도 같이 갱신해서 올릴 것.
