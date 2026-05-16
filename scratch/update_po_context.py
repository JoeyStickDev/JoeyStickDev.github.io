import csv
import re
import os

mbti_path = r"f:\Git\JoeyStickDev.github.io\Temp\NPC_MBTI_DT.csv"
quest_path = r"f:\Git\JoeyStickDev.github.io\Temp\QuestDialog_DT.csv"
talk_path = r"f:\Git\JoeyStickDev.github.io\Temp\NPC_TalkData_DT.csv"
po_path = r"f:\Git\JoeyStickDev.github.io\Temp\Game.po"
out_po_path = r"f:\Git\JoeyStickDev.github.io\Temp\Game_Fixed.po"

# 1. Load MBTI Data
mbti_info = {}
with open(mbti_path, 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if len(row) >= 4:
            name = row[1]
            mbti = row[2]
            respect = row[3].upper() == "TRUE"
            tone = "존댓말(Polite, honorifics)" if respect else "반말(Casual, informal)"
            mbti_info[name] = {"MBTI": mbti, "Tone": tone}

# 2. Extract Keys from QuestDialog
key_to_char = {}

with open(quest_path, 'r', encoding='utf-16', errors='replace') as f:
    content = f.read()
    # Find patterns like Title=LOCTABLE(..., "Name_Joey")...Contents=NSLOCTEXT(..., "KEY",
    # Note: Sometimes Title=LOCTABLE is for "A_System", which is not an NPC.
    matches = re.finditer(r'Title=LOCTABLE\([^,]+,\s*"Name_([^"]+)"\).*?Contents=NSLOCTEXT\([^,]+,\s*"([^"]+)"', content, re.DOTALL)
    for m in matches:
        npc_name = m.group(1)
        key = m.group(2)
        if npc_name in mbti_info:
            key_to_char[key] = npc_name

# 3. Extract Keys from NPC_TalkData
with open(talk_path, 'r', encoding='utf-16', errors='replace') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) > 3:
            row_name = row[1]
            details = row[3]
            # Try to infer name from RowName (e.g. Leon_MBTI_Talk)
            parts = row_name.split('_')
            npc_name = parts[0]
            
            if npc_name in mbti_info:
                # Find NSLOCTEXT KEY
                key_match = re.search(r'NSLOCTEXT\([^,]+,\s*"([^"]+)"', details)
                if key_match:
                    key = key_match.group(1)
                    key_to_char[key] = npc_name

print(f"Found {len(key_to_char)} dialog keys associated with NPCs.")

# 4. Process Game.po
with open(po_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
i = 0
added_comments = 0
while i < len(lines):
    line = lines[i]
    new_lines.append(line)
    
    # Match Key line: #. Key:    A2E5D06D42298683714B63BF1FD577B3
    if line.startswith("#. Key:"):
        key = line.split("Key:")[-1].strip()
        
        # Check if this key belongs to an NPC
        if key in key_to_char:
            npc = key_to_char[key]
            info = mbti_info[npc]
            
            # Inject a Poedit Context Comment right after the Key comment
            # Poedit reads "#. " as developer comments that help GPT!
            comment1 = f"#. [Poedit GPT Context] Speaker: {npc}\n"
            comment2 = f"#. [Poedit GPT Context] MBTI Personality: {info['MBTI']}\n"
            comment3 = f"#. [Poedit GPT Context] Required Korean Tone: {info['Tone']}\n"
            
            new_lines.append(comment1)
            new_lines.append(comment2)
            new_lines.append(comment3)
            added_comments += 1
            
    i += 1

with open(out_po_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f"Added context comments to {added_comments} translations!")
print(f"Saved as Game_Fixed.po. You can rename it to Game.po after verification.")
