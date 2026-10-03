---
name: forey-preset-workflow
description: forey-preset(포레이로) = github.com/jihyunok/forey-preset → ~/forey-preset(git) + 작업 폴더 ~/volcano_work. 나레 주인 세로 드라마 숏폼 파이프라인
metadata: 
  node_type: memory
  type: project
  originSessionId: d2b57b69-f033-4505-a9b3-68def4d202fa
  modified: 2026-09-15T05:33:57.067Z
---

"forey-preset" / "포레이로 프리셋" = 저장소 `~/forey-preset` (jihyunok/forey-preset, 2026-09-15 클론).
설치본은 `~/volcano_work` (CLAUDE.md · docs/ · presets/포레이로/ · examples/). **작업은 ~/volcano_work 에서**,
규칙·기록은 `docs/PLAYBOOK-포레이로.md`·`docs/SESSION-LOG-포레이로.md` 에 적고 **~/forey-preset 에 복사해 커밋**하고 ★**푸시는 `drama` 리모트(github.com/tmzkxl007/drama-preset)로만** 한다(2026-09-24 사용자 지시 · main 의 upstream = drama/main, origin=jihyunok/forey-preset 에는 올리지 않는다)(커밋 identity 는 `-c user.name=jihyunok -c user.email=251929866+jihyunok@users.noreply.github.com`, 전역 설정 없음).

- 파이썬 `~/.volcano/venv/Scripts/python.exe`, 키 `~/.volcano/keys/{typecast,speechmatics}` (gemini 없음).
- 절차: prep → _asr_sm → episode.py → dlgcheck → get_fonts → tts → align → reframe → build → synccheck → cutsheet.
- 완성본 `~/volcano_work/포레이로/<편>.mp4` + `<편>_업로드.txt` → **사용자 납품 폴더 `~/Downloads/드라마/`** 에도 복사한다(2026-09-15 지시).
- 첫 편 mk01_눈빛제압(메이드 인 코리아 2, 디즈니+ 공식 쇼츠). 세로 쇼츠 소재는 §17-44 대로 그림 칸만 오리고 `spec.ZOOM` 덮어쓰기.
- 박힌 글자(하드섭·편집자 자막)는 §17-47: 그림 칸(프레임별 max 로 잰 행 범위)만 오려 [[vmake-skill]] SKM0002 로 지우고 소리는 1차 처리음을 얹는다. mk01 vmake 판 = `mk01_눈빛제압_vmake/`.
- 사용자 소재 폴더: `~/Downloads/서호준(쇼츠)/원본영상_youtube/` (파일명에 전각 ｜ → ASCII 로 복사해서 쓴다).

- 사용자 확정 취향(2026-09-15 mk01): 나레 목소리 = 커스텀 보이스 **"드라마"** `uc_6aa8eb42d1b77888a4240797` · 1.3배 ·
  `STYLE="tome"`(대사 살리고 말틈에 짧은 나레) · 마지막 마디는 재밌는 "내 생각" 한 줄("~열라 쫄았네" 톤) ·
  펀치 대사 구간 배경음악은 demucs 로 뺀다(시스템 python 에 demucs 있음) · 인물명은 사용자 확인(황 장군→전 장군).

**How to apply:** 3D·크랩 프리셋과 별개 채널이다 — 자산·엔진 섞지 않는다. [[proceed-without-asking]] [[preset-firewall]]
- (2026-09-18) 업로드 세트 `* 작품:` 줄 아래에 "더 자세한 내용은 디즈니 플러스에서 감상하는 걸 추천합니다!" 한 줄 — 사용자 요청, 이후 모든 편 기본(플랫폼은 작품에 맞게).
- (2026-09-23) 장면전환 효과음(휙) 끔 — `spec.SFX_TRANS=False`. 0초 두둥 북소리는 그대로. 사용자 "슥 같은 효과음은 빼줘".
