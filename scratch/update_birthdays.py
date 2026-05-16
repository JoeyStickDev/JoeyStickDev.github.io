import json
import csv

calendar_path = r"f:\Git\JoeyStickDev.github.io\_data\calendar_events.json"
csv_path = r"f:\Git\JoeyStickDev.github.io\Temp\NPC_DetailInfo_DT.csv"

# Read JSON
with open(calendar_path, "r", encoding="utf-8") as f:
    events = json.load(f)

# Filter out old birthdays
new_events = [e for e in events if e.get("type") != "birthday"]

# Read CSV
birthdays = []
with open(csv_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        npc_id = row.get("NPCID")
        if not npc_id or npc_id.startswith("Test"):
            continue
            
        job = row.get("Job", "")
        zodiac = row.get("Zodiac", "")
        season = row.get("BirthSeason", "")
        day_str = row.get("Birthday", "")
        
        try:
            day = int(day_str)
        except:
            continue
            
        birthdays.append({
            "season": season,
            "day": day,
            "type": "birthday",
            "name": f"{npc_id} 생일",
            "desc": f"직업: {job} / 별자리: {zodiac}\n{npc_id}의 생일입니다."
        })

# Prepend birthdays to keep them at the top as before
# Sort birthdays by season and day for better organization (optional, but good)
season_order = {"Spring": 1, "Summer": 2, "Fall": 3, "Winter": 4}
birthdays.sort(key=lambda x: (season_order.get(x["season"], 99), x["day"]))

final_events = birthdays + new_events

with open(calendar_path, "w", encoding="utf-8") as f:
    json.dump(final_events, f, ensure_ascii=False, indent=2)

print(f"Updated {len(birthdays)} birthdays successfully.")
