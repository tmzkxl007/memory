# 마지막 목격자 프리셋 — 다른 컴퓨터에서 설정하기

실화 범죄·미스터리 16:9 롱폼(약 7~9분) + 쇼츠를 만드는 프리셋입니다.
만드는 방식(규칙)은 이 저장소 최상위의 기억 파일 두 개에 정리돼 있습니다. **먼저 읽으세요.**
- `../lastwitness-standard-recipe.md` — 새 편 만드는 순서(표준)
- `../lastwitness-channel-workflow.md` — 지금까지 정한 규칙과 각 편 기록

## 1. 폴더 놓기
이 `lastwitness-preset` 폴더를 통째로 `~/lastwitness_work` 로 복사합니다(이름이 바뀌어도 되지만 아래 설명은 이 이름 기준).

```
~/lastwitness_work/
  build.py 가 쓰는 공통 파일: fonts/ music/ click.wav endcard_yt.py subsplit.py
  flow_img.py import_mp3.py sub_check.py thumb2.py thumb.py omni_video.py
  template/          ← 새 편은 이 폴더를 복사해서 시작 (ep05_<소재>/)
  examples/          ← 1~3편 계획 파일(참고용)
```

## 2. 설치할 것
- **Python 3.11** + 패키지: `pip install numpy opencv-python pillow scipy kiwipiepy`
- **ffmpeg / ffprobe** (PATH 에)
- **폰트**: `fonts/` 의 검은고딕(BlackHanSans)·고딕 A1 은 SIL Open Font License 로 같이 넣었습니다.
  엔딩 좋아요·구독 버튼에 쓰는 **여기어때 잘난체(Jalnan2TTF.ttf)** 는 재배포 조건 때문에 넣지 않았습니다 →
  여기어때 잘난체 공식 배포처에서 받아 `fonts/Jalnan2TTF.ttf` 로 넣으세요.

## 3. 키·계정 (저장소에 없음 — 직접 설정)
- **Speechmatics** (녹음 mp3 를 대본 줄마다 자르는 데 사용): 키를 `~/.volcano/keys/speechmatics` 파일에 한 줄로 저장.
- **Google Flow 그림 생성 (flowkit)**: https://github.com/crisng95/flowkit 를 설치하고 `python -m agent.main` 으로 서버(127.0.0.1:8100)를 켠 뒤,
  크롬에 flowkit 확장을 설치하고 flow.google.com 에 같은 구글 계정으로 로그인. `curl http://127.0.0.1:8100/health` 의 `extension_connected: true` 확인.
  그림은 이 채널 전용 Flow 프로젝트(`flow_img.py` 의 PROJECT 기본값)에 만들어집니다 — 다른 계정이면 환경변수 `LASTWITNESS_FLOW_PROJECT` 로 바꿉니다.
- 나레이션은 **사용자가 직접 녹음한 mp3** 를 씁니다(TTS 키 필요 없음).

## 4. 새 편 만들기 (요약 — 자세한 건 standard-recipe)
1. 소재 사실 확인 → `cp -r template ep05_<소재>` → `plan_<약칭>.py` 작성(SCENES, 실제 자료는 위키미디어 공용 PD/CC 를 `archive/` 에)
2. 녹음 대본 txt 를 만들어 녹음 요청 → mp3 를 받으면
   `python ../import_mp3.py . <나레이션.mp3> plan_<약칭>`
3. 재연 그림: `LW_PLAN=plan_<약칭> python img.py` (Flow 가 막히면 4분 쉬고 이어서 함)
4. 카드: `python make_cards.py` (편마다 내용 고쳐 쓰기)
5. 조립: `LW_PLAN=plan_<약칭> python build.py` → `final_<약칭>.mp4`
6. 검사: `LW_PLAN=plan_<약칭> python ../sub_check.py final_<약칭>_subs.ass`, 소리 -14 LUFS
7. 업로드 정보: `python upload_info.py` (편마다 제목·목차·태그 고치기)
8. 썸네일: `thumb2.make(...)` (노란 띠 = 폴리스라인 기본)
9. 쇼츠: `python short.py <시작초> <끝초> <이름> "<제목\n둘째줄>" [--full]` (끝 안내 = 폴리스라인)

`template/` 의 파일 안 `final_dy`·`plan_dy`·`tts_dy` 같은 이름은 4편(디아틀로프) 것이니 새 편 약칭으로 바꿔 쓰세요
(`short.py`, `upload_info.py` 안의 `final_dy` 등).

## 5. 저작권 메모
- 실제 사진·영상은 위키미디어 공용의 퍼블릭 도메인/CC 자료만 사용, CC 자료는 업로드 설명란에 저작자 표기.
- 언론사·통신사 사진, 원래 벤치마크 채널 영상 화면은 쓰지 않음. 영화 캐릭터는 그리지 않고 작품 카드로.
- `music/gnossienne1.ogg` = Erik Satie 「Gnossienne No. 1」, 연주 La Pianista, 퍼블릭 도메인 (`music/sources.json`).
