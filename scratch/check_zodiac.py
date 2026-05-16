import json

file_path = r"f:\Git\JoeyStickDev.github.io\_data\calendar_events.json"

with open(file_path, 'r', encoding='utf-8') as f:
    events = json.load(f)

zodiac_events = [e for e in events if "별자리" in e.get("name", "") or e.get("type") == "jodiac" or e.get("type") == "zodiac"]

print(f"Found {len(zodiac_events)} zodiac events.")
for ze in zodiac_events:
    print(ze.get("name"))
