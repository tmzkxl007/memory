---
name: netflix-subtitle-standard
description: "모든 프리셋에 넷플릭스 자막 규격 경고 단계 + 자막은 한 줄(사용자 지정) — 짧은 자막 합치기·enforce fail 은 미결"
metadata:
  node_type: memory
  type: project
  originSessionId: f78170b2-f5fa-45a8-bbce-c297edf42ca0
  modified: 2026-09-25T00:37:54.349Z
---

2026-09-25 사용자가 넷플릭스 Timed Text Style Guide(General + Korean) 를 "모든 폴더에 적용"하라고 함.
각 프리셋 저장소에 `NETFLIX-자막규격.md` + `netflix_sub_check.py` 추가, 3D·크랩 preset_guard 에 `--subs` 옵션(preset.json `subtitle_standard.enforce: "warn"`).
크랩은 한 줄 14~22자 → 16자 이하로 규칙 자체를 바꿈.
**자막은 한 줄**(사용자 "자막을 한줄로 해줘", 2026-09-25 — 넷플릭스 2줄보다 엄격): 정치·뇌전구 `04_build_captions.py` `MAX_LINES = 1`(16자 조각을 한 줄씩, 3으로 두면 옛 3줄 카드), 군림보·강석주는 `~/volcano-work/oneline_subs.py`(post_fix.py 3단계 자동), 포레이로·라마 spec `DLG_LINES`/`CAP_MAXLINES` = 1(원래 전부 한 줄). 짧은 조각 합치기는 16자 넘으면 안 합침. 짧은 자막 합치기(3D stage5_build, 포레이로/라마 NARR_CHUNK)와 정치/뇌전구 오른쪽 정렬·기울임은 **안 바꿈**.

**Why:** 기존 완성본 전부 위반(3D 35%·포레이로 27%·라마 29% 자막이 0.83초 미만 위주, 정치/뇌전구 100% 레이아웃). 강제하면 사용자 확정 모양(한 줄 강제, 나레 1행, 3줄 롤링)이 바뀜.

**How to apply:** 새 편 만들 때 검사기를 돌려 경고를 보고. 빌더 자동 합치기/enforce "fail" 전환은 사용자가 정하면 진행. 관련: [[preset-firewall]] [[preset-3d-defaults]]

**포레이로 자동 적용(2026-09-25, 커밋 bd515bc):** 사용자 "앞으로 만들 영상에" · "만들어진 편은 그냥 나둬" — 이미 만든 편은 다시 굽지 않음. `presets/포레이로/netflix_sub.py` + chunks() MODS(꾸미는 말 뒤 안 끊기) + align.py resplit(0.83초 미만 나레를 낱말 시각으로) + build.py fix_ass(늘리기·0.10초 안 당기기·한 줄 합치기). PLAYBOOK §17-53.

**전 프리셋 빌더 자동 적용(2026-09-25, 사용자 "모든 폴더에 적용해줘"):** 3D `scripts/batch/stage5_build.py` (+netflix_sub.py, 42편 시험 위반 481→35), 라마 엔진(커밋 383db9b), 정치·뇌전구 `scripts/04_build_captions.py` (+scripts/netflix_sub.py), 군림보·강석주 `~/volcano-work/oneline_subs.py` 의 netflix_timing. 크랩은 빌더 없음. 3D·크랩·정치·뇌전구·군림보 저장소는 미커밋.

**3D 한 편짜리 템플릿도 적용(2026-09-28, 사용자 "다시 굽지 말고 이제부터 만드는 편에 적용"):** `scripts/narration_variant/build_ass.py` 에 같은 netflix_sub 모듈(nf_split·어절 시각·fix_ass). 8편 시험 위반 143/288 → 11/198. 두둥픽 완성본 42편은 전부 규격 전(09-10~15) 제작이라 위반 36% — 다시 굽지 않음. 3D 저장소 넷플릭스 작업 커밋 c629d21(09-28, master). git 사용자 정보가 전역 설정에 없어 -c user.name/email 로 기존 작성자(최진영) 지정.
