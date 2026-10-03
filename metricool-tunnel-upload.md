---
name: metricool-tunnel-upload
description: "터널방식" 메트리쿨 예약 = 로컬 mp4를 http.server + cloudflared 임시 URL로 열어 media에 넣는 방법
metadata:
  type: reference
---

사용자가 "터널방식으로 예약"이라고 하면 이 순서로 한다.
1. 영상을 scratchpad/serve 에 ASCII 이름으로 복사한 뒤 `python -m http.server 8765 --bind 127.0.0.1` 을 돌린다(백그라운드).
2. `C:\Program Files (x86)\cloudflared\cloudflared.exe tunnel --url http://127.0.0.1:8765 --no-autoupdate` 를 로그로 남기며 돌리고, 로그에서 trycloudflare URL을 찾아 curl -I 로 200이 나오는지 확인한다.
3. createScheduledPost 의 media 에 그 URL을 넣는다. 메트리쿨은 예약할 때 영상을 static.metricool.com 으로 복사해 둔다. 그러므로 예약이 끝나면 cloudflared 와 서버를 바로 닫아도 된다.
   - `Failed to normalize media` 가 나면 터널이 느려서 메트리쿨이 받다가 시간이 초과된 것이다. 2026-09-29에 34MB를 받는 데 44초가 걸렸을 때 이 오류가 났다. cloudflared 를 끄고 `--protocol http2` 를 붙여 새로 열었더니 16초로 줄었고 예약이 됐다. 예약하기 전에 `curl -w "%{time_total}"` 로 전체 다운로드 시간을 재 보는 게 좋다.
4. 제목은 `<id>_업로드.txt` 의 첫 줄로, 본문은 나머지로 한다. 세로 영상이면 youtubeData.type=short, madeForKids=false 로 둔다.

브랜드 (2026-09-24에 한글 이름으로 바뀜. 예약은 ID로 하므로 이름이 바뀌어도 상관없다. 전부 YouTube, 시간대 Asia/Seoul):
- 앵보이 (옛 Aeng boy) = 7064565
- 달달콩콩 (옛 daldalkongkong) = 7059755
- 오란씨 (옛 Oran-C) = 7064457
- 이모저모 (옛 emo jomo) = 7064595
