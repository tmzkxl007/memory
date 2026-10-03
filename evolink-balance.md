---
name: evolink-balance
description: EvoLink 남은 크레딧 조회법 — GET api.evolink.ai/v1/credits, 키는 ~/.volcano/keys/evolink
metadata:
  type: reference
---

EvoLink 잔액: `curl -H "Authorization: Bearer $(cat ~/.volcano/keys/evolink)" https://api.evolink.ai/v1/credits`
→ 실제 잔액은 `data.user.remaining_credits` (`data.token` 쪽은 키 한도라 unlimited 99999 로 나와 의미 없음).
2026-09-28 조회: 남은 1.2327 / 쓴 1308.77 크레딧. 나노바나나 그림 1장 1.6크레딧이라 한 장도 못 만드는 상태. [[medhist-channel-workflow]]
