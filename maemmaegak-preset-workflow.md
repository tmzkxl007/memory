---
name: maemmaegak-preset-workflow
description: "맴매각 = ~/maemmaegak (nm2240/maemmaegak) 참사이다식 블랙박스 무한루프 쇼츠. 다른 PC에서 시작, 완성본은 GitHub에 없음. 이 PC 첫 편 ep04 (2026-09-29)"
metadata:
  node_type: memory
  type: project
  originSessionId: 00422c73-9d88-4d13-8b31-d61430fa52fd
  modified: 2026-10-01T04:32:58.440Z
---

맴매각 프리셋 = `~/maemmaegak` (GitHub private nm2240/maemmaegak, 2026-09-29 클론). 지침은 저장소 `SKILL.md`, 실행은 `pipeline.py` (Python312 + opencv·numpy·pillow·scipy). ep01~03 은 다른 PC(`C:\Users\Administrator`)에서 만들었고 `맴매각 최종본/` 은 gitignore → 그 완성본은 이 PC·GitHub 어디에도 없다 (사용자가 "만들어진 영상 다운" 요청했을 때 이렇게 설명함).

- 이 PC 첫 편: `episodes/ep04_parking_truck` (참사이다 쇼츠 cle-vcCFfgg, 사용자 "허락 받았어") 14.1초 → `~/maemmaegak/맴매각 최종본/불법주차_트럭_참교육.mp4`, 커밋 f0e7151 푸시.
- ep05 한문철 갓길 추월(18.2초, 라이브 VOD 원본 구간 사용)·ep06 그것이 블랙박스 모닝 할머니(16.9초) — 사용자 "병렬로 작업해줘"로 포크 2개 동시 제작, 커밋 4a49fc5. 권리는 ep01~03 에 적힌 채널 허락 기록을 근거로 진행하고 사용자에게 알림.
- ep07 202km 초과속 오토바이 (2026-10-01, 에펨코리아 글 → 한문철TV 28376회 ue9Pp--bDYk 가로 원본): 20.9초, 커밋 6027c68(푸시 안 함). 오토바이 본인 블박 + 목격차 확대. 한문철 판정 장면은 넣었다가 사용자 지적으로 삭제(커밋 cadade2, 18.3초) — [[hanmuncheol-only-when-asked]].
- 2026-10-01 오후: 사용자 "다른 컴퓨터 깃허브 업데이트 했거든 그걸로 다시 만들어봐" → origin 7bdac06 합침(커밋 9f58c36, SKILL 충돌은 다른 PC 판을 기본으로 + 이 PC 규칙 '사람 말소리 효과음 금지'·punch/whip 설명 유지). ep07 을 새 템플릿(_template, y470~1446·두둥_픽식 헤더·우우웅 끽 쿵·인트로 2번·끝→첫 나레이션 한 문장)으로 재제작 20.6초. 새 qc 기준(루프 이어짐 OK·빈 구간 없음)·tools_narr_level.py(--raw-mix 두 번 뽑은 뒤) 사용. 이 PC 에 없는 '뒤로감기 효과음.mp3'·'심장소리.mp3' 는 assets/sounds/rewind.wav·heartbeat.wav 로 대체.
- 2026-10-01 사용자 "저장 커밋 푸쉬해줘" → origin f91eaa8(다른 PC: ep07_bike_police·ep02 v2·face_blur·RULES_*.md) 합쳐 ae25837 푸시. **에피소드 번호 겹침**: 다른 PC ep07 = ep07_bike_police, 이 PC ep07 = ep07_overspeed_bike (폴더가 달라 충돌은 없음). 다음 새 편은 ep08 부터. pipeline 은 줄바꿈(CRLF/LF) 차이로 파일 전체가 충돌로 잡힘 → 이 PC 판에 상대 diff 만 git apply --ignore-whitespace 로 얹고 LF 로 맞춤.
- 이 PC git 에 user.name 이 없다 → 커밋은 `git -c user.name=nm2240 -c user.email=a93231123@gmail.com commit` (이전 커밋 작성자와 같게).
- **★ 프리셋 템플릿(제목·도장 배치 등)은 사용자가 말하기 전엔 고치지 않는다** (사용자 "프리셋에 고치지마", 2026-09-29): 쇼츠 잘림 대응(제목 안쪽·아래로)을 pipeline 기본값으로 넣었다가 되돌림(커밋 0ed44e2). 한 편만 고칠 땐 그 편 설정으로.
- **★ 사람이 말하는 효과음 금지 — 2026-10-01 좁아짐: 아픔·신남 반응 음성은 넣음, [[maemmaegak-fx-pairing]]** (사용자 "이 프리셋에는 이런 사람이 말하는 효과음이 안들어가야해", 2026-09-29): 대사·욕·밈 음성은 삐 처리해도 안 넣음, 욕·반응은 화면 글씨로만. pipeline `SPEECH_SFX` 에 걸리면 render 멈춤. 허얽·뜨헉 같은 짧은 놀람 소리는 일단 남겨 둠(사용자 확인 전). ep06 에 "이게 뭔 개소리야"가 남아 있음(재제작 여부 미결).
- ep04b(트럭 참사이다식 나레 샘플) 사용자 수정 반복 중: TTS 1.3배, 긁힘=Mixkit 실제 효과음, 화난 경적 7초 1번(작게), 사용자 효과음 폴더 = `문서\효과음\효과음_1\효과음 - 복사본`(SFX_DIRS 맨 앞).
- 효과음: OneDrive `문서\효과음\효과음_1` + `문서\쇼츠\마라하기 효과음 (1)` 만 로컬에 있음. `블로그 풀팩\…\★효과음…` 등 온라인 전용 파일은 "cloud file provider is not running" 으로 못 읽음. 없는 소리는 `make_sounds.py` 합성음.
- 남의 편집본 소재는 SKILL §0 권리 확인 필수 — 물어보고 허락 답을 받은 뒤 진행했다.

- 2026-10-02: GitHub 081aed6(다른 PC ep08~ep10) fast-forward 로 받음. **이 PC ep11** = `ep11_porter_cabriolet` 지붕 날린 포터 역주행 (에펨 글 → 한문철TV 쇼츠 #5968 설명란 '260910 (목) 1부' → 라이브 ZC7j5jD8l9Q 880~960초 1920x1080), 18.1초, 커밋 0f955ba(푸시 안 함). 충돌 없는 스침이라 우우웅 끽(trim 0.85)만. **영상 속 자막이 트럭 아래 박혀 있으면** 블박차가 멈춰 있을 때 그 자리를 깨끗한 프레임 조각으로 덮은 src.mp4 를 만들어 크롭을 아래로 내릴 수 있음(나레이션 자막 y≈710 이 대상 가리지 않게). 다음 새 편은 ep12 부터.
- 2026-10-02 (같은 날): 에펨 링크 3개 → 포크 3개 병렬 제작, 커밋 15f5ae1(푸시 안 함). ep12_night_runner 밤길 차도 런닝 학생(26734회 kIaieD9LXNY, 17.9초) · ep13_wrongway_ambush 새벽 역주행 블박차 vs 전기자전거(28033회 qLVSjtWe0po, 18.2초, 블박차가 역주행한 쪽) · ep14_starex_towed_bike 끈에 묶여 끌려가던 오토바이(원본 못 찾아 에펨 720×396 첨부본, 22.5초, 영상 속 글씨 지우기 work/clean_src.py 강제 커밋). 다음 새 편은 ep15 부터.

**Why:** 프리셋이 다른 PC 경로(효과음 폴더 등)를 가정하고 있어서, 이 PC에서 돌리려면 위 사항이 필요했다.

**How to apply:** "맴매각" 요청 → `~/maemmaegak/SKILL.md` 대로, 새 편은 `episodes/epNN_*`. 3D/크랩/포레이로/라마 자산과 섞지 않는다. 관련: [[proceed-without-asking]] [[netflix-subtitle-standard]]
