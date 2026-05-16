import csv
import re

mbti_path = r"f:\Git\JoeyStickDev.github.io\Temp\NPC_MBTI_DT.csv"
npc_dt_path = r"f:\Git\JoeyStickDev.github.io\Temp\NPC_DT.csv"

# 1. Read MBTI to get the names
names = []
with open(mbti_path, 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if len(row) >= 3:
            names.append(row[1])

# 2. Read NPC_DT.csv
with open(npc_dt_path, 'r', encoding='utf-16') as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

talk_list_idx = header.index("TalkListRowNames")

# Update each row
for row in rows:
    npc_name = row[1] # NPCID or Name. In NPC_DT, Name is column 2, NPCID is column 1
    # Actually, column 1 is NPCID (e.g., Angela), column 2 is Name (e.g. LOCTABLE...)
    if npc_name in names:
        # Generate the new names to add
        new_items = []
        for cat in ["Friendship", "Relationship", "Joke"]:
            for i in range(3):
                new_items.append(f"{npc_name}_{cat}_{i}")
        
        # Read existing TalkListRowNames
        current_talks = row[talk_list_idx]
        if current_talks == "()":
            current_talks = ""
            
        # Remove parentheses and split by comma
        cleaned = current_talks.strip("()")
        if cleaned:
            # e.g. ""Friendship_0"",""Relationship_1"",""Wicked_0""
            # Use regex or just string splitting
            # Actually, the python csv reader removes outer quotes, so current_talks is like:
            # ("Friendship_0","Relationship_1","Wicked_0")
            existing_items = re.findall(r'"([^"]+)"', cleaned)
        else:
            existing_items = []
            
        # Append new items if not already there
        for item in new_items:
            if item not in existing_items:
                existing_items.append(item)
                
        # Reconstruct
        # Wait, the inner string needs to be formatted like:
        # ("Friendship_0","Relationship_1","Wicked_0","Angela_Friendship_0",...)
        # In Python string:
        # '("Friendship_0","Relationship_1","Wicked_0","Angela_Friendship_0")'
        # The csv writer will wrap it in quotes and escape inner quotes if necessary, 
        # but actually we just need to provide the exact string we want inside the field.
        new_val = "(" + ",".join([f'"{x}"' for x in existing_items]) + ")"
        
        row[talk_list_idx] = new_val

with open(npc_dt_path, 'w', encoding='utf-16', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

print("Updated TalkListRowNames in NPC_DT.csv successfully!")
