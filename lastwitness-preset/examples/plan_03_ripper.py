# 마지막 목격자 3편 「잭 더 리퍼」 — 새 편 표준(2편 에드 게인 방식) 그대로
# 사실 근거: en.wikipedia "Jack the Ripper" (화이트채플 약 8만 명·숙소 233곳 매일 밤 약 8,500명·성매매 여성 약 1,200명 추정·아이 55%가 5세 전 사망,
#   니콜스 8.31 03:40 벅스 로(43세), 채프먼 9.8 06:00 행버리 가 29번지 뒤뜰(47세), 스트라이드 9.30 01:00 더트필드 야드(44세, 디엠슈츠 발견),
#   에도우스 9.30 01:44 마이터 광장(46세, 45분 뒤), 켈리 11.9 10:45 밀러스 코트 13호(25세 무렵, 집세 받으러 간 사람 발견),
#   목격자 엘리자베스 롱 05:30(사슴 사냥 모자·어두운 외투·'가난하지만 점잖은'), 이즈리얼 슈워츠 00:45, 조지프 라웬드 01:35(30세쯤·밝은 콧수염·모자·뱃사람 같은 차림),
#   조지 허친슨 02:00(사흘 뒤 경찰에, 잘 차려입은 남자·매우 자세한 묘사), '친애하는 보스' 9.25 작성·9.27 소인·통신사, '건방진 재키' 엽서 10.1 '이중 사건',
#   '지옥에서' 10.16 조지 러스크·장기 일부, 굴스턴 가 02:55 앞치마 조각·분필 낙서·워런이 지움, 가죽 앞치마 존 파이저 알리바이로 석방,
#   2천 명 조사·3백 명 넘게 수사·80명 구금·도축업자 76명, 신문 하루 100만 부 넘게, 블러드하운드 시험, 자경단, 맥노튼 비망록 1894(드루이트·코스민스키·오스트로그),
#   용의자 100명 넘게(시커트·루이스 캐럴 등), 2014 숄 DNA 주장과 비판, 1931 기자 프레드 베스트 편지 작성 고백 주장)
# 수위: 피해자 시신·상처는 묘사하지 않는다. 영안실·현장 사진 쓰지 않음. 피 흘리는 컬러 판화 제외.
# 나레이션 = 사용자 mp3 → ../import_mp3.py (tts_jr). 실제 자료 = archive/sources.json (위키미디어 공용 퍼블릭 도메인/CC0), 1896 블랙프라이어스 기록 영상(로고 없음)
STYLE = ("Photorealistic cinematic documentary reenactment still, shot on 35mm film, subtle film grain, muted natural colors. "
         "Setting: Whitechapel, East End of London, autumn 1888 — Victorian working-class people in period clothing, narrow cobblestone alleys, "
         "gas street lamps, soot-stained brick tenements, horse carts. Wide 16:9 full-bleed frame, no border. "
         "No blood, no gore, no bodies, no injuries, no weapons in use. "
         "Absolutely no text, no letters, no numbers, no readable signs, no captions, no watermark, no logo.")
DARK = " Night, thick fog, dim gaslight, deep shadows, tense eerie atmosphere."
BRIGHT = ("Photorealistic documentary reenactment photo, soft overcast daylight, realistic muted colors, evenly lit and clearly visible, "
          "like a high-quality stock photo used in a TV documentary. Victorian London 1888, people in period clothing. "
          "16:9 full-bleed. No blood, no gore, no bodies. Absolutely no text, no letters, no readable signs, no watermark.")
TTS_FIX = {}
NAMES = ["잭 더 리퍼", "메리 앤 니콜스", "애니 채프먼", "엘리자베스 스트라이드", "캐서린 에도우스", "메리 제인 켈리", "엘리자베스 롱", "이즈리얼 슈워츠",
         "조지프 라웬드", "조지 허친슨", "루이스 디엠슈츠", "찰스 워런", "조지 러스크", "프레더릭 애버라인", "멜빌 맥노튼", "몬터규 드루이트", "아론 코스민스키",
         "마이클 오스트로그", "프랜시스 텀블티", "월터 시커트", "루이스 캐럴", "존 파이저", "화이트채플", "더트필드 야드", "마이터 광장", "밀러스 코트", "굴스턴 가"]
VOICE = None
TTS_DIR, IMG_DIR, OUTNAME = "tts_jr", "img_jr", "final_jr"
TVOFF = True
GRADE = True
NOCAP = True   # 영상 왼쪽 위 출처·날짜 표시 빼기(사용자 2026-10-03) — 출처는 업로드 설명란에만
INTRO = dict(music="music/gnossienne1.ogg", music_list=["music/gnossienne1.ogg"], through=True,
             lead=2.4, at=1.6, offset=0.0, end_scene="a08", gain=0.31, body_gain=0.16)

A = "archive/"
BF = "footage/blackfriars_1896.webm"; CBF = "런던 블랙프라이어스 다리 (1896 기록 영상)"
ILN = A + "JacktheRipper1888.jpg"; SHEDS = A + "The_Illustrated_London_News_-_October_13_1888_-_Outcast_Sleeping_in_Sheds_in_Whitechapel.jpg"
EAST = A + "JacktheRipperWhitechapelcirca1890.jpg"; BOSS1, BOSS2 = A + "DearBossletterJacktheRipper.jpg", A + "Dear_Boss_pt2.jpg"
LAWENDE = A + "Joseph_Lawende_Jack_the_Ripper_Suspect_1899.jpg"


def L(t, e="normal", q=False):
    return (t, e, "q") if q else (t, e)


SCENES = [
# ⓪ 도입
dict(id="a01", foot=BF, t0=1.0, cap=CBF, lines=[L("마지막 목격자.")]),
dict(id="a02", photo=ILN, cap="1888.10.13 일러스트레이티드 런던 뉴스", lines=[L("오늘은 1888년 가을, 런던에서 가장 가난한 동네를 공포에 빠뜨린 정체불명의 살인마.")]),
dict(id="a03", photo=BOSS1, cap="'친애하는 보스' 편지 (1888.9.25)", lines=[L("스스로 지은 이름으로 경찰과 언론을 조롱했던 남자, 잭 더 리퍼에 대한 이야기입니다.")]),
dict(id="a04", dark=True, prompt="A narrow cobblestone alley in Whitechapel at night in thick fog, a single gas lamp, the distant dark silhouette of a man in a long coat and hat walking away, no face visible.",
     lines=[L("다섯 명의 여성이 희생됐고, 경찰은 2천 명이 넘는 사람을 조사했습니다.")]),
dict(id="a05", prompt="Close-up of a dusty pile of old Victorian police case files tied with string on a wooden desk, an old magnifying glass and an inkwell, soft window light.",
     lines=[L("하지만 130여 년이 지난 지금까지, 그의 정체는 밝혀지지 않았죠.")]),
dict(id="a06", photo=LAWENDE, cap="목격자 조지프 라웬드가 있는 가족 사진 (1899)", lines=[L("그런데 그를 직접 본 사람들이 있었습니다.")]),
dict(id="a07", dark=True, qcard=True, prompt="An empty foggy Victorian London street at night, wet cobblestones reflecting a gas lamp, long shadows.",
     lines=[L("어쩌면 범인의 얼굴을 본 마지막 목격자들, 그들의 기억은 왜 모두 달랐던 걸까요?")]),
dict(id="a08", foot=BF, t0=12.0, cap=CBF, lines=[L("1888년 런던으로 가 보겠습니다.")]),

# ① 화이트채플
dict(id="b01", foot=BF, t0=19.0, cap=CBF, lines=[L("19세기 말 런던은 세계에서 가장 크고 부유한 도시였습니다.")]),
dict(id="b02", photo=EAST, cap="런던 이스트엔드 (1890년경)", lines=[L("하지만 그 동쪽 끝, 화이트채플은 완전히 다른 세상이었죠.")]),
dict(id="b03", photo=SHEDS, cap="1888.10.13 화이트채플 헛간에서 잠든 사람들", lines=[L("좁은 골목에 8만 명이 넘게 몰려 살았고, 싸구려 숙소 233곳에는 매일 밤 8천 5백 명이 잠자리를 구했습니다.")]),
dict(id="b04", prompt="Close-up of a dirty worn hand holding out a few old Victorian copper pennies in a dim lodging-house doorway.",
     lines=[L("침대 하나 값은 4펜스.")]),
dict(id="b05", dark=True, prompt="A dim Victorian lodging house room: rows of tired people sleeping sitting up on a bench, leaning forward over a rope stretched across the room, a single candle.",
     lines=[L("그 돈조차 없는 사람들은 방을 가로지른 밧줄에 기대어 앉은 채 잠들었습니다.")]),
dict(id="b06", prompt="A Whitechapel back alley in grey daylight, 1888: barefoot children in ragged clothes sitting on a doorstep, laundry hanging between soot-stained brick walls.",
     lines=[L("태어난 아이의 절반 넘게 다섯 살을 넘기지 못했다고 하죠.")]),
dict(id="b07", dark=True, prompt="Night in Whitechapel 1888: two women in shawls standing under a gas lamp near a pub door, seen from behind at a distance, fog.",
     lines=[L("경찰은 이곳에서 몸을 팔아 살아가는 여성이 1천 2백 명에 이른다고 추정했습니다."),
            L("그리고 1888년 늦여름, 이 여성들이 하나둘 쓰러지기 시작합니다.", "tonedown")]),

# ② 첫 두 희생자
dict(id="c01", photo=A + "Bucks-Row.jpg", cap="벅스 로 (1888)", name=("메리 앤 니콜스", "1888년 8월 31일 · 43세"),
     lines=[L("1888년 8월 31일 새벽 3시 40분쯤, 벅스 로."), L("일하러 가던 짐마차꾼이 길바닥에 쓰러진 한 여성을 발견합니다.")]),
dict(id="c02", photo=A + "PC_Jonas_Mizen_Discovers_Mary_Ann_Nichols_31_August_1888A.jpg", cap="1888 신문 삽화",
     lines=[L("마흔세 살의 메리 앤 니콜스였죠."), L("경찰이 도착했을 때 그녀는 이미 숨져 있었습니다.", "tonedown")]),
dict(id="c02b", dark=True, prompt="Close-up of a worn woman's hand holding a small new black straw bonnet under a gas lamp outside a Victorian lodging-house door at night, no face visible.",
     lines=[L("그녀는 다섯 아이의 엄마였습니다."), L("술 문제로 남편과 헤어진 뒤, 구빈원과 싸구려 숙소를 떠돌았죠."),
            L("그날 밤 숙소비 4펜스가 없어 쫓겨나면서도, 새로 산 보닛을 자랑하며 금방 돈을 구해 오겠다고 했다고 합니다."),
            L("새벽 2시 반, 함께 방을 쓰던 친구가 그녀를 마지막으로 봤습니다.")]),
dict(id="c03", photo=A + "Hanbury.jpg", cap="행버리 가 (1888)", name=("애니 채프먼", "1888년 9월 8일 · 47세"),
     lines=[L("일주일 뒤인 9월 8일 아침 6시쯤, 행버리 가 29번지 뒤뜰."), L("이번에는 마흔일곱 살의 애니 채프먼이었습니다.")]),
dict(id="c03b", prompt="Close-up of a crocheted lace antimacassar and a small bunch of cheap paper flowers on a worn table in a Victorian lodging-house kitchen, soft grey daylight.",
     lines=[L("그녀에게도 세 아이가 있었습니다."), L("열두 살 큰딸을 병으로 먼저 떠나보냈고, 남편이 세상을 떠나면서 매주 받던 생활비마저 끊겼죠."),
            L("뜨개질한 덮개와 꽃을 팔아 하루하루를 버텼고, 그녀 역시 몇 달 남지 않은 병을 앓고 있었다고 합니다.")]),
dict(id="c04", photo=A + "29_Hanbury_Street.jpg", cap="행버리 가 29번지", lines=[L("그리고 이번에는 목격자가 있었습니다.")]),
dict(id="c05", use="cards/w1.png", lines=[L("새벽 5시 반, 이 집 앞을 지나던 엘리자베스 롱은 애니 채프먼이 한 남자와 이야기하는 모습을 봤습니다."),
                                         L("남자는 사슴 사냥 모자에 어두운 외투를 입은, 가난하지만 점잖아 보이는 사람이었다고 하죠.")]),
dict(id="c06", photo=A + "Wanted_poster.jpg", cap="1888.9 신문 '가죽 앞치마'", lines=[L("신문들은 '가죽 앞치마'라는 별명의 남자를 범인으로 몰아갔습니다."),
                                                                                L("구두공 존 파이저가 체포됐지만, 알리바이가 확인돼 곧 풀려났죠.")]),

# ③ 편지와 이름
dict(id="d01", photo=BOSS1, cap="'친애하는 보스' 편지 (1888.9.25)", hl=[(40, 40, 650, 330, 0.6)],
     lines=[L("9월 27일, 런던의 한 통신사로 붉은 잉크로 쓴 편지 한 통이 도착합니다.")]),
dict(id="d02", photo=BOSS2, cap="'친애하는 보스' 편지 둘째 장", lines=[L("자신이 범인이라고 주장한 이 편지의 끝에는, 이런 서명이 있었습니다."), L("잭 더 리퍼.", "tonedown", True)]),
dict(id="d03", dark=True, prompt="A Victorian newsboy in a flat cap holding up a newspaper on a crowded foggy London street corner, people crowding around to buy papers, the newspaper pages blank and unreadable.",
     lines=[L("신문들이 이 이름을 그대로 실으면서, 이름 없는 살인마는 하룻밤 사이에 전설이 됐습니다."),
            L("사건이 한창일 때 신문은 하루 1백만 부 넘게 팔렸다고 하죠.")]),

# ④ 9월 30일, 하룻밤에 두 명
dict(id="e01", photo=A + "Berner.jpg", cap="버너 가 (1909)", name=("엘리자베스 스트라이드", "1888년 9월 30일 · 44세"),
     lines=[L("9월 30일 새벽 1시, 버너 가의 더트필드 야드."), L("조랑말 수레를 몰고 들어오던 루이스 디엠슈츠가 어둠 속에서 쓰러진 여성을 발견합니다.")]),
dict(id="e02", photo=A + "Louis_Diemsch_tz.png", cap="루이스 디엠슈츠 (1888.10 신문 스케치)", lines=[L("마흔네 살의 엘리자베스 스트라이드였죠.")]),
dict(id="e02b", prompt="A quiet Swedish fishing harbour near Gothenburg in the 1860s on a grey morning, wooden boats and red cottages, a young woman with a travel bag seen from behind on the pier.",
     lines=[L("스웨덴 예테보리 근처에서 태어난 그녀는, 스물두 살에 런던으로 건너왔습니다."), L("키가 커서 '롱 리즈'라고 불렸고, 바느질과 청소로 생계를 이었죠.")]),
dict(id="e03", use="cards/w2.png", lines=[L("15분쯤 전, 이 길을 지나던 이즈리얼 슈워츠는 한 남자가 여성을 거칠게 넘어뜨리는 장면을 봤습니다."),
                                         L("겁에 질린 그는 그대로 달아났다고 하죠.")]),
dict(id="e04", photo=A + "Mitre_Square_Corner.jpg", cap="마이터 광장 (19세기)", name=("캐서린 에도우스", "1888년 9월 30일 · 46세"),
     lines=[L("그리고 불과 45분 뒤, 걸어서 10여 분 거리의 마이터 광장."), L("순찰 중이던 경관이 또 다른 여성, 마흔여섯 살의 캐서린 에도우스를 발견합니다.")]),
dict(id="e04b", dark=True, prompt="Night, the open door of a small Victorian police station cell with a wooden bench inside, a gas lamp in the corridor, a constable's helmet on a hook. No people visible.",
     lines=[L("사실 그녀는 그날 밤 술에 취해 길에 쓰러져 있다가, 경찰서에 붙잡혀 있었습니다."),
            L("새벽 1시쯤 술이 깼다며 풀려났고, 경관에게 잘 자라는 인사를 남기고 걸어 나갔죠."), L("그리고 40여 분 뒤, 마이터 광장에서 발견된 겁니다.", "tonedown")]),
dict(id="e05", photo=LAWENDE, cap="조지프 라웬드가 있는 가족 사진 (1899)", lines=[L("10분 전, 근처를 지나던 조지프 라웬드는 이 광장 입구에서 한 남자와 여성을 봤습니다.")]),
dict(id="e06", use="cards/w3.png", lines=[L("그가 기억한 남자는 서른 살쯤, 중간 키에 밝은 콧수염, 모자를 쓴 뱃사람 같은 차림이었습니다.")]),
dict(id="e07", dark=True, prompt="Night, a dark Victorian tenement doorway on a narrow street: a torn scrap of white cloth lying on the stone step, chalk marks on the brick wall above (unreadable), a police lantern beam.",
     lines=[L("새벽 2시 55분, 굴스턴 가의 한 건물 입구에서 에도우스의 앞치마 조각이 발견됐습니다.")]),
dict(id="e08", photo=A + "The_Juwes_are_the_men_that_Will_not_be_Blamed_for_nothing.jpg", cap="굴스턴 가 낙서 (경찰이 베껴 둔 기록)",
     lines=[L("그 위 벽에는 분필로 쓴 수상한 문장이 남아 있었죠.")]),
dict(id="e09", photo=A + "The_Illustrated_Police_News_-_20_October_1888_-_Sir_Charles_Warren_viewing_handwriting_on_wall.jpg", cap="1888.10.20 일러스트레이티드 폴리스 뉴스",
     lines=[L("하지만 런던 경찰청장 찰스 워런은, 이 낙서가 유대인을 향한 폭동을 부를까 봐 날이 밝기 전에 지우게 했습니다."), L("사진 한 장 남기지 않은 채였죠.")]),
dict(id="e10", photo=A + "Saucy_Jack_front.jpg", cap="'건방진 재키' 엽서 (1888.10.1)", lines=[L("다음 날 통신사로 엽서 한 장이 또 날아옵니다."),
                                                                                       L("하룻밤에 두 명을 해치웠다며, 이 일을 '이중 사건'이라 불렀죠.")]),

# ⑤ 공포의 런던
dict(id="f01", photo=A + "Police_Notice_to_the_Occupier_Whitechapel_murders_30th_September_1888.jpg", cap="1888.9.30 경찰 공고문",
     lines=[L("런던 전체가 공포에 빠졌습니다."), L("경찰은 집집마다 공고문을 돌렸고,")]),
dict(id="f02", photo=A + "Vigilancecommittee.jpg", cap="1888.10.27 화이트채플 자경단", lines=[L("주민들은 직접 자경단을 꾸려 밤거리를 순찰했습니다.")]),
dict(id="f03", photo=A + "FromHellLetter.jpg", cap="'지옥에서' 편지 (1888.10.16)", hl=[(60, 20, 420, 140, 0.8)],
     lines=[L("10월 16일, 자경단 대표 조지 러스크에게 작은 상자 하나가 배달됩니다."),
            L("그 안에는 사람의 장기 일부와 함께, '지옥에서'라는 말로 시작하는 편지가 들어 있었죠.", "tonedown")]),
dict(id="f04", photo=A + "Drawing_of_the_Whitechapel_bloodhouse_trial.jpg", cap="1888 블러드하운드 추적 시험", lines=[L("경찰은 블러드하운드까지 데려와 추적 시험을 했고,")]),
dict(id="f05", photo=A + "Blind-man_s_buff_-_Punch_22_September_1888_139_-_BL.jpg", cap="펀치 1888.9.22 「술래잡기」", lines=[L("잡지들은 눈을 가린 채 헤매는 경찰을 조롱했습니다.")]),
dict(id="f06", prompt="Close-up of a heap of old handwritten Victorian letters and envelopes spilling across a police office desk under a green lamp, handwriting blurred and unreadable.",
     lines=[L("잭 더 리퍼의 이름으로 날아든 편지는 수백 통에 달했지만, 대부분은 장난이었습니다.")]),

# ⑥ 밀러스 코트
dict(id="g01", photo=A + "Dorset-street-1902.jpg", cap="도싯 가 (1902)", lines=[L("11월 9일 오전 10시 45분, 도싯 가의 밀러스 코트.")]),
dict(id="g02", photo=A + "13_Miller_s_Court_Illustration_Mary_Jane_Kelly.jpg", cap="밀러스 코트 13호 (1888.11 신문 삽화)",
     lines=[L("밀린 집세를 받으러 간 남자가 창문 틈으로 방 안을 들여다봅니다.")]),
dict(id="g03", photo=A + "Mary_Jane_Kelly_sketch.jpg", cap="메리 제인 켈리 (1888.11.24 신문 스케치)", name=("메리 제인 켈리", "1888년 11월 9일 · 25세 무렵"),
     lines=[L("다섯 번째 희생자, 스물다섯 살 무렵의 메리 제인 켈리였습니다."),
            L("다섯 사건 가운데 유일하게 방 안에서 벌어진 일이었고, 그 모습은 차마 말로 옮기기 어려울 정도였다고 합니다.", "tonedown")]),
dict(id="g04", use="cards/w4.png", lines=[L("그런데 사흘 뒤, 조지 허친슨이라는 남자가 경찰을 찾아옵니다."),
                                         L("그날 새벽 2시, 켈리가 잘 차려입은 남자와 함께 있는 걸 봤다는 겁니다.")]),
dict(id="g05", dark=True, prompt="Close-up of a well-dressed Victorian gentleman's coat with a fur collar and a gold watch chain across his waistcoat, under a gaslight at night, framed from chest to waist, no face.",
     lines=[L("그는 남자의 외투 깃 모양부터 시곗줄까지 놀라울 만큼 자세히 기억했죠."),
            L("하지만 그 자세함 때문에, 오히려 그의 증언을 의심하는 사람도 많았습니다.")]),

# ⑦ 엇갈린 기억
dict(id="h01", use="cards/compare.png", lines=[L("다시 목격자들의 이야기를 모아 보면,"),
                                              L("엘리자베스 롱은 사슴 사냥 모자를 쓴 점잖은 남자를,"),
                                              L("이즈리얼 슈워츠는 여성을 거칠게 넘어뜨린 남자를,"),
                                              L("조지프 라웬드는 뱃사람 같은 젊은 남자를,"),
                                              L("그리고 조지 허친슨은 부유해 보이는 신사를 봤습니다.")]),
dict(id="h02", dark=True, qcard=True, prompt="Four different blurred male silhouettes in Victorian hats standing apart in thick fog under gas lamps, none recognizable.",
     lines=[L("같은 남자를 봤다고 하기엔, 그들의 기억은 너무나 달랐습니다.")]),

# ⑧ 수사와 용의자
dict(id="i01", photo=A + "Frederick_Abberline.jpg", cap="프레더릭 애버라인 경위 (1888)", name=("프레더릭 애버라인", "스코틀랜드 야드 경위"),
     lines=[L("스코틀랜드 야드에서는 화이트채플을 잘 아는 프레더릭 애버라인 경위가 수사를 이끌었습니다.")]),
dict(id="i02", photo=A + "EdmundReid.jpg", cap="에드먼드 리드 경위 (1896년경)",
     lines=[L("경찰은 2천 명 넘는 사람을 조사했고, 3백 명 넘게 뒤를 캤으며, 80명을 붙잡아 두었습니다."),
            L("근처 정육점 주인과 도축업자 76명까지 하나하나 확인했죠.")]),
dict(id="i03", dark=True, prompt="An empty foggy Whitechapel street at dawn, gas lamps going out, a lone police constable in an 1888 helmet seen from behind walking away.",
     lines=[L("하지만 범인은 끝내 잡히지 않았습니다.", "tonedown")]),
dict(id="i03b", photo=A + "The_Penny_Illustrated_Paper_-_Scenes_of_the_Aldgate_and_Whitechapel_murders.jpg", cap="1888.10.6 페니 일러스트레이티드 페이퍼",
     lines=[L("경찰의 화이트채플 살인 기록에는 1891년까지 모두 열한 건의 살인이 올라 있습니다."),
            L("그중 어디까지가 같은 사람의 짓인지도, 지금까지 논쟁거리죠.")]),
dict(id="i04", photo=A + "Macnaghten_memorandum.jpg", cap="맥노튼 비망록 (1894)", lines=[L("1894년, 경찰 간부 멜빌 맥노튼은 내부 문서에 세 명의 용의자를 적었습니다.")]),
dict(id="i05", photo=A + "Montague_Druitt.jpg", cap="몬터규 드루이트", lines=[L("1888년 12월 템스강에서 시신으로 발견된 변호사 몬터규 드루이트,")]),
dict(id="i06", prompt="Close-up of an old Victorian barber's straight razor, comb and leather strop laid on a worn wooden counter, dim window light.",
     lines=[L("정신병원에 갇힌 폴란드 출신 이발사 아론 코스민스키,")]),
dict(id="i07", photo=A + "Michael_Ostrog.jpg", cap="마이클 오스트로그 (1870년대)", lines=[L("그리고 러시아 출신 사기꾼 마이클 오스트로그였죠."), L("하지만 세 사람 모두 확실한 증거는 없었습니다.")]),
dict(id="i08", photo=A + "Tumblety.jpg", cap="프랜시스 텀블티 (1889)", lines=[L("그 뒤로 용의자로 거론된 사람은 1백 명이 넘습니다."), L("미국인 가짜 의사 프랜시스 텀블티,")]),
dict(id="i09", photo=A + "Walter_Sickert_photo_by_George_Charles_Beresford_1911_1_.jpg", cap="화가 월터 시커트 (1911)", lines=[L("화가 월터 시커트.")]),
dict(id="i10", photo=A + "Walter_Sickert_-_Jack_the_Ripper_s_Bedroom.jpg", cap="월터 시커트 「잭 더 리퍼의 침실」 (1907년경)",
     lines=[L("그는 실제로 「잭 더 리퍼의 침실」이라는 그림을 남기기도 했죠."), L("심지어 「이상한 나라의 앨리스」를 쓴 루이스 캐럴까지 의심을 받았습니다.")]),
dict(id="i11", prompt="Close-up of an old faded Victorian shawl with a floral pattern laid on a modern laboratory bench under bright white light, sample tubes and a pipette nearby.",
     lines=[L("2014년에는 피해자의 것으로 전해지는 숄에서 DNA를 분석해, 코스민스키가 범인이라는 주장이 나왔습니다."),
            L("하지만 숄의 출처부터 분석 방법까지 문제가 지적되면서, 인정받지 못했습니다.")]),
dict(id="i12", photo=A + "John_Tenniel_-_Punch_-_The_Nemesis_of_Neglect.jpg", cap="펀치 1888.9.29 「방치의 응보」",
     lines=[L("편지 상당수는 기자들이 신문을 팔려고 쓴 것이라는 의심도 나왔습니다."), L("실제로 한 기자는 훗날, 동료와 함께 편지를 썼다고 털어놓았다고 하죠.")]),

# ⑨ 마무리
dict(id="j01", foot=BF, t0=22.0, cap=CBF, lines=[L("잭 더 리퍼 사건은 언론이 범죄를 다루는 방식 자체를 바꿔 놓았습니다.")]),
dict(id="j02", photo=SHEDS, cap="1888.10.13 화이트채플 헛간에서 잠든 사람들", lines=[L("그리고 그 그늘에서, 가난한 동네의 비참한 삶이 처음으로 세상의 주목을 받았죠.")]),
dict(id="j03", dark=True, prompt="A lone gas lamp glowing in thick night fog over an empty Whitechapel crossroads, the silhouette of a man in a hat barely visible in the mist, no face.",
     lines=[L("다섯 여성을 마지막으로 본 사람들은, 저마다 다른 남자를 기억했습니다.", "tonedown")]),
dict(id="j04", dark=True, qcard=True, use="img_jr/a04.png", lines=[L("어쩌면 잭 더 리퍼는, 런던의 안개처럼 누구의 얼굴이든 될 수 있었는지도 모릅니다.")]),
dict(id="j05", foot=BF, t0=26.0, cap=CBF, lines=[L("지금까지 마지막 목격자였습니다.")]),
dict(id="j06", use="img_jr/j03.png", blur=True, endcard=True, lines=[L("영상이 재미있었다면 좋아요와 구독 부탁드립니다.")]),
]
