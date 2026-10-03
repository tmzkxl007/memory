# 마지막 목격자 4편 「디아틀로프 사건」 — 새 편 표준(ep03_ripper 템플릿)
# 사실 근거: en.wikipedia "Dyatlov Pass incident" (우랄 공대, 이고리 디아틀로프 23세, 목표 오토르텐산·3급 난이도, 1959.1.23 스베르들롭스크 출발 10명,
#   1.27 산행 시작, 1.28 유리 유딘 무릎·관절 통증으로 돌아감, 1.31 고원 가장자리, 2.1~2 홀라트시아흘 동쪽 비탈 야영, 텐트 안에서 찢고 나감·짐과 신발 그대로,
#   양말·한쪽 신발·맨발 발자국 9명 1.5km 숲 가장자리, 500m 뒤 눈에 덮임, 시베리아소나무 아래 작은 불·가지 5m 높이까지 부러짐,
#   2.26 수색대가 텐트 발견, 소나무 아래 도로셴코·크리보니셴코, 소나무와 텐트 사이 디아틀로프·콜모고로바·슬로보딘(저체온), 5.4 골짜기 눈 4m 아래 4명
#   (티보브리뇰·두비니나·졸로타료프 큰 부상, 겉 상처는 거의 없음, 콜레바토프 저체온), 두비니나가 크리보니셴코의 바지를 입고 있음, 한 명의 옷에서 방사능,
#   일기·카메라로 전날까지 경로 확인, 처음엔 원주민 만시족 의심 → 다른 발자국·몸싸움 흔적 없어 배제, 1959.5 '저항할 수 없는 자연의 힘'으로 종결,
#   유딘 2013.4.27 사망 75세, 2019.2 재조사 → 2020 쿠랴코프 "눈사태가 공식 사인… 영웅적인 싸움이었다", 2021 가움·푸즈린 「Communications Earth & Environment」
#   28도 비탈 위 바람에 쌓인 작은 눈판 붕괴로 텐트 손상·부상 설명 가능), 수색대: 학생·교사 자원봉사 → 군·경찰·비행기·헬기
# 실제 자료: 1959 수색대 텐트 사진·수사 기록 원본(PD), 1958년 디아틀로프가 참가한 아극 우랄 겨울 원정 사진(표트르 바르톨로메이, CC BY-SA 2.0),
#   추모비 사진(PD/CC BY-SA), 지도(Merikanto, CC BY-SA), 오토르텐 풍경(CC BY/BY-SA), 1901 만시족 가족(PD), 만시족 천막(CC0)
# 수위: 시신·부상은 묘사하지 않는다. 1958 사진은 '1958년 다른 원정'이라고 분명히 말한다(1959 원정 사진처럼 쓰지 않음).
STYLE = ("Photorealistic cinematic documentary reenactment still, shot on 35mm film, subtle film grain, muted cold colors. "
         "Setting: the Northern Ural Mountains, Soviet Union, winter 1959 — deep snow, sparse frozen conifer forest, bare windswept slopes, "
         "Soviet students in 1950s woolen ski clothing, canvas tents, wooden skis. Wide 16:9 full-bleed frame, no border. "
         "No blood, no gore, no bodies, no injuries. Absolutely no text, no letters, no numbers, no readable signs, no captions, no watermark, no logo.")
DARK = " Night, blizzard or deep blue darkness, very cold, tense eerie atmosphere."
BRIGHT = ("Photorealistic documentary reenactment photo, soft overcast winter daylight, realistic muted colors, evenly lit and clearly visible, "
          "like a high-quality stock photo used in a TV documentary. Soviet Union 1959, people in period winter clothing. "
          "16:9 full-bleed. No blood, no gore, no bodies. Absolutely no text, no letters, no readable signs, no watermark.")
TTS_FIX = {}
NAMES = ["이고리 디아틀로프", "유리 유딘", "유리 도로셴코", "류드밀라 두비니나", "게오르기 크리보니셴코", "알렉산드르 콜레바토프", "지나이다 콜모고로바",
         "루스템 슬로보딘", "니콜라이 티보브리뇰", "세묜 졸로타료프", "홀라트시아흘", "오토르텐", "스베르들롭스크", "우랄 공대", "만시족"]
VOICE = None
TTS_DIR, IMG_DIR, OUTNAME = "tts_dy", "img_dy", "final_dy"
TVOFF = True
GRADE = True
NOCAP = True
INTRO = dict(music="music/gnossienne1.ogg", music_list=["music/gnossienne1.ogg"], through=True,
             lead=2.4, at=1.6, offset=0.0, end_scene="a08", gain=0.31, body_gain=0.16)

A = "archive/"
TENT = A + "Dyatlov_Pass_incident_02.jpg"
H58A, H58B, H58C, H58D = (A + "Pohod_na_Pripolarnyi_Ural_anvar__1958_goda_.jpg", A + "Pohod_na_Pripolarnyi_Ural_anvar__1958_goda_-_51906749096.jpg",
                          A + "Pohod_na_Pripolarnyi_Ural_anvar__1958_goda_-_51906843848.jpg", A + "Pohod_na_Pripolarnyi_Ural_anvar__1958_goda_-_51906847458.jpg")
GRAVE9 = A + "Foto_clenov_turgruppy_Igora_Datlova.jpg"
COVER, P1, P370, P384 = A + "Dyatlov.Volume_1.Original_cover.jpg", A + "Dyatlov.Volume_1.Page_1.jpg", A + "Dyatlov.Volume_1.Page_370.jpg", A + "Dyatlov.Volume_1.Page_384.jpg"
MAP_T, MAP_C, MAP_B, MAP_AV = (A + "Dyatlov_pass_incident_accurate_mountain_and_tent_map_2.png", A + "Dyatlov_pass_incident_accurate_fancy_map_4.png",
                               A + "Dyatlov_pass_incident_accurate_fancy_map_3.png", A + "Dyatlov_pass_incident_avalanche_possibility_map_1.png")
OTOR, OTOR2, FOREST = A + "Gora_Otorten._Severoural_skii_minimalizm.jpg", A + "Vid_s_Otortena_-_panoramio.jpg", A + "Zimnii_ural_skii_les.jpg"
MANSI, CHUM, MEMO, CEM = A + "Family_of_Mansi_1901.png", A + "Chum_-_The_Museum_of_History_and_Archeology_of_the_Urals.jpg", A + "Pamatnik_datlovcam_na_Mihailovskom_kladbise.jpg", A + "Mikhailovskoe_Cemetery_in_Yekaterinburg_June_2024_-_2.jpg"
TENTSLOPE = "a small Soviet canvas ridge tent pitched on a bare, windswept snowy mountain slope above the treeline, skis stuck upright in the snow beside it"


def L(t, e="normal", q=False):
    return (t, e, "q") if q else (t, e)


SCENES = [
# ⓪ 도입
dict(id="a01", photo=TENT, lines=[L("마지막 목격자.")]),
dict(id="a02", photo=GRAVE9, lines=[L("오늘은 1959년 겨울, 소련 우랄산맥에서 대학생 아홉 명이 한꺼번에 숨진 채 발견된 사건.")]),
dict(id="a03", photo=OTOR, lines=[L("60년이 넘도록 수많은 가설을 낳은 미스터리, '디아틀로프 사건'에 대한 이야기입니다.")]),
dict(id="a04", dark=True, prompt=f"Night blizzard on a bare snowy mountain slope: {TENTSLOPE}, the tent wall slashed open from the inside, flapping in the wind, a faint glow of a flashlight inside. No people.",
     lines=[L("영하 30도의 한밤중, 그들은 텐트를 안에서 찢고 뛰쳐나갔습니다.", "tonedown")]),
dict(id="a05", prompt="Extreme close-up of a line of footprints in deep snow made by feet in woolen socks, some barefoot prints, leading down a slope into grey mist.",
     lines=[L("신발도 신지 않은 채, 양말이나 맨발로 눈 덮인 비탈을 1.5킬로미터나 내려갔죠.")]),
dict(id="a06", photo=P384, lines=[L("소련 수사 당국이 내린 결론은 단 한 줄이었습니다.")]),
dict(id="a07", dark=True, qcard=True, prompt="A dark frozen forest edge at night, a tall lone Siberian pine tree, snow swirling, deep blue darkness.",
     lines=[L("저항할 수 없는 자연의 힘, 그날 밤 그 산에서는 대체 무슨 일이 있었던 걸까요?")]),
dict(id="a08", photo=OTOR2, lines=[L("그들의 마지막 여정을 따라가 보겠습니다.")]),

# ① 원정대
dict(id="b01", prompt="A 1950s Soviet university corridor in winter daylight: students in woolen sweaters carrying skis and rucksacks, a hiking club notice board (blank, no readable text).",
     lines=[L("1959년 1월, 스베르들롭스크의 우랄 공과대학."), L("학생 산악 동아리의 이고리 디아틀로프가 겨울 원정을 준비하고 있었습니다.")]),
dict(id="b02", photo=H58B, lines=[L("스물세 살의 디아틀로프는 이미 여러 차례 겨울 산행을 이끈 베테랑이었죠."),
                                   L("이 사진도 1년 전, 그가 참가한 다른 겨울 원정에서 찍힌 모습입니다.")]),
dict(id="b03", photo=OTOR, lines=[L("목표는 북부 우랄의 오토르텐산."), L("당시 기준으로 가장 어려운 3급 코스였습니다.")]),
dict(id="b04", use="cards/roster.png", lines=[L("대원은 모두 열 명."), L("대부분 스무 살 남짓한 우랄 공대 학생과 졸업생이었고, 단 한 명, 스키·등산 강사 자격을 준비하던 서른여덟 살의 세묜 졸로타료프가 함께했죠.")]),
dict(id="b05", prompt="A 1950s Soviet steam train interior in winter: young students in woolen hats laughing and singing with a guitar among rucksacks and skis, frosted windows.",
     lines=[L("1월 23일, 일행은 기차를 타고 스베르들롭스크를 떠났습니다."), L("남겨진 일기와 사진 속 그들은 노래를 부르고 농담을 주고받는 평범한 대학생들이었습니다.")]),
dict(id="b06", photo=H58D, lines=[L("기차와 트럭을 갈아타고 도착한 마지막 마을에서부터는 스키를 타고 걸어서 가야 했죠.")]),

# ② 돌아간 한 명
dict(id="c01", prompt="A young Soviet man in a 1950s winter jacket sitting on a sled at the edge of a snowy forest, holding his knee, looking back at a line of skiers disappearing into the trees.",
     lines=[L("1월 28일, 대원 한 명이 발길을 돌립니다."), L("스물한 살 유리 유딘이었습니다.")]),
dict(id="c02", prompt="Close-up of two young men's gloved hands shaking goodbye in a snowy forest, one holding ski poles, breath steaming in the cold air.",
     lines=[L("무릎과 관절 통증 때문에 더 이상 걸을 수 없었던 거죠."), L("친구들과 작별 인사를 나눈 그는, 혼자 마을로 돌아갔습니다.")]),
dict(id="c03", photo=GRAVE9, lines=[L("그것이 그가 친구들을 본 마지막 모습이었습니다.", "tonedown"), L("그리고 유딘은 디아틀로프 원정대에서 살아남은 단 한 사람이 됐습니다.")]),

# ③ 마지막 밤
dict(id="d01", photo=H58C, lines=[L("남은 아홉 명은 계속 북쪽으로 나아갔습니다.")]),
dict(id="d02", prompt="A line of nine Soviet skiers with heavy rucksacks crossing a vast white plateau under a grey sky in 1959, seen from far away, wind blowing snow.",
     lines=[L("1월 31일, 숲이 끝나는 고원의 가장자리에 다다랐고, 다음 날 일행은 고개를 넘기 시작합니다.")]),
dict(id="d03", photo=MAP_T, lines=[L("2월 1일 저녁, 그들은 홀라트시아흘이라는 산의 비탈에 텐트를 쳤습니다.")]),
dict(id="d04", dark=True, prompt="Dusk on a bare snowy mountain slope with a view down to a dark forest valley: " + TENTSLOPE + ", soft lamplight glowing through the canvas.",
     lines=[L("현지 원주민인 만시족의 말로 '죽은 산'이라는 뜻이라고 알려진 곳이었죠."),
            L("숲까지 내려가면 바람을 피할 수 있었지만, 그들은 바람이 몰아치는 비탈 한가운데를 골랐습니다.")]),
dict(id="d05", dark=True, prompt="Inside a crowded Soviet canvas tent at night, warm lamplight: woolen mittens, a notebook, a small stove pipe, rucksacks and boots lined up, steam from tea mugs. No faces.",
     lines=[L("텐트 안에서 그들은 저녁을 먹고, 일기를 쓰고, 잠자리에 들었을 겁니다.")]),
dict(id="d06", dark=True, prompt="Extreme close-up of a 1950s Soviet camera and a small open diary on a rolled sleeping bag in a dark tent, lamplight going out.",
     lines=[L("그들이 남긴 일기와 카메라에는, 바로 그 전날까지의 여정이 고스란히 남아 있었습니다."), L("그리고 그날 밤의 기록은 아무것도 없었죠.", "tonedown")]),

# ④ 수색
dict(id="e01", prompt="A 1959 Soviet sports club office in winter: worried parents in coats and a university official at a desk with a telephone, a wall map of the Urals (no readable text).",
     lines=[L("원래대로라면 2월 12일쯤 마을에 도착해 무사하다는 전보를 보냈어야 했습니다."), L("하지만 소식이 오지 않았고, 가족들의 걱정이 커졌죠.")]),
dict(id="e02", prompt="A Soviet search party in 1959: students and soldiers on skis with long probe poles, a small biplane flying low over a snowy ridge in the background.",
     lines=[L("2월 20일, 대학은 학생과 교사들로 수색대를 꾸렸고, 곧 군과 경찰, 비행기와 헬기까지 동원됐습니다.")]),
dict(id="e03", photo=TENT, hl=[(140, 230, 680, 520, 1.0)], lines=[L("그리고 2월 26일, 수색대는 홀라트시아흘 비탈에서 반쯤 무너져 눈에 덮인 텐트를 발견합니다.")]),
dict(id="e04", photo=TENT, lines=[L("텐트는 텅 비어 있었습니다."), L("짐과 신발, 겉옷이 모두 안에 그대로 남아 있었죠.")]),
dict(id="e05", prompt="Extreme close-up of a long knife cut through stiff frozen canvas tent fabric, seen from the inside out, snow beyond the slit.",
     lines=[L("그런데 텐트의 한쪽 벽이 칼로 찢겨 있었습니다."), L("조사 결과, 누군가 밖에서가 아니라 안에서 찢고 나간 것이었죠.", "tonedown")]),
dict(id="e06", prompt="A long line of faint footprints in snow leading down a bare mountain slope toward a distant dark forest edge, grey overcast day, search party members standing at the top looking down.",
     lines=[L("텐트 밖에는 아홉 명의 발자국이 숲 쪽으로 이어져 있었습니다."), L("양말만 신거나 신발을 한 짝만 신은 발자국, 맨발 자국도 있었죠."),
            L("발자국은 500미터쯤 이어지다가 눈에 덮여 사라졌습니다.")]),

# ⑤ 소나무 아래
dict(id="f01", photo=MAP_C, lines=[L("1.5킬로미터 떨어진 숲 가장자리, 커다란 시베리아소나무 아래.")]),
dict(id="f02", prompt="The base of a huge old Siberian pine at a snowy forest edge in grey daylight: the black remains of a small campfire in the snow, broken branches scattered around. No people.",
     lines=[L("수색대는 작은 모닥불의 흔적과 함께, 첫 번째 두 사람을 찾아냈습니다."), L("유리 도로셴코와 게오르기 크리보니셴코였죠.")]),
dict(id="f03", prompt="Looking up the trunk of a tall Siberian pine in winter: branches snapped off high up the trunk, about five meters above the snow, grey sky.",
     lines=[L("소나무 가지는 5미터 높이까지 부러져 있었습니다."), L("누군가 나무 위로 올라가 텐트 쪽을 살폈던 것처럼 보였죠.")]),
dict(id="f04", photo=MAP_B, lines=[L("그리고 소나무와 텐트 사이의 비탈에서, 세 사람이 더 발견됩니다."),
                                    L("대장 이고리 디아틀로프, 지나이다 콜모고로바, 루스템 슬로보딘."),
                                    L("세 사람은 마치 텐트로 돌아가려던 것처럼, 텐트 쪽을 향해 쓰러져 있었습니다.", "tonedown")]),
dict(id="f05", prompt="Close-up of a gloved hand of a searcher holding a long wooden probe pole pushed into deep snow, the slope and tiny far-away tent in the background.",
     lines=[L("다섯 명의 사인은 모두 저체온증이었습니다."), L("하지만 나머지 네 명은 어디에도 없었죠.")]),

# ⑥ 골짜기의 네 사람
dict(id="g01", prompt="Spring thaw in the Northern Urals: a deep snow-filled ravine by a forest stream, melting snow walls about four meters deep, search team with shovels standing at the edge. Nothing visible in the snow.",
     lines=[L("눈이 녹기 시작한 5월 4일, 소나무에서 75미터쯤 떨어진 골짜기."), L("4미터 깊이의 눈 아래에서 마지막 네 사람이 발견됩니다.")]),
dict(id="g02", photo=GRAVE9, lines=[L("류드밀라 두비니나, 세묜 졸로타료프, 니콜라이 티보브리뇰, 알렉산드르 콜레바토프.")]),
dict(id="g03", dark=True, prompt="A dim 1959 Soviet forensic office: a doctor in a white coat writing a report at a desk under a lamp, X-ray films clipped to a light box (no readable details).",
     lines=[L("그런데 이 네 사람은 앞의 다섯과 달랐습니다."), L("세 사람은 두개골과 가슴뼈가 크게 부러져 있었죠."),
            L("검시관은 자동차에 치인 것 같은 강한 충격이라고 했는데, 정작 겉으로 보이는 상처는 거의 없었습니다.", "tonedown")]),
dict(id="g04", prompt="Close-up of mismatched burnt and torn 1950s woolen trousers and a knitted sweater lying on a wooden table in a cold morgue storeroom, evidence tags (blank).",
     lines=[L("게다가 두비니나는 동료 크리보니셴코의 바지를 입고 있었습니다."), L("먼저 숨진 친구들의 옷을 벗겨 입은 것으로 보였죠.")]),
dict(id="g05", photo=P370, lines=[L("이상한 점은 또 있었습니다."), L("한 사람의 옷에서 방사능이 검출된 겁니다."), L("수사관은 곧바로 방사능 감정을 의뢰했습니다.")]),

# ⑦ 수사와 결론
dict(id="h01", photo=MANSI, lines=[L("처음 의심을 받은 건 이 지역의 원주민인 만시족이었습니다."), L("자기들의 땅에 들어온 외지인을 공격했다는 거였죠.")]),
dict(id="h02", photo=CHUM, lines=[L("하지만 현장에는 아홉 명 말고 다른 사람의 발자국이 없었고, 몸싸움의 흔적도 없었습니다."), L("만시족은 곧 혐의를 벗었죠.")]),
dict(id="h03", photo=COVER, lines=[L("그리고 1959년 5월 28일, 수사는 갑자기 끝이 납니다.")]),
dict(id="h04", photo=P384, hl=[(150, 1500, 2150, 2400, 0.8)], lines=[L("결론은 아홉 명이 저항할 수 없는 자연의 힘에 의해 숨졌다는 것."),
                                                                          L("무엇이 그 힘이었는지는, 아무도 설명하지 않았습니다.", "tonedown")]),
dict(id="h05", prompt="A 1959 Soviet archive storeroom: rows of grey metal shelves with tied cardboard case folders, a single bare bulb, dust in the light.",
     lines=[L("사건 기록은 기밀 문서보관소로 들어갔고, 사람들은 저마다의 상상으로 그 빈자리를 채우기 시작했습니다.")]),

# ⑧ 가설들
dict(id="i01", use="cards/theories.png", lines=[L("눈사태, 산을 타고 내려오는 강한 돌풍, 사람을 공포에 빠뜨리는 초저주파."),
                                                L("소련군의 비밀 무기 실험, 낙하산 폭탄, 심지어 설인과 미확인 비행 물체까지.")]),
dict(id="i02", dark=True, prompt="Night sky over a snowy Ural mountain ridge with a strange bright glowing orb of light high in the sky and a faint trail, dark silhouettes of conifers in the foreground.",
     lines=[L("그해 이 지역 하늘에서 이상한 빛을 봤다는 목격담도 있었죠."), L("주황색 빛 덩어리가 2월부터 3월까지 근처 하늘에서 계속 보였다는 기록이 남아 있지만, 그 정체는 끝내 밝혀지지 않았습니다.")]),
dict(id="i03", photo=MAP_AV, lines=[L("가장 오래, 가장 많이 반박된 가설은 눈사태였습니다."),
                                      L("텐트가 있던 비탈은 경사가 완만해 보였고, 수색대가 왔을 때 눈사태의 뚜렷한 흔적도 없었기 때문이죠.")]),

# ⑨ 60년 뒤
dict(id="j01", prompt="A modern Russian prosecutor's office with a large window, thick old case folders tied with string stacked on a desk next to a modern laptop, winter daylight.",
     lines=[L("그리고 60년 뒤인 2019년 2월, 러시아 검찰이 사건을 다시 열었습니다.")]),
dict(id="j02", use="cards/conclusion.png", lines=[L("2020년 검찰은 공식 사인을 눈사태로 발표했습니다."),
                                                  L("그들은 공황에 빠지지 않았다, 다만 그 상황에서 스스로를 구할 방법이 없었다고 말했죠.")]),
dict(id="j03", prompt="Close-up of a modern laboratory: a researcher's hands next to a slanted model of a snowy slope with a small tent model on it, a computer screen showing a snow simulation (no readable text).",
     lines=[L("2021년에는 스위스 연구진이 과학 학술지에 논문을 발표합니다."),
            L("텐트 바로 위 28도 비탈에 바람에 실려 온 눈이 쌓여, 작은 눈판이 무너져 내렸다면,"),
            L("텐트가 찌그러지고 대원들이 그런 부상을 입는 일이 충분히 가능했다는 겁니다.")]),
dict(id="j04", dark=True, prompt=f"Night: heavy snow sliding down onto {TENTSLOPE}, the snow slab pressing in the tent roof, wind and snow swirling. No people visible.",
     lines=[L("한밤중 텐트 위로 갑자기 눈이 쏟아지자, 대원들은 더 큰 눈사태가 올까 봐 텐트를 찢고 아래 숲으로 피했을 것이고,"),
            L("돌아갈 길을 잃은 채 혹독한 추위 속에 하나둘 쓰러졌을 거라는 설명이죠.", "tonedown")]),
dict(id="j05", photo=FOREST, lines=[L("하지만 이 설명에도 모든 의문이 풀린 것은 아닙니다."), L("방사능과, 사라진 옷과, 골짜기의 네 사람."),
                                     L("사람들은 지금도 그날 밤의 진실을 두고 논쟁하고 있습니다.")]),

# ⑩ 마무리
dict(id="k01", photo=GRAVE9, lines=[L("유리 유딘은 평생 친구들의 죽음의 진실을 찾고 싶어 했습니다."), L("그리고 2013년, 일흔다섯의 나이로 세상을 떠났죠.")]),
dict(id="k02", photo=MEMO, lines=[L("아홉 명은 지금 예카테린부르크의 묘지에 함께 잠들어 있습니다."), L("그리고 그들이 숨진 고개에는, 대장의 이름을 딴 '디아틀로프 고개'라는 이름이 붙었습니다.")]),
dict(id="k03", photo=OTOR2, lines=[L("그날 밤 그 산에는, 그들 말고는 아무도 없었습니다.", "tonedown")]),
dict(id="k04", dark=True, qcard=True, use="img_dy/a04.png", lines=[L("마지막 목격자는 그 산과 바람, 그리고 눈뿐이었습니다.")]),
dict(id="k05", photo=TENT, lines=[L("지금까지 마지막 목격자였습니다.")]),
dict(id="k06", use="img_dy/a07.png", blur=True, endcard=True, lines=[L("영상이 재미있었다면 좋아요와 구독 부탁드립니다.")]),
]
