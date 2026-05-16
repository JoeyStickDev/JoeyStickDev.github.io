import csv
import re
import os

characters_path = r"f:\Git\JoeyStickDev.github.io\_data\characters.csv"
npc_path = r"f:\Git\JoeyStickDev.github.io\Temp\NPC_DetailInfo_DT.csv"

# Translation maps
season_map = {
    "Spring": "봄",
    "Summer": "여름",
    "Fall": "가을",
    "Winter": "겨울"
}

zodiac_map = {
    "Aquarius": "물병자리",
    "Pisces": "물고기자리",
    "Aries": "양자리",
    "Taurus": "황소자리",
    "Gemini": "쌍둥이자리",
    "Cancer": "게자리",
    "Leo": "사자자리",
    "Virgo": "처녀자리",
    "Libra": "천칭자리",
    "Scorpio": "전갈자리",
    "Sagittarius": "궁수자리",
    "Capricorn": "염소자리"
}

relation_map = {
    "Brother": "형제",
    "Sister": "자매",
    "Cousin": "사촌",
    "Uncle": "삼촌",
    "Aunt": "이모/고모",
    "Nephew": "조카"
}

# 1. Read NPC info into a dictionary
npc_info = {}
with open(npc_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        npc_id = row.get("NPCID", "")
        if npc_id:
            npc_info[npc_id] = row

# 2. Process characters.csv
new_rows = []
fieldnames = []

with open(characters_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    
    # We want to insert "생일", "별자리", "나이", "가족관계" right after "Pic"
    try:
        pic_idx = header.index("Pic")
    except ValueError:
        pic_idx = 3 # default
        
    # Create new header
    fieldnames = header[:pic_idx+1] + ["생일", "별자리", "나이", "가족관계"] + header[pic_idx+1:]
    
    for row in reader:
        # Pad row to match old header length just in case
        row_dict = dict(zip(header, row))
        
        c_npc_id = row_dict.get("NPCID", "")
        c_name = row_dict.get("Name", "")
        
        # Determine the key to lookup in npc_info
        lookup_key = c_npc_id
        if lookup_key not in npc_info and c_name in npc_info:
            lookup_key = c_name
            
        bday_str = ""
        zodiac_str = ""
        age_str = ""
        family_str = ""
        
        if lookup_key in npc_info:
            info = npc_info[lookup_key]
            
            # Birthday
            season = info.get("BirthSeason", "")
            day = info.get("Birthday", "")
            if season and day:
                bday_str = f"{season_map.get(season, season)} {day}일"
                
            # Zodiac
            z = info.get("Zodiac", "")
            if z:
                zodiac_str = zodiac_map.get(z, z)
                
            # Age
            age = info.get("BirthYear", "")
            if age:
                age_str = f"{age}세"
                
            # Family
            fam = info.get("FamilyMembers", "")
            if fam and fam != "()":
                # fam looks like: ((""Rio"", ""Brother""),(""Sebastian"", ""Brother""))
                matches = re.findall(r'"([^"]+)",\s*"([^"]+)"', fam)
                if matches:
                    f_list = []
                    for name, rel in matches:
                        rel_kr = relation_map.get(rel, rel)
                        f_list.append(f"{name} ({rel_kr})")
                    family_str = ", ".join(f_list)
                else:
                    family_str = fam
                    
        # Construct new row
        new_row = []
        for h in fieldnames:
            if h == "생일":
                new_row.append(bday_str)
            elif h == "별자리":
                new_row.append(zodiac_str)
            elif h == "나이":
                new_row.append(age_str)
            elif h == "가족관계":
                new_row.append(family_str)
            else:
                new_row.append(row_dict.get(h, ""))
        new_rows.append(new_row)

# 3. Write back to characters.csv
with open(characters_path, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(fieldnames)
    writer.writerows(new_rows)

print("characters.csv updated successfully!")
