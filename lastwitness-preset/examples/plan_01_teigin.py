# 마지막 목격자 1편 「데이긴 사건」 본편 — 05번 샘플 방식(2026-10-02 사용자 확정)
#   Jaejun · 첫인사 · 실제 사진(퍼블릭 도메인) 최대 + 기록 영상(PD) + 사진 편집 효과(툭·셔터·필름 결·빨간 동그라미) · AI 표시 없음 · AI 영상 없음
#   자료가 없는 장면만 재연 그림: use=기존 그림 재사용 / prompt=새로 만듦(img_full) — 밝은 자연광, 결정적 순간만 dark
# 대본·사실 근거는 plan.py 머리말과 같다. 대사 한 줄 = 장면 하나가 기본(원래 채널처럼 4~6초마다 화면 전환)
from plan import STYLE, DARK, TTS_FIX, NAMES   # noqa: F401
from plan_s1 import BRIGHT                      # noqa: F401

VOICE = "tc_653220349ba8419521ae8a63"   # Typecast Jaejun
TTS_DIR, IMG_DIR, OUTNAME = "tts_full", "img_full", "final_full"
TVOFF = True
# 인트로(2026-10-02 사용자 요청, 원래 채널처럼): 처음 2.4초 채널 신호음(직접 합성) → 첫인사부터 f03 까지 사티 「그노시엔느 1번」(퍼블릭 도메인 녹음, music/sources.json) 진하게 → 본론 '쿵' 후 평소 배경음악
INTRO = dict(music="music/gnossienne1.ogg", lead=2.4, at=1.6, offset=0.0, end_scene="f03", gain=0.22)   # 끝에 브라운관 TV 꺼지는 효과(2026-10-02 사용자 요청)

A = "archive/"
BANK, POSTER, H51, H20, TRIAL = A + "Shiina-Machi_branch_of_the_Teikoku_Bank.JPG", A + "Teigin_case.jpg", A + "Sadamichi_Hirasawa.jpg", A + "Sadamichi_Hirasawa_photographed_by_Ishii_Hakutei.jpg", A + "Hirasawa_Sadamichi_at_the_1st_trial.JPG"
REEN, KANDA, MATSUI, IKII, YAMADA = A + "Reenact_of_the_scene_of_Teigin_incident_by_Hirasawa_Sadamichi.JPG", A + "Kanda_when_Hirasawa_confessed.JPG", A + "Matsui_Shigeru_Teigin_incident_.JPG", A + "Ikii_Tamegoro.JPG", A + "Yamada_Yoshio_lawyer_.JPG"
INVEST, HACHI, HQ, COMPARE = A + "The_investigation_for_Hirasawa.JPG", A + "Hachioji_Medical_Prison.JPG", A + "Teikoku_Bank_Head_Office.JPG", A + "compare_montage_vs_hirasawa.png"
OT, JT = "footage/occupied_tokyo.webm", "footage/japan_today_1946.ogv"
CAP_REEN = "1948 히라사와의 범행 재연 (경찰 현장 검증)"
MAN = ("a calm middle-aged Japanese man in a dark wool overcoat with a white cloth armband on his upper arm, "
       "carrying a small leather doctor's bag, his face never visible (seen from behind or in silhouette)")
BANKIN = ("a small 1948 Japanese bank branch office: dark wooden counters and desks, ledgers, abacuses, "
          "a cast-iron stove, frosted glass windows, a wall clock")


def L(t, e="normal", q=False):
    return (t, e, "q") if q else (t, e)


SCENES = [
# ⓪ 도입 (1분 샘플과 같은 구성)
dict(id="f01", foot=OT, t0=6.0, cap="점령기 도쿄 (1945, 미군 촬영)", lines=[L("안녕하세요! 마지막 목격자입니다.")]),
dict(id="f02", foot=JT, t0=12.0, cap="도쿄 거리 (1946, 뉴스영화)", lines=[L("오늘은 1948년 도쿄의 한 은행에서,")]),
dict(id="p02", photo=BANK, cap="1948.1.27 제국은행 시이나마치 지점", lines=[L("열여섯 명이 낯선 남자가 건넨 약을 스스로 마시고 쓰러진 사건.")]),
dict(id="s02", use="img_s1/s02.png", lines=[L("그중 열두 명이 숨지고 단 네 명만 살아남은, 일본 '데이긴 사건'에 대한 이야기입니다.")]),
dict(id="p03", photo=H20, cap="화가 히라사와 사다미치 (1920년경)", lines=[L("범인으로 지목된 화가, 히라사와 사다미치.")]),
dict(id="p04", photo=H51, cap="히라사와 사다미치 (1951)", lines=[L("1955년 사형이 확정됐습니다.")]),
dict(id="p05", photo=TRIAL, cap="1948.12 1심 재판", hl=[(1040, 200, 1380, 660, 0.8)],
     lines=[L("그런데 법무대신이 여러 번 바뀌었지만, 누구도 그의 사형 집행 명령서에 서명하지 않았죠.")]),
dict(id="p06", photo=HACHI, cap="하치오지 의료교도소 (최근 모습)", lines=[L("결국 그는 체포된 지 39년 만에, 아흔다섯 살의 나이로 감옥 안에서 숨을 거뒀는데요.", "tonedown")]),
dict(id="s05", use="img_s1/s05.png", lines=[L("마지막까지 자신은 범인이 아니라고 말했습니다.", "tonedown")]),
dict(id="p07", photo=POSTER, cap="1948 경찰 수배 전단", hl=[(505, 85, 605, 200, 0.6)], lines=[L("더 이상한 건, 범인의 얼굴을 직접 본 목격자들의 말이었습니다.")]),
dict(id="s07", use="img_s1/s07.png", lines=[L("살아남은 행원 한 명은 법정에서 이렇게 말했죠.")]),
dict(id="p08", photo=TRIAL, cap="1948.12 1심 재판", lines=[L("피고인이 범인이라고 확신합니다.", "tonedown", True)]),
dict(id="s08", use="img_s1/s08.png", lines=[L("하지만 또 다른 생존자의 말은 정반대였습니다."), L("피고인은 그 남자와 같은 사람으로 보이지 않습니다.", "tonedown", True)]),
dict(id="p09", photo=COMPARE, hl=[(300, 120, 770, 760, 0.3), (1100, 150, 1580, 760, 1.1)], lines=[L("같은 남자를 본 마지막 목격자들.", "tonedown")]),
dict(id="p10", photo=REEN, cap=CAP_REEN, lines=[L("그들의 기억은 왜 엇갈렸던 걸까요?")]),
dict(id="f03", foot=OT, t0=20.5, cap="점령기 도쿄 (1945, 미군 촬영)", lines=[L("사건이 일어난 그날로 돌아가 보겠습니다.")]),

# ① 1948년 1월 26일
dict(id="f04", foot=OT, t0=34.5, cap="점령기 도쿄 (1945, 미군 촬영)", lines=[L("1948년 1월 26일 월요일, 도쿄.")]),
dict(id="f05", foot=JT, t0=24.0, cap="도쿄 (1946, 뉴스영화)", lines=[L("전쟁이 끝난 지 2년 반, 도시는 아직 폐허에서 벗어나지 못했고,")]),
dict(id="f06", foot=OT, t0=40.5, cap="점령기 도쿄 (1945, 미군 촬영)", lines=[L("일본은 미군이 이끄는 연합군의 점령 아래 있었습니다.")]),
dict(id="f07", foot=JT, t0=66.0, cap="도쿄 거리 시장 (1946, 뉴스영화)", lines=[L("먹을 것도 약도 모자랐던 시절, 이질이나 발진티푸스 같은 전염병도 수시로 돌았죠.")]),
dict(id="b03", photo=BANK, cap="1948.1.27 제국은행 시이나마치 지점", lines=[L("도쿄 도시마구 시이나마치에 있던 제국은행 시이나마치 지점.")]),
dict(id="b03b", photo=A + "Teikoku_Bank_Head_Office.JPG", cap="제국은행 본점 (1953년경)", lines=[L("이날 오후 세 시, 은행은 평소처럼 영업을 마치고 문을 닫았습니다.")]),
dict(id="b04", use="img_test/b04_bright.png", lines=[L("안에서는 행원들이 하루 장부를 정리하고 있었죠.")]),
dict(id="b04b", prompt=f"Interior of {BANKIN}, late afternoon: about a dozen bank clerks, men and women in 1940s clothes, finishing work at their desks; at the back door a caretaker's wife with a young child looks in.",
     lines=[L("행원들, 그리고 은행 건물에 함께 살던 사환의 가족까지, 건물 안에는 모두 열여섯 명이 있었습니다.")]),
dict(id="b05", dark=True, prompt=f"Seen from inside the dim bank, through a half-open side door: the dark silhouette of {MAN}, backlit by the cold grey light outside so that he is only a black shape; no face, no facial features visible at all.",
     lines=[L("그런데 오후 세 시가 조금 넘었을 무렵, 한 남자가 은행을 찾아왔습니다.", "tonedown")]),
dict(id="b05b", prompt="Close-up of a man's upper arm in a dark wool overcoat wearing a white cloth armband, his gloved hand holding a small leather doctor's bag, framed from the shoulder to the waist, no face, inside a 1948 bank.",
     lines=[L("팔에는 하얀 완장을 차고, 손에는 가방을 들고 있었죠.")]),
dict(id="b06", use="img/b06.png", lines=[L("남자는 명함 한 장을 내밀었습니다."), L("명함에는 후생성 관리라는 직함이 적혀 있었는데요.")]),
dict(id="b07", use="img/b07.png", lines=[L("남자는 침착하게 말을 꺼냈습니다."), L("근처 집에서 집단 이질이 발생했습니다.", "tonedown", True)]),
dict(id="b08", use="img/b08.png", lines=[L("그 집 사람이 오늘 이 은행에 다녀갔으니, 곧 GHQ가 소독을 하러 올 겁니다."), L("그 전에 여러분 모두 예방약을 먹어야 합니다.", "tonedown", True)]),
dict(id="b09", use="img/b09.png", lines=[L("점령군의 이름이 나오자, 아무도 의심하지 않았습니다."), L("행원들은 시키는 대로 각자 찻잔을 들고 남자 앞에 모였죠.")]),

# ② 독
dict(id="c01", use="img/c01.png", lines=[L("남자는 가방에서 작은 약병 두 개를 꺼냈습니다.")]),
dict(id="c01b", photo=A + "reenact_2.png", cap=CAP_REEN, lines=[L("그리고 스포이트로 찻잔마다 약을 조금씩 나눠 담았는데요.")]),
dict(id="c02", use="img/c02.png", lines=[L("그는 약 먹는 법을 아주 꼼꼼하게 설명했습니다.")]),
dict(id="c02b", photo=A + "reenact_1.png", cap=CAP_REEN, lines=[L("이를 상하게 하는 약이니, 혀를 내밀고 그 위에 흘려 넣듯 한 번에 삼키세요.", "tonedown", True)]),
dict(id="c03", photo=A + "reenact_3.png", cap=CAP_REEN, lines=[L("그리고 의심을 없애려는 듯, 자기가 먼저 그 약을 마셔 보였죠.")]),
dict(id="c04", use="img/c04.png", lines=[L("남자의 신호에 맞춰, 열여섯 명이 한꺼번에 첫 번째 약을 삼켰습니다."), L("목이 타는 듯 화끈거렸다고, 살아남은 사람들은 기억합니다.", "tonedown")]),
dict(id="c05", use="img/c05.png", lines=[L("1분쯤 지나, 남자는 두 번째 약을 마시게 했습니다."), L("속을 달래는 약이라고 했지만, 사실 그건 그냥 물이었죠.", "tonedown")]),
dict(id="c06", use="img/c06.png", lines=[L("몇몇은 입을 헹구려고 수돗가로 향했습니다."), L("그런데 몇 걸음 떼지 못하고, 사람들이 하나둘 바닥에 쓰러지기 시작했습니다.", "tonedown")]),
dict(id="c07", use="img/c07.png", lines=[L("정신을 잃은 사람들 사이로, 남자는 아무 일도 없다는 듯 움직였습니다.", "tonedown")]),
dict(id="c08", use="img/c08.png", lines=[L("그리고 책상 위에 있던 현금과 수표를 챙겨, 조용히 은행을 빠져나갔죠.")]),
dict(id="c09", use="img/c09.png", lines=[L("얼마 뒤, 쓰러졌던 여직원 한 명이 가까스로 정신을 차리고 길가까지 기어 나왔습니다."), L("지나가던 사람들이 그녀를 발견하고서야, 은행 안의 일이 세상에 알려졌습니다.")]),
dict(id="c10", use="img/c10.png", lines=[L("현장에서만 열한 명이 숨졌고, 병원으로 옮겨진 한 명도 끝내 깨어나지 못했습니다.", "tonedown"), L("살아남은 사람은 단 네 명.", "tonedown")],
     ov=[("사망 12명 · 생존 4명", "stat", 1)]),
dict(id="c10b", photo=BANK, cap="1948.1.27 사건 다음 날 은행 앞", lines=[L("범인이 가져간 돈은 현금 16만 4천여 엔과 수표 1만 7천여 엔.")]),
dict(id="c11", use="img/c11.png", lines=[L("그리고 남자는 그대로 사라졌습니다.", "tonedown")]),

# ③ 명함
dict(id="d01", photo=POSTER, cap="1948 경찰 수배 전단", lines=[L("경찰이 수사를 시작하자, 놀라운 사실이 드러났습니다.")]),
dict(id="d01b", dark=True, prompt="Two Japanese detectives in 1948 overcoats and fedoras examining papers under a desk lamp in a smoky police office, faces in partial shadow.",
     lines=[L("이 사건 전에도, 똑같은 수법의 시도가 두 번이나 있었던 거죠.")]),
dict(id="d02", prompt="Interior of a small 1947 Japanese bank office in autumn daylight: bank clerks holding small teacups looking puzzled, a man in a dark coat with his back to the camera standing at the table.",
     lines=[L("1947년 10월, 야스다 은행 에바라 지점."), L("한 남자가 똑같이 이질 예방약을 핑계로 행원들에게 약을 먹였지만, 이때는 아무도 죽지 않았습니다.")]),
dict(id="d02b", photo=MATSUI, cap="마쓰이 시게루 박사 (1948.1.29)", lines=[L("그가 내민 명함에는, 마쓰이 시게루라는 실제 후생성 관리의 이름이 적혀 있었죠.")]),
dict(id="d03", prompt="A suspicious Japanese bank branch manager in a 1948 suit standing with arms crossed at his office door, through the glass a man in a dark coat walking away down a winter street, daylight.",
     lines=[L("그리고 데이긴 사건 일주일 전, 미쓰비시 은행 나카이 지점."), L("이번에는 야마구치 지로라는, 세상에 없는 사람의 명함이었는데요."),
            L("지점장이 수상하게 여기고 응하지 않자, 남자는 그대로 돌아갔습니다.")]),
dict(id="d04", prompt="A wooden desk in a 1948 Japanese police office covered with dozens of small business cards arranged in neat rows (blank, no readable text), a magnifying glass and a notebook, daylight from a window.",
     lines=[L("경찰이 붙잡은 단서는 명함이었습니다.")]),
dict(id="d04b", photo=IKII, cap="명함을 추적한 이키이 다메고로 경위 (1948.9)",
     lines=[L("진짜 마쓰이와 명함을 주고받은 사람들을 한 명씩 찾아가, 그 명함을 아직 갖고 있는지 확인하기 시작한 거죠.")]),
dict(id="d05", photo=INVEST, cap="1948.8 히라사와 수사", lines=[L("그리고 사건 일곱 달 뒤인 8월 21일, 홋카이도 오타루에서 한 남자가 체포됩니다.")]),
dict(id="d05b", photo=H20, cap="화가 히라사와 사다미치 (1920년경)", lines=[L("템페라화로 이름이 알려진 쉰여섯 살의 화가, 히라사와 사다미치.")]),
dict(id="d06", prompt="A 1940s Japanese ferry crossing a grey northern strait in daylight, passengers in coats on the deck, two men exchanging small cards near the railing, seen from a distance.",
     lines=[L("히라사와는 1947년, 아오모리와 하코다테를 잇는 연락선에서 마쓰이와 명함을 주고받은 사람이었습니다.")]),
dict(id="d06b", photo=H51, cap="히라사와 사다미치 (1951)", lines=[L("그런데 그 명함을 내놓지 못했죠."), L("지갑을 소매치기 당했다는 게 그의 설명이었습니다.")]),
dict(id="d07", prompt="Close-up of an old 1940s Japanese bank passbook and a stack of old yen banknotes on a wooden table under a bare bulb in a police interrogation room (no readable text).",
     lines=[L("게다가 사건 직후, 그는 다른 사람 이름으로 큰돈을 은행에 맡겼는데, 이 돈이 어디서 났는지 끝내 설명하지 못했습니다.")]),
dict(id="d08", photo=KANDA, cap="1948.9 '히라사와 자백' 호외에 몰린 간다 거리", lines=[L("처음엔 혐의를 부인하던 히라사와는, 한 달 넘는 조사 끝에 범행을 자백합니다.")]),
dict(id="d08b", photo=TRIAL, cap="1948.12 1심 재판", hl=[(1040, 200, 1380, 660, 0.4)], lines=[L("하지만 재판이 시작되자 자백을 뒤집었죠.")]),
dict(id="d08c", photo=YAMADA, cap="변호인 야마다 요시오 (1948.9)", lines=[L("강압적인 조사 때문에 거짓으로 자백했다는 겁니다.")]),
dict(id="d09", prompt="Close-up of an old glass syringe and a small vaccine vial on a metal tray in a 1920s Japanese clinic, soft sepia daylight.",
     lines=[L("변호인들은 히라사와가 젊은 시절 맞은 광견병 예방 주사의 부작용으로, 기억이 흐려지고 없는 이야기를 지어내는 증상을 겪었다고 주장했습니다.")]),
dict(id="d10", photo=COMPARE, hl=[(300, 120, 770, 760, 0.3), (1100, 150, 1580, 760, 1.0)], lines=[L("그리고 다시, 마지막 목격자들.", "tonedown")]),
dict(id="d10b", use="img_s1/s07.png", lines=[L("범인과 마주 앉아 직접 이야기를 나눈 지점장 대리는, 히라사와가 범인이 틀림없다고 증언했습니다.")]),
dict(id="d10c", use="img_s1/s08.png", lines=[L("하지만 다른 생존자는 같은 사람으로 보이지 않는다고 말했죠.")]),
dict(id="d11", photo=TRIAL, cap="1948.12 1심 재판", lines=[L("1950년 1심 사형, 1951년 2심도 사형.")]),
dict(id="d11b", dark=True, prompt="A judge's wooden gavel and a thick bound court document on a bench in a 1950s Japanese courtroom, dramatic side light.",
     lines=[L("그리고 1955년, 최고재판소가 상고를 기각하면서 사형이 확정됩니다.", "tonedown")]),
dict(id="d12", prompt="A dark wood Japanese government office desk in the 1960s with a single document and a capped fountain pen lying beside it, an empty leather chair, daylight through tall windows.",
     lines=[L("그런데 그 뒤로 이상한 일이 이어졌습니다."), L("법무대신이 몇 번이나 바뀌었지만, 아무도 히라사와의 사형 집행 명령서에 서명하지 않았던 거죠.")]),
dict(id="d12b", photo=H51, cap="히라사와 사다미치 (1951)", lines=[L("그 사이 히라사와는 열여덟 번이나 재심을 청구했고, 모두 받아들여지지 않았습니다.")]),
dict(id="d13", photo=HACHI, cap="하치오지 의료교도소 (최근 모습)", lines=[L("1987년 5월 10일, 히라사와는 하치오지 의료교도소에서 폐렴으로 숨을 거뒀습니다.", "tonedown")]),
dict(id="d13b", use="img_s1/s05.png", lines=[L("나이 아흔다섯, 체포된 지 39년 만이었습니다.", "tonedown")]),

# ④ 진범
dict(id="e01", photo=POSTER, cap="1948 경찰 수배 전단", hl=[(505, 85, 605, 200, 0.5)], lines=[L("그렇다면 진짜 범인은 따로 있었던 걸까요?")]),
dict(id="e01b", prompt="Close-up of laboratory glassware, small brown chemical bottles and a precise brass balance scale on a wooden bench in a 1940s laboratory, daylight from a window.",
     lines=[L("많은 사람들이 주목한 건, 범인이 독을 다룬 솜씨였습니다.")]),
dict(id="e01c", photo=A + "reenact_4.png", cap=CAP_REEN,
     lines=[L("양을 정확히 나눠 담았고, 자기가 먼저 마시고도 멀쩡했으며, 사람들이 한꺼번에 삼키도록 마시는 법까지 정해 줬죠.")]),
dict(id="e02", dark=True, prompt="An abandoned 1940s military research facility in Manchuria in snow, barbed wire fence, a dark brick building, overcast sky.",
     lines=[L("그래서 수사 초기에는 옛 일본군의 독극물 연구자들, 특히 세균전 부대로 악명 높은 731부대 출신들이 용의선상에 올랐습니다.")]),
dict(id="e02b", prompt="An old handwritten Japanese police notebook lying open on a desk next to a fountain pen and a teacup, 1948, the handwriting blurred and unreadable, soft daylight.",
     lines=[L("당시 수사 간부가 남긴 수기에도, 군 관계자를 쫓은 기록이 남아 있는데요.")]),
dict(id="e03", photo=H20, cap="화가 히라사와 사다미치 (1920년경)", lines=[L("하지만 어느 순간, 수사의 방향은 군 관계자에서 화가 한 사람으로 바뀌었습니다.")]),
dict(id="e03b", foot=JT, t0=14.5, cap="점령기 도쿄 (1946, 뉴스영화)",
     lines=[L("점령군이 이 부대의 연구 자료를 넘겨받는 대가로 관계자들을 보호했다는 사실이 훗날 알려지면서, 이 사건에도 같은 그림자가 드리운 게 아니냐는 의혹이 지금까지 이어지고 있죠.")]),
dict(id="e04", prompt="A small simple grave in a quiet Japanese cemetery at dusk, incense smoke rising, a single white chrysanthemum, soft warm light.",
     lines=[L("히라사와가 세상을 떠난 뒤에도 가족들은 재심 청구를 이어갔지만, 재심의 문은 아직 열리지 않았습니다.")]),
dict(id="e05", photo=BANK, cap="1948.1.27 제국은행 시이나마치 지점", lines=[L("그날 은행 안에서 범인의 얼굴을 본 사람은 단 네 명.", "tonedown")]),
dict(id="e05b", prompt=f"Interior of {BANKIN}, empty, late afternoon golden light fading through frosted windows, small teacups left on the desks, dust in the light beam.",
     lines=[L("그들의 기억은 끝내 하나가 되지 못했고, 진실은 지금도 그날 오후 세 시의 은행 안에 머물러 있습니다.", "tonedown")]),
dict(id="f08", foot=OT, t0=47.5, cap="점령기 도쿄 (1945, 미군 촬영)", lines=[L("지금까지 마지막 목격자였습니다.")]),
dict(id="f09", use="img_full/e05b.png", blur=True, endcard=True,     # 엔딩 좋아요·구독(2026-10-02 사용자 요청)
     lines=[L("영상이 재미있었다면 좋아요와 구독 부탁드립니다.")]),
]
