---
name: rounded-noejeongu-preset-workflow
description: "noejeongu-preset"/"둥근 뇌전구" 요청 = ~/rounded-noejeongu-preset (nm2240/rounded-noejeongu-preset) 수동 ffmpeg 파이프라인. 볼케이노 MCP 뇌전구 프리셋 아님. 키 위치·이미지 소싱·길이 트레이드오프.
metadata:
  type: project
---

사용자가 "noejeongu-preset으로 만들어줘"라고 하면 `~/rounded-noejeongu-preset`(README가 전체 스펙)의 5개 스크립트 CUSTOMIZE 구간만 채워 돌린다. 볼케이노 MCP `뇌전구` 프리셋은 버려진 방식이라 쓰지 않는다. 작업 폴더 `~/noejeongu-work/<소재id>/img`, 완성본 `C:\Users\최진영\OneDrive\문서\뇌전구\`. 첫 제작 2026-09-14(네이버 008/0005413076 지지율 기사, 36.9초).

**Why:** README는 다른 PC에서 쓰였다 — 이 PC엔 README가 참조하는 메모리(`project_hainma_template_spec.md` 등)도, ElevenLabs 키도 없었다. 사용자가 세션 중 `sk_` 키를 줘서 `~/.volcano/keys/elevenlabs`에 저장했다(voices_read 권한은 없지만 TTS는 됨; 키 ID를 키로 주면 401이라 `sk_` 키인지 확인).

**How to apply:**
- 이미지: 기사·방송사(KBS/MBC/뉴스1 등) 화면 금지 → **리얼미터 공식 차트/PDF**(realmeter.net, `pdftoppm`로 페이지 렌더)·**KTV 국민방송**(정부 제작, 채널 UCIMOytYIzaUpoAM2bpT4JZQ) 프레임·페페 라이브러리 `~/volcano-work/군림보/fm_10323813802/pepe/fm/`(57장) 조합이 통했다. KTV 프레임은 하단 자막 밴드·좌상단 로고 피해서 박스 비율 0.878로 미리 크롭(`-ss` 정확 탐색은 컨택트시트 fps 샘플과 프레임이 달라 자막이 끼어들 수 있음 → 잘라낸 결과를 반드시 다시 본다).
- 길이 vs 이미지 수: README의 "19~28초"와 "이미지 15장 이상"은 충돌한다. 숫자가 많은 대본은 세그먼트당 ~2.4초라 15세그먼트면 ~37초. 15장 유지 쪽을 택했고 사용자 피드백은 아직 없음.
- 05_render.py의 `scale=-2:H,crop`을 README 권고대로 `scale=W:H:force_original_aspect_ratio=increase`로 바꿔 두었다(저장소 미커밋 상태).
- `%P`는 TTS 발음이 불안해 대본에 "3.6포인트"로 쓴다. 관련: [[gunrimbo-community-preset-workflow]] [[output-folder-documents]] [[proceed-without-asking]]
