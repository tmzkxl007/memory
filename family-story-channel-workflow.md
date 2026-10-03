---
name: family-story-channel-workflow
description: "새 채널 \"가족 사연 쇼츠\"(마음 머문 이야기 벤치마크, 시댁 사연 대화극) — ~/family_story_work, Flow 그림·Typecast 3목소리, 1편 완성 (2026-09-28)"
metadata:
  node_type: memory
  type: project
  originSessionId: 0b019826-78ba-4cf9-8a1d-7eb3a5b6eeb0
  modified: 2026-09-28T07:29:29.158Z
---

2026-09-28 시작한 새 세로 쇼츠 채널. 벤치마크 = 유튜브 「마음 머문 이야기」(@따뜻함가득, UCrRITyFQ2v6be_4534_chaA): "Ep.N ○○의 한마디가 충격입니다" 제목, 시댁 갈등 → 반전 화해, 끝에 질문형 댓글 유도, 2분 안팎. 기존 프리셋(3D/크랩/포레이로/라마/볼케이노)과 별개.

- 작업 폴더 `~/family_story_work/<편>/` (plan.py · tts.py · img.py · build.py · asr_check.py · sub_check.py — 의학의 역사 파일을 복사한 이 채널 전용 사본, import 금지). 공용 `~/family_story_work/flow_img.py`.
- 소재: 네이트판 사는얘기 랭킹에서 뽑음. 목록 = `바탕 화면\시댁사연_소재목록.txt`(추천 15 + 후보 163). 원글 문장은 쓰지 않고 상황만 각색, "실제 사연" 문구 넣지 않음, "퍼가지 마세요" 글 제외.
- 그림: Google Flow(flowkit 8100), 이 채널 전용 프로젝트 `558c1394-1218-4dcf-9c6f-d84ee2dd42f9`(family-story-shorts, 내가 만듦). 9:16 768×1376. 인물 기준 그림 `ref_<키>_solo.png`(첫 기준 그림에 아이·가족이 끼어 나와 참고 그림으로 한 사람만 다시 뽑음). 편당 15장.
- 목소리(Typecast ssfm-v30, 속도 1.0): 며느리·나레 Gowoon `tc_68785db8ba9cd7503f27d921`, 남편 Doyoon `tc_6a3350f8e5a50a4abe948fa8`, 시어머니 Sooni `tc_60ad0841061ee28740ec2e1c`. 강석주 목소리(Sanghyun)는 피함. 경상도 사투리 대사 OK(ASR 97.7%).
- 조립: 1080×1920, 위쪽 제목 두 줄(Jua, 흰/노랑) 고정, 자막 Jua 72 한 줄 16자(나레 흰색 · 대사 노랑), 문장 사이 0.25/화자 바뀜 0.4/장면 0.35초, BGM 쇼팽 녹턴 PD(반전 전 20번 단조 → plan.BGM_SWITCH 부터 10번 장조), -14 LUFS.
- 완성본 `내 문서\가족사연\`. 1편 `01_제삿날이제생일_시어머님의한마디.mp4` 122.4초, 자막 59장 위반 0.
- flowkit 서버가 작업 중 꺼진 적 있음 → `cd ~/flowkit && FLOW_PROJECT_ID=558c… venv/Scripts/python -m agent.main` 로 다시 켬.

관련: [[medhist-channel-workflow]] [[netflix-subtitle-standard]] [[proceed-without-asking]]
