import json

data = []

birthdays_text = """Aiden	Kaitor	Fire Fighter	195	Taurs	23	Summer	7
Alex	Felix	Nurse	185	Capricorn	24	Winter	21
Angela	Aelos	Barista	168	Libra	25	Summer	21
Aria	Hainos	Police	175	Leo	26	Fall	2
Bella	Lucio	Musician	175	Aquarius	25	Spring	3
Blake	Promthe	Fire Fighter	183	Leo	29	Fall	9
Camila	Teranis	Commission Manager	165	Taurus	21	Winter	27
Casandra	Noctrelle	Accessory Crafter	173	Scorpio	33	Winter	5
Celine	Balon	Lifeguard	168	Scorpio	25	Fall	28
Chronos	Sinate	Bard	178	Gemini	99	Summer	15
Dan	Sinate	Reader	195	Gemini	21	Summer	14
Daniel	Balon	Lifeguard	190	Scorpio	22	Winter	2
Darius	Felix	Gardner	180	Aquarius	30	Spring	9
Emily	Hainos	Server	175	Virgo	24	Fall	25
Erica	Tyrnus	Fisher	170	Leo	23	Fall	7
Erik	Tyrnus	Sailor	180	Cancer	33	Summer	23
Fergus	Kaitor	Carpenter	193	Aries	32	Spring	25
Fiona	Agirn	Carpenter	178	Aquarius	29	Spring	10
Halen	Noctrelle	Secretary	173	Capricorn	32	Winter	19
Iris	Briget	Librarian	168	Aries	27	Spring	22
Ivy	Tyrnus	Herbalist	168	Cancer	23	Summer	25
Jade	Herment	Hunter	173	Virgo	21	Fall	12
Jenny	Briget	Author	173	Sagittarius	28	Winter	14
Jocelyn	Promthe	Tailor	175	Leo	30	Fall	5
Joey	Lucio	Mechanic	185	Sagittarius	22	Winter	11
Jun	Hainos	Doctor	187	Aquarius	31	Spring	5
Kai	Herment	Police	191	Sagittarius	28	Winter	17
Kelly	Kaitor	Hunter	175	Libra	29	Summer	22
Kiri	Briget	Trainer	170	Pisces	31	Spring	15
Leon	Briget	Mayor	183	Aries	32	Spring	21
Lilis	Lucio	Artifact Donor	165	Taurs	22	Summer	3
Mia	Agirn	Painter	168	Pisces	21	Spring	11
Michael	Hainos	Driver	190	Pisces	24	Spring	17
Nick	Teranis	Bartender	195	Virgo	25	Fall	17
Nora	Kaitor	Chef	170	Capricorn	26	Winter	22
Raymor	Tyrnus	Miner	170	Cancer	23	Summer	27
Reina	Aelos	Makeup Artist	180	Cancer	24	Summer	26
Rio	Aelos	Jeweler	182	Capricorn	25	Winter	23
Samuel	Promthe	Tailor	193	Leo	26	Fall	4
Sean	Sinate	Reader	195	Gemini	21	Summer	21
Sebastian	Aelos	Farmer	190	Libra	29	Fall	25
Syra	Teranis	Nurse	170	Virgo	27	Fall	14
Vincent	Lucio	Police	183	Pisces	27	Spring	14
Vivian	Agirn	Fire Fighter	173	Taurus	31	Summer	10"""

season_map = {"Spring": "봄", "Summer": "여름", "Fall": "가을", "Winter": "겨울"}

# Process Birthdays
for line in birthdays_text.split('\n'):
    parts = line.split('\t')
    if len(parts) >= 8:
        name = parts[0]
        job = parts[2]
        zodiac = parts[4]
        season = parts[6]
        day = int(parts[7])
        data.append({
            "season": season,
            "day": day,
            "type": "birthday",
            "name": f"{name} 생일",
            "desc": f"직업: {job} / 별자리: {zodiac}\n{name}의 생일입니다."
        })

# Process Zodiacs
zodiacs = [
    ("Spring", 1, "물병자리"), ("Spring", 11, "물고기자리"), ("Spring", 21, "양자리"),
    ("Summer", 3, "황소자리"), ("Summer", 13, "쌍둥이자리"), ("Summer", 22, "게자리"),
    ("Fall", 1, "사자자리"), ("Fall", 10, "처녀자리"), ("Fall", 19, "천칭자리"), ("Fall", 28, "전갈자리"),
    ("Winter", 9, "사수자리"), ("Winter", 19, "염소자리"), ("Winter", 28, "물병자리")
]
for s, d, z in zodiacs:
    data.append({
        "season": s,
        "day": d,
        "type": "zodiac",
        "name": f"{z} 시작",
        "desc": f"{z}의 기운이 시작됩니다."
    })

# Process Festivals
festivals = [
    ("Spring", 8, 13, "벚꽃놀이", "봄을 알리는 벚꽃 축제입니다."),
    ("Spring", 26, 28, "로맨스 축제", "사랑을 고백하는 축제입니다."),
    ("Summer", 8, 14, "바다 축제", "여름 바다를 즐기는 축제입니다."),
    ("Summer", 26, 28, "불꽃놀이", "밤하늘을 수놓는 불꽃 축제입니다."),
    ("Fall", 8, 14, "수확제", "풍성한 작물을 기념하는 축제입니다."),
    ("Fall", 26, 28, "유령 축제", "가을 밤의 미스터리한 축제입니다."),
    ("Winter", 8, 13, "온천 여행", "따뜻한 온천에서 몸을 녹이는 축제입니다."),
    ("Winter", 24, 28, "겨울 축제", "한 해를 마무리하는 눈꽃 축제입니다.")
]
for s, start_d, end_d, name, desc in festivals:
    for d in range(start_d, end_d + 1):
        data.append({
            "season": s,
            "day": d,
            "type": "festival",
            "name": name,
            "desc": desc
        })

with open("_data/calendar_events.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    
print("Calendar events generated.")
