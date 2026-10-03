# 마지막 목격자 2편 「에드 게인」 — 1편 본편(05번) 방식 그대로
# 사실 근거: en.wikipedia "Ed Gein" (1906.8.27 출생, 아버지 조지 1940.4.1 사망, 형 헨리 1944.5.16 화재 중 사망(질식, 머리 멍 보도),
#   어머니 오거스타 1945.12.29 뇌졸중 사망, 1954.12.8 메리 호건 실종(핏자국·탄피), 1957.11.16 버니스 워든 실종(사슴 사냥 첫날, 아들 프랭크 부보안관, 부동액 영수증),
#   1947~1952 공동묘지 3곳 무덤 9기, 확인 희생자 2명, 1958 재판 불능→중앙주립병원, 1958.3.20 집 화재(방화 의심), 차 경매 760달러(유랑 쇼),
#   1968.11 재판 유죄·정신이상, 멘도타, 1984.7.26 77세 사망, 플레인필드 묘지, 묘비 2000 도난→2001.6 시애틀 근처 회수, 블록 소설 1959·히치콕 1960)
# 수위: 시신·유해는 묘사하지 않고 돌려 말한다. 그림은 피·시신 없음.
# 나레이션 = 사용자가 주는 mp3 → ../import_mp3.py 로 줄마다 자름(tts_eg). 실제 자료 = archive/sources.json (위키미디어 공용 퍼블릭 도메인)
STYLE = ("Photorealistic cinematic documentary reenactment still, shot on 35mm film, subtle film grain, muted natural colors. "
         "Setting: rural Wisconsin, USA, 1940s-1950s — American people in period clothing, wooden farmhouses, pickup trucks of the era. "
         "Wide 16:9 full-bleed frame, no border. No blood, no gore, no bodies, no human remains, no visible injuries. "
         "Absolutely no text, no letters, no numbers, no readable signs, no captions, no watermark, no logo.")
DARK = " Night or very dim light, deep shadows, tense eerie atmosphere."
BRIGHT = ("Photorealistic documentary reenactment photo, natural soft daylight, realistic natural colors, evenly lit and clearly visible, "
          "like a high-quality stock photo used in a TV documentary. Rural Wisconsin, USA, 1940s-1950s, American people in period clothing. "
          "16:9 full-bleed. No blood, no gore, no bodies. Absolutely no text, no letters, no readable signs, no watermark.")
TTS_FIX = {}
NAMES = ["에드 게인", "오거스타", "헨리", "메리 호건", "버니스 워든", "프랭크 워든", "로버트 블록", "플레인필드"]
VOICE = None                       # 사용자 mp3 (import_mp3.py)
TTS_DIR, IMG_DIR, OUTNAME = "tts_eg", "img_eg", "final_eg"
TVOFF = True
GRADE = True   # 재연 그림에 '오래된 기록물' 필터(세피아/밤은 청록 + 빛 번짐 + 필름 결) — 사용자 요청 2026-10-02
# 음악: 그노시엔느 1번만 영상 끝까지 반복(사용자 "인트로 음악이 계속 나오는거야, 그 음악이 맘에 들어" 2026-10-02) — 다른 곡 섞지 않음, 합성 배경음악 없음
INTRO = dict(music="music/gnossienne1.ogg", music_list=["music/gnossienne1.ogg"], through=True,
             lead=2.4, at=1.6, offset=0.0, end_scene="a08", gain=0.31, body_gain=0.16)

A = "archive/"
GEIN, CENSUS, STONE, TOWN = A + "Ed-Gein.jpeg", A + "1930_census_Gein.jpg", A + "Ed_Gein_Headstone.jpg", A + "Plainfield_Wisc_-_1923.jpg"
MAP = A + "Sanborn_Fire_Insurance_Map_from_Plainfield_Waushara_County_Wisconsin._LOC_sanborn09664_002-1.jpg"
PSY = "footage/Psycho_Theatrical_Trailer_1960_.webm"; CP = "영화 「사이코」 예고편 (1960)"   # 예고편만 퍼블릭 도메인 — 영화 본편 장면은 쓰지 않는다
FARM = "an isolated weathered two-story wooden farmhouse with a sagging porch and a barn, bare trees, flat empty fields"


def L(t, e="normal", q=False):
    return (t, e, "q") if q else (t, e)


SCENES = [
# ⓪ 도입 — 첫인사 형식(2026-10-02 사용자 지정): "마지막 목격자." → "오늘의 이야기는 ~" 으로 이야기 소개
dict(id="a01", foot=PSY, t0=60.0, cap=CP, lines=[L("마지막 목격자.")]),
dict(id="a02", foot=PSY, t0=74.0, cap=CP, lines=[L("오늘은 영화 「사이코」와 「텍사스 전기톱 학살」, 「양들의 침묵」의 모티브가 된 실제 인물.")]),
dict(id="a03", name=("에드 게인", "Edward Theodore Gein · 1906~1984"), photo=GEIN, cap="에드 게인 (1958년경)", hl=[(120, 60, 300, 290, 1.0)],
     lines=[L("미국 위스콘신의 조용한 시골 마을에서 이웃집 아이들까지 돌봐 주던 남자, 에드 게인에 대한 이야기입니다.")]),
dict(id="a04", prompt="Close-up of weathered farmers' hands around chipped coffee mugs on a 1950s small-town diner counter, a waitress's hand pouring coffee from a pot, warm friendly light.",
     lines=[L("마을 사람들은 그를 조금 별나지만 순하고 착한 사람으로 기억했습니다.")]),
dict(id="a05", qcard=True, dark=True, prompt=f"Night, November 1957: {FARM}, two sheriff's cars of the 1950s parked in front with headlights on, deputies with flashlights walking toward the house.",
     lines=[L("그런데 1957년 11월, 그의 농장을 찾아간 보안관들은 평생 잊지 못할 광경을 마주하게 되는데요.", "tonedown")]),
dict(id="a06", photo=TOWN, cap="위스콘신주 플레인필드 (1923)", lines=[L("그날 이후 플레인필드라는 마을 이름은, 미국 범죄사에서 가장 끔찍한 기억이 됐습니다.")]),
dict(id="a07", foot=PSY, t0=98.0, cap=CP, lines=[L("도대체 그 집에서는 무슨 일이 있었던 걸까요?")]),
dict(id="a08", foot=PSY, t0=40.0, cap=CP, lines=[L("처음부터 따라가 보겠습니다.")]),

# ① 어머니
dict(id="b01", prompt="A poor 1910s Wisconsin farm family portrait-style scene: a stern mother in a long dark dress, a tired father, two young boys in overalls standing in front of a plain wooden house.",
     lines=[L("에드 게인은 1906년 8월 27일, 미국 위스콘신주에서 태어났습니다.")]),
dict(id="b01b", prompt="A small 1910s American town grocery store front with wooden shelves and barrels, a tired shopkeeper locking the door for the last time, early morning.",
     lines=[L("아버지는 한때 작은 식료품 가게를 했지만 곧 가게를 정리했고, 가족은 시골로 옮겨 가게 됩니다.")]),
dict(id="b02", prompt="Close-up of a tired man's rough hand gripping a half-empty liquor bottle on a worn 1910s kitchen table, a woman's hand pressed firmly on the table edge beside it.",
     lines=[L("아버지 조지는 술에 기대 사는 사람이었고, 집안을 실제로 이끈 건 어머니 오거스타였죠.")]),
dict(id="b03", prompt="A stern middle-aged woman in a dark 1910s dress and hair in a tight bun, holding a thick old Bible, sitting upright in a plain farmhouse parlor, cold daylight.",
     lines=[L("오거스타는 독실하다 못해 극단적인 신앙을 가진 사람이었습니다."),
            L("세상은 죄로 가득하고, 술과 여자는 모두 악마의 도구라고 아들들에게 가르쳤죠.")]),
dict(id="b04", prompt="Close-up of a stern woman's hands holding open an old worn Bible on her lap, a small boy's hands folded tightly on his knees beside her, afternoon window light.",
     lines=[L("매일 오후면 성경 속 죽음과 심판에 관한 구절을 읽어 주었다고 하는데요.")]),
dict(id="b05", photo=MAP, cap="플레인필드 지도 (1901)", lines=[L("1914년, 가족은 바깥세상과 떨어진 플레인필드 외곽의 농장으로 이사합니다.")]),
dict(id="b06", prompt="A shy thin boy in 1910s clothes standing alone at the edge of a country schoolyard, watching other children play from a distance.",
     lines=[L("어머니는 아들들이 친구를 사귀는 것조차 못마땅하게 여겼습니다."), L("학교에서 에드는 수줍고 어딘가 어색한 아이였죠.")]),
dict(id="b06b", prompt="A 1910s country schoolroom: a shy boy at a wooden desk reading a book intently while other children whisper and point at him, daylight through tall windows.",
     lines=[L("공부, 특히 책 읽기는 꽤 잘했다고 합니다."), L("하지만 엉뚱한 순간에 혼자 웃음을 터뜨리는 버릇 때문에, 아이들 사이에서 놀림을 받기도 했죠.")]),
dict(id="b06c", prompt="Evening in a plain 1910s farmhouse: a boy doing farm chores alone by lantern light while his stern mother watches from the porch, empty fields around.",
     lines=[L("학교가 끝나면 친구 대신 농장 일과 어머니의 성경 이야기가 기다리고 있었습니다."), L("에드에게 세상은 어머니가 들려주는 이야기, 그게 전부였죠.")]),
dict(id="b07", photo=CENSUS, cap="1930 미국 인구조사 기록", lines=[L("1930년 인구조사 기록에도, 게인 가족 넷의 이름이 나란히 남아 있습니다.")]),

# ② 가족의 죽음
dict(id="c01", prompt="A small rural funeral in 1940 Wisconsin: a plain wooden coffin, a few mourners in dark coats, a stern widow and two grown sons standing apart, grey sky.",
     lines=[L("1940년, 아버지가 심장마비로 세상을 떠납니다.")]),
dict(id="c02", prompt="Two grown brothers in 1940s farm clothes arguing quietly beside a barn, the older one pointing toward the farmhouse, the younger one looking down.",
     lines=[L("형 헨리는 어머니에게 지나치게 매달리는 동생을 걱정했다고 전해지는데요.")]),
dict(id="c03", prompt="A brush fire spreading across dry marsh grass near a 1940s Wisconsin farm, thick grey smoke rising, two small figures with shovels in the distance.",
     lines=[L("1944년 5월, 두 형제가 농장 근처의 마른 풀숲을 태우던 중 불이 번졌습니다.")]),
dict(id="c04", dark=True, prompt="Close-up of a hand holding an old kerosene lantern low over burnt black marsh grass at dusk, smoke drifting through the light.",
     lines=[L("불이 꺼진 뒤 에드는 형이 보이지 않는다고 신고했죠."),
            L("수색대는 그가 안내한 곳에서 헨리를 찾아냈다고 전해집니다.")]),
dict(id="c05", prompt="A 1940s small-town coroner's office: an old typewriter, a death certificate form (blank, no readable text) and a desk lamp, a sheriff's hat on the desk.",
     lines=[L("공식 사인은 질식이었지만, 머리에 멍 자국이 있었다는 이야기도 나왔습니다."), L("하지만 당시 이 죽음은 사고로 처리됐습니다.")]),
dict(id="c06", dark=True, prompt="Close-up of an old woman's wrinkled hand resting still on a faded quilt beside a closed Bible, dim winter light from a window.",
     lines=[L("그리고 1945년 12월, 어머니마저 두 차례 뇌졸중 끝에 숨을 거둡니다.", "tonedown")]),
dict(id="c06b", foot=PSY, t0=178.0, cap=CP, lines=[L("에드는 하나뿐인 친구이자 세상의 전부를 잃었습니다.", "tonedown")]),
dict(id="c07", foot=PSY, t0=162.0, cap=CP, lines=[L("그는 어머니가 쓰던 방들을 판자로 막아, 그 모습 그대로 봉인해 버렸죠.")]),
dict(id="c08", dark=True, prompt="A tiny cluttered farmhouse room next to a kitchen lit by a single kerosene lamp: a narrow cot, piles of old magazines and books, jars and junk everywhere, a lonely atmosphere. No people.",
     lines=[L("자신은 부엌 옆 작은 방 하나에서만 지냈습니다.")]),
dict(id="c09", prompt="Overgrown abandoned farm fields in early 1950s Wisconsin, a rusting plow and a sagging fence, a weathered farmhouse in the distance, overcast daylight.",
     lines=[L("농사도 그만뒀습니다."), L("1951년부터는 정부의 농지 보조금을 받으며 생활했죠.")]),
dict(id="c10", dark=True, prompt="A messy table in a dim 1950s farmhouse room lit by a kerosene lamp: stacks of cheap old pulp magazines with lurid painted covers (no readable text) and worn books, a pair of reading glasses.",
     lines=[L("그리고 혼자 남은 집에서, 그는 이상한 책과 잡지에 빠져들었습니다."),
]),
dict(id="c10b", photo=A + "Ilse_Koch_testifies_in_her_own_defense_8_jul_47.png", cap="나치 수용소 간수 일제 코흐, 1947년 재판 (미군 촬영)",
     lines=[L("식인 풍습이나 나치의 잔혹 행위 같은 끔찍한 이야기를 다룬 싸구려 잡지들이었는데요.")]),
dict(id="c10c", use="img_eg/c10.png", lines=[L("그는 그 이야기들을 몇 번이고 다시 읽었다고 합니다.")]),

# ③ 이웃
dict(id="d01", photo=TOWN, cap="위스콘신주 플레인필드 (1923)", lines=[L("혼자가 된 에드는 마을에서 이런저런 잡일을 하며 살았습니다.")]),
dict(id="d01b", prompt="A 1950s rural Wisconsin road crew and threshing crew at work in summer: men in overalls and caps with shovels and a threshing machine, dust in the sunlight.",
     lines=[L("도로 공사 일꾼으로도, 추수철 일꾼으로도 일했죠."), L("성실하진 않아도, 부르면 군말 없이 오는 사람이었다고 합니다.")]),
dict(id="d02", prompt="Close-up of a small child's hand holding a thin man's rough finger on a wooden farm porch step, summer daylight.",
     lines=[L("이웃집 아이들을 봐주는 일도 했는데, 아이들은 그를 꽤 잘 따랐다고 하죠."), L("어른들보다 아이들과 더 편하게 어울렸다는 증언도 있습니다.")]),
dict(id="d03", prompt="Two 1950s farm women gossiping over a wooden fence in a small Wisconsin town, one glancing toward a distant lone farmhouse on the horizon.",
     lines=[L("혼자 사는 그 집에 대해서는 이상한 소문이 돌기도 했습니다.")]),
dict(id="d03b", foot=PSY, t0=266.0, cap=CP,
     lines=[L("그의 집에서 사람 머리 모양의 물건을 봤다는 아이들도 있었지만, 에드는 먼 친척이 보내 준 외국 기념품이라고 둘러댔죠.")]),
dict(id="d03c", use="img_eg/d03.png", lines=[L("어른들은 그 이야기를 아이들의 상상으로 넘겼습니다.")]),

# ④ 사라진 사람들
dict(id="e00", prompt="A 1940s-50s Wisconsin small-town police station bulletin board covered with missing-person posters and photos (no readable text), a worried policeman looking at them, daylight.",
     lines=[L("사실 그 무렵 위스콘신에서는 설명되지 않는 실종 사건이 잇따르고 있었습니다.")]),
dict(id="e00b", missing=True, prompt="A quiet 1940s Wisconsin country lane near a farmhouse mailbox in late afternoon, empty, a child's red ball lying at the side of the road.",
     lines=[L("1947년에는 여덟 살 소녀 조지아 웨클러가 집 근처에서 사라졌고,")]),
dict(id="e00c", missing=True, prompt="A snowy forest clearing in 1952 Wisconsin with car tire tracks fading into the woods and hunters' footprints, grey sky, no car and no people.",
     lines=[L("1952년에는 사냥을 나간 남자 두 명이 차와 함께 감쪽같이 사라졌죠.")]),
dict(id="e00d", missing=True, dark=True, prompt="Night, 1953 La Crosse, Wisconsin: a quiet suburban house with the porch light on, an open back door, a policeman's flashlight on the lawn.",
     lines=[L("1953년에는 라크로스에서 아이를 돌보던 열다섯 살 소녀 에블린 하틀리가 실종됐습니다."), L("어느 사건도 범인을 찾지 못했습니다.")]),
dict(id="e01", missing=True, dark=True, prompt="A small empty 1950s country tavern at night: a wooden bar counter, stools, beer signs without text, a single bulb, an overturned chair, cold winter night outside the window.",
     lines=[L("1954년 12월 8일, 마을 술집 주인 메리 호건이 갑자기 사라집니다.", "tonedown")]),
dict(id="e02", dark=True, prompt="Close-up on the worn wooden floor of an empty 1950s tavern near the bar counter: a single small brass bullet casing lying on the floor under dim light.",
     lines=[L("가게 바닥에는 핏자국이 남아 있었고, 계산대 옆에서는 탄피 하나가 발견됐죠."), L("범인의 단서는 더 나오지 않았습니다.")]),
dict(id="e03", prompt="Inside a 1950s small-town general store: a few local men in caps laughing at the counter, a thin quiet man in a plaid jacket at the edge of the group with an odd smile, daylight.",
     lines=[L("얼마 뒤 누군가 메리 호건 이야기를 꺼내자, 에드는 그녀가 지금 자기 농장에 있다고 농담처럼 말했다고 하는데요."),
            L("모두 그저 별난 사람의 엉뚱한 농담으로 여겼습니다.")]),

# ⑤ 1957년 11월 16일
dict(id="f01", prompt="November 1957, a small Wisconsin main street dusted with snow, almost empty, pickup trucks with hunting gear, men in red-and-black plaid hunting coats with rifles leaving for the woods.",
     lines=[L("그리고 3년 뒤인 1957년 11월 16일."), L("사슴 사냥 시즌이 시작된 날이라, 마을의 남자들은 대부분 숲으로 떠나 있었습니다.")]),
dict(id="f02", missing=True, dark=True, prompt="An empty 1950s small-town hardware store interior: shelves of tools and paint cans, the cash register drawer left open, the front door ajar with cold light coming in. No people.",
     lines=[L("그날 철물점 주인 버니스 워든이 가게에서 사라집니다.", "tonedown"), L("그녀의 아들 프랭크는 마을의 부보안관이었죠."),
            L("오후 다섯 시쯤 가게에 들른 프랭크는, 열려 있는 금전등록기와 바닥의 핏자국을 발견합니다.", "tonedown")]),
dict(id="f03", prompt="Close-up of a deputy sheriff's hand in a 1950s uniform sleeve holding a small handwritten store sales slip (blank, no readable text) beside an old cash register.",
     lines=[L("그리고 어머니가 그날 아침 마지막으로 쓴 영수증 한 장을 찾아냈죠."),
            L("부동액을 샀다는 내용이었고, 손님은 바로 에드 게인이었습니다.")]),
dict(id="f04", prompt="A 1950s hardware store counter the evening before: a thin man in a plaid hunting cap talking with a middle-aged woman shopkeeper in a cardigan, cans of antifreeze on the shelf behind.",
     lines=[L("전날 저녁에도 에드는 가게에 들러, 다음 날 아침 부동액을 사러 오겠다고 말했었습니다."), L("프랭크는 곧바로 에드 게인을 떠올렸습니다.")]),
dict(id="f04b", dark=True, prompt="Evening, a small 1950s rural grocery store with warm lit windows in the snow, two sheriff's deputies in 1950s uniforms walking in through the door, a thin man in a hunting cap at the counter seen from behind.",
     lines=[L("그 시각 에드는 웨스트 플레인필드의 한 식료품점에 있었습니다."), L("보안관들은 그곳에서 그를 체포했죠.")]),
dict(id="f05", dark=True, prompt=f"Night: two 1950s sheriff's cars driving fast down a snowy country road toward {FARM}, headlights cutting through the dark.",
     lines=[L("그리고 다른 보안관들은 에드의 농장으로 향했습니다.")]),

# ⑥ 헛간과 집
dict(id="g01", dark=True, prompt="Close-up of a deputy's flashlight beam cutting across a dusty wooden floor inside a dark shed at night, his boot at the edge of the frame. Nothing else visible.",
     lines=[L("헛간 안에서 그들은 버니스 워든을 찾아냈습니다.", "tonedown"),
            L("그 모습은 너무 참혹해, 현장에 있던 사람들 모두가 할 말을 잃었다고 하는데요.", "tonedown")]),
dict(id="g02", foot=PSY, t0=106.0, cap=CP, lines=[L("집 안은 더 믿기 어려웠습니다.", "tonedown")]),
dict(id="g03", dark=True, prompt="A dark cluttered 1950s farmhouse kitchen lit only by flashlight beams: piles of junk, old newspapers, dirty dishes, boxes and jars stacked everywhere, deputies' silhouettes in the doorway. No bodies, no gore.",
     lines=[L("쓰레기와 잡동사니가 가득한 방들 사이에서, 사람의 유해로 만든 물건들이 줄줄이 나왔던 거죠."),
            L("그중에는 행방불명됐던 메리 호건의 흔적도 있었습니다.")]),
dict(id="g03c", foot=PSY, t0=206.0, cap=CP, lines=[L("수사관들은 처음에 자신들이 무엇을 보고 있는지조차 믿지 못했다고 하는데요.")]),
dict(id="g03b", prompt="Daytime, November 1957: 1950s state crime laboratory investigators in overcoats and hats carrying cardboard evidence boxes out of an old farmhouse, a deputy writing notes, police cars parked in the snowy yard.",
     lines=[L("주 범죄 연구소까지 나서 집 안의 물건들을 하나하나 기록했고, 조사에는 며칠이 걸렸습니다.")]),
dict(id="g04", foot=PSY, t0=170.0, cap=CP, lines=[L("봉인된 어머니의 방만은, 먼지만 쌓인 채 깨끗하게 남아 있었죠.")]),

# ⑦ 자백
dict(id="h01", name=("에드 게인", "1957년 체포 당시 51세"), photo=GEIN, cap="에드 게인 (1958년경)", lines=[L("체포된 에드는 차분하게 진술했습니다.")]),
dict(id="h02", dark=True, prompt="Close-up of an old shovel stuck upright in dark earth at night, lantern light and fog, a blurred old headstone in the background.",
     lines=[L("1947년부터 몇 년 동안, 밤마다 마을 근처 공동묘지 세 곳에서 무덤을 파헤쳤다는 겁니다."),
            L("대상은 대부분 세상을 떠난 지 얼마 안 된 중년 여성들, 어머니를 닮은 사람들이었죠.")]),
dict(id="h02b", prompt="Cold daytime in a small Wisconsin cemetery, 1957: investigators in overcoats and hats standing around a grave site behind a canvas screen, shovels, grim faces. Nothing visible in the ground.",
     lines=[L("수사관들은 그의 말이 사실인지 확인하기 위해, 무덤 세 곳을 직접 열어 보았습니다."),
            L("관은 그의 진술대로 비어 있거나 훼손돼 있었죠.")]),
dict(id="h03", photo=GEIN, cap="에드 게인 (1958년경)", hl=[(120, 60, 300, 290, 0.6)],
     lines=[L("그가 직접 목숨을 빼앗았다고 인정한 사람은 메리 호건과 버니스 워든, 두 명이었습니다."),
            L("형 헨리의 죽음도 다시 의심받았지만, 끝내 밝혀지지는 않았습니다.")],
     ov=[("확인된 희생자 2명 · 파헤친 무덤 9기", "stat", 0)]),
dict(id="h04", dark=True, prompt="A bare 1957 county jail interrogation room with brick walls and a single hanging bulb, an empty wooden chair and table, a sheriff's hat left on the table.",
     lines=[L("그런데 조사 과정에도 문제가 있었습니다."),
            L("당시 보안관이 조사 중에 에드를 폭행했다는 사실이 알려지면서, 첫 자백은 재판에서 증거로 쓰이지 못하게 됐죠."),
            L("그 보안관은 재판을 앞둔 1968년, 마흔셋의 나이로 심장마비로 세상을 떠났습니다.")]),
dict(id="h05", prompt="Extreme close-up of a 1950s polygraph machine needle drawing jagged ink lines on a moving paper chart.",
     lines=[L("에드는 다른 실종 사건들에 대해서도 조사를 받았습니다."),
            L("에블린 하틀리 사건에 대해서는 거짓말 탐지기 검사를 두 번 통과했고, 그의 집에서도 흔적은 나오지 않았죠."),
            L("나머지 사건들도 그와의 연관성은 끝내 확인되지 않았습니다.")]),

# ⑧ 재판·이후
dict(id="i00", prompt="Daytime 1957-58: a crowd of reporters with old press cameras and curious sightseers in winter coats gathered at the gate of an isolated Wisconsin farmhouse, many 1950s cars parked along the snowy road.",
     lines=[L("사건이 알려지자 플레인필드에는 전국에서 기자들과 구경꾼이 몰려들었습니다."),
            L("주말이면 그의 농장 앞에 차들이 줄을 섰고, 그를 소재로 한 섬뜩한 농담까지 유행했죠."),
            L("마을 사람들은 이 모든 관심을 몹시 괴로워했다고 합니다.")]),
dict(id="i01", photo=A + "Entrance_to_Dodge_Correctional_Institution_01.jpg", cap="옛 중앙주립병원 자리 (현 도지 교정시설, 2016)",
     lines=[L("1958년, 그는 재판을 받을 수 없는 정신 상태라는 판정을 받고 정신병원에 수용됩니다.")]),
dict(id="i02", dark=True, prompt=f"Night, March 1958: {FARM} engulfed in flames, sparks rising into the dark sky, silhouettes of townspeople watching from the road.",
     lines=[L("그 집이 관광 명소가 될지도 모른다는 소문이 돌던 1958년 3월."), L("경매를 앞두고 있던 그의 집은 원인 모를 불에 타 사라졌습니다."),
            L("누군가 일부러 불을 질렀다는 의심이 돌았지만, 범인은 밝혀지지 않았습니다.")]),
dict(id="i03", prompt="A 1950s traveling carnival sideshow tent on a summer evening, a crowd of curious people in 1950s clothes lining up to look at an old 1940s sedan displayed behind a rope, no text on banners.",
     lines=[L("그가 타던 차는 경매에서 760달러에 팔려, 유랑 서커스의 구경거리가 됐습니다.")]),
dict(id="i04", prompt="Close-up of a judge's wooden gavel striking the sound block, a 1960s courtroom blurred in the background.",
     lines=[L("그리고 10년 뒤인 1968년, 의사들은 그가 마침내 재판을 받을 수 있는 상태가 됐다고 판단합니다."),
            L("재판은 그해 11월 7일, 배심원 없이 판사 한 명이 맡아 일주일 동안 열렸습니다."),
            L("11월 14일, 로버트 골마 판사는 그에게 버니스 워든 살해의 유죄를 선고합니다."),
            L("하지만 이어진 정신 감정 재판에서, 범행 당시 정신이상이었다는 판단이 내려졌죠."),
            L("그는 다시 정신병원으로 돌아갔습니다.")]),
dict(id="i05", photo=A + "Mendota_Mental_Health_Institute_-_Stovall_Hall.jpg", cap="멘도타 정신건강연구소 (2024, 사진 Praiawart · CC BY 4.0)",
     lines=[L("병원에서 그는 조용하고 말 잘 듣는 환자였다고 전해집니다."), L("에드 게인은 1984년 7월 26일, 일흔일곱의 나이로 병원에서 숨을 거뒀습니다.")]),
dict(id="i06", photo=STONE, cap="에드 게인의 묘비 (1999년 모습)", lines=[L("그는 플레인필드 공동묘지, 어머니와 형 곁에 묻혔습니다."),
            L("하지만 그 묘비마저 2000년에 도둑맞았다가, 이듬해 시애틀 근처에서 발견됐죠.")]),
dict(id="i07", prompt="A quiet small-town Wisconsin cemetery in autumn daylight, a patch of grass with no headstone between two old family graves, fallen leaves.",
     lines=[L("지금 그의 무덤에는 아무 표시도 남아 있지 않습니다.")]),

# ⑨ 마지막
dict(id="j01", foot=PSY, t0=50.0, cap=CP, lines=[L("1959년, 작가 로버트 블록은 이 사건에서 영감을 얻어 소설 「사이코」를 썼습니다.")]),
dict(id="j02", foot=PSY, t0=138.0, cap=CP, lines=[L("그리고 이듬해 히치콕 감독이 이 소설을 영화로 만들었죠.")]),
# ⑨-2 에드 게인에게서 영감을 받은 작품·캐릭터(사용자 요청 2026-10-02) — 캐릭터 그림은 저작권 때문에 그리지 않고 직접 만든 '작품 카드'(cards/)로
#   근거: en.wikipedia "Ed Gein" 대중문화 부분(텍사스 전기톱 학살 1974 레더페이스, 디레인지드 1974, 양들의 침묵 버팔로 빌, AHS: Asylum 올리버 스레드슨,
#   In the Light of the Moon 2000(미국 개봉명 Ed Gein), Monster: The Ed Gein Story 넷플릭스 2025.10.3 찰리 허냄)
dict(id="k01", foot=PSY, t0=290.0, cap=CP, lines=[L("영화 속 노먼 베이츠는 죽은 어머니에게서 벗어나지 못한 채, 외딴 집 아래에서 모텔을 지키는 남자였습니다.")]),
dict(id="k02", use="cards/k02.png", lines=[L("그리고 에드 게인은 이후 수많은 공포 영화의 단골 모델이 됩니다.")]),
dict(id="k03", use="cards/k03.png", lines=[L("1974년 개봉한 「텍사스 전기톱 학살」의 살인마, 레더페이스.")]),
dict(id="k04", dark=True, prompt="Dusk in rural 1970s Texas: an isolated weathered wooden farmhouse with a rusty windmill and dead trees, dry yellow grass, an ominous orange sky. No people.",
     lines=[L("외딴 시골집에 숨어 사는 정체불명의 살인마라는 설정은, 에드 게인의 집에서 나온 기괴한 물건들에서 영감을 받은 것이었죠.")]),
dict(id="k05", use="cards/k05.png", lines=[L("같은 해 나온 영화 「디레인지드」는, 아예 그의 사건을 거의 그대로 옮겨 온 작품이었습니다.")]),
dict(id="k06", use="cards/k06.png", lines=[L("1991년 「양들의 침묵」의 연쇄살인마 버팔로 빌에게도, 그의 흔적이 남아 있습니다.")]),
dict(id="k07", use="cards/k07.png", lines=[L("드라마 「아메리칸 호러 스토리」 시즌 2에서는, 정신과 의사 올리버 스레드슨이라는 인물로 다시 태어났죠.")]),
dict(id="k08", use="cards/k08.png", lines=[L("2000년에는 그의 삶을 다룬 영화 「인 더 라이트 오브 더 문」이 만들어졌고, 미국에서는 「에드 게인」이라는 제목으로 개봉했습니다.")]),
dict(id="k09", use="cards/k09.png", lines=[L("그리고 2025년 10월, 넷플릭스 드라마 「몬스터: 에드 게인 이야기」가 공개되며 다시 한번 전 세계의 관심을 모았습니다."),
                                         L("배우 찰리 허냄이 에드 게인을 연기했죠.")]),
dict(id="j03", foot=PSY, t0=114.0, cap=CP, lines=[L("외딴 집, 죽은 어머니, 그리고 친절한 얼굴의 남자.", "tonedown")]),
dict(id="j04", foot=PSY, t0=340.0, cap=CP, lines=[L("에드 게인이 남긴 그림자는 지금도 수많은 공포 영화 속에 살아 있습니다.")]),
dict(id="j05", photo=TOWN, cap="위스콘신주 플레인필드 (1923)", lines=[L("가장 가까이에서 그를 지켜본 이웃들은, 끝까지 그를 순하고 조용한 사람으로 기억했습니다."),
            L("그 조용한 이웃의 집 안을 들여다본 사람은, 마을에 아무도 없었죠.")]),
dict(id="j06", qcard=True, prompt=f"Golden dusk over flat Wisconsin farmland, a long empty dirt road and a lone mailbox, {FARM} small on the horizon.",
     lines=[L("어쩌면 그들이야말로, 아무것도 보지 못한 마지막 목격자들이었는지도 모릅니다.", "tonedown")]),
dict(id="j07", foot=PSY, t0=82.0, cap=CP, lines=[L("지금까지 마지막 목격자였습니다.")]),
dict(id="j08", use="img_eg/j06.png", blur=True, endcard=True, lines=[L("영상이 재미있었다면 좋아요와 구독 부탁드립니다.")]),
]
