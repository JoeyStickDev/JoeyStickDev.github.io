import json
import csv
import re

calendar_path = r"f:\Git\JoeyStickDev.github.io\_data\calendar_events.json"
characters_path = r"f:\Git\JoeyStickDev.github.io\_data\characters.csv"

option_mapping = {
    "물병자리": ["최소스탯증가", "인트증가", "얼음대미지"],
    "물고기자리": ["HP,MP,스테미나증가", "인트증가", "얼음대미지"],
    "양자리": ["크리티컬대미지증가", "힘증가", "불대미지"],
    "황소자리": ["방어력증가", "힘증가", "전기대미지"],
    "쌍둥이자리": ["스킬쿨타임감소", "덱스증가", "전기대미지"],
    "게자리": ["최대스탯증가", "인트증가", "얼음대미지"],
    "사자자리": ["보너스대미지증가", "힘증가", "불대미지"],
    "처녀자리": ["기동성증가", "덱스증가", "전기대미지"],
    "천칭자리": ["크리티컬확률증가", "행운증가", "얼음대미지"],
    "전갈자리": ["크리티컬대미지증가", "행운증가", "전기대미지"],
    "사수자리": ["스킬쿨타임감소", "덱스증가", "불대미지"],
    "궁수자리": ["스킬쿨타임감소", "덱스증가", "불대미지"],
    "염소자리": ["방어력증가", "행운증가", "불대미지"]
}

# 1. Update calendar_events.json
with open(calendar_path, 'r', encoding='utf-8') as f:
    events = json.load(f)

for e in events:
    name = e.get("name", "")
    if "자리 시작" in name:
        zodiac_name = name.split(" 시작")[0]
        if zodiac_name in option_mapping:
            opts = option_mapping[zodiac_name]
            opt_str = f"옵션1: {opts[0]} / 옵션2: {opts[1]} / 옵션3: {opts[2]}"
            
            # append only if not already appended
            desc = e.get("desc", "")
            if "[별자리 효과]" not in desc:
                e["desc"] = desc + f"\n\n[별자리 효과]\n{opt_str}"

with open(calendar_path, 'w', encoding='utf-8') as f:
    json.dump(events, f, ensure_ascii=False, indent=2)

# 2. Update characters.csv
with open(characters_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

if "별자리 효과" not in header:
    z_idx = header.index("별자리")
    header.insert(z_idx + 1, "별자리 효과")
    for row in rows:
        zodiac = row[z_idx]
        effect = ""
        if zodiac in option_mapping:
            opts = option_mapping[zodiac]
            effect = f"{opts[0]}, {opts[1]}, {opts[2]}"
        row.insert(z_idx + 1, effect)
else:
    z_idx = header.index("별자리")
    ef_idx = header.index("별자리 효과")
    for row in rows:
        zodiac = row[z_idx]
        if zodiac in option_mapping:
            opts = option_mapping[zodiac]
            row[ef_idx] = f"{opts[0]}, {opts[1]}, {opts[2]}"

with open(characters_path, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

print("Updated calendar_events.json and characters.csv successfully!")
