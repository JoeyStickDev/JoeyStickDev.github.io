import csv

mbti_path = r"f:\Git\JoeyStickDev.github.io\Temp\NPC_MBTI_DT.csv"
characters_path = r"f:\Git\JoeyStickDev.github.io\_data\characters.csv"

# 1. Read MBTI data
mbti_data = {}
with open(mbti_path, 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    header = next(reader)
    # ---,Name,MBTI,RespectLanguage,Warmth
    for row in reader:
        if len(row) >= 5:
            name = row[1]
            mbti = row[2]
            respect = "존댓말" if row[3].upper() == "TRUE" else "반말"
            warmth = f"{row[4]}/5"
            mbti_data[name] = {"MBTI": mbti, "말투": respect, "따스함": warmth}

# 2. Update characters.csv
with open(characters_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    char_header = next(reader)
    char_rows = list(reader)

# Check if columns already exist
new_cols = ["MBTI", "말투", "따스함"]
for col in new_cols:
    if col not in char_header:
        # Insert after Name or Pic
        idx = char_header.index("Name") + 1
        char_header.insert(idx, col)
        
        for row in char_rows:
            row.insert(idx, "")

# Find indices
name_idx = char_header.index("Name")
mbti_idx = char_header.index("MBTI")
tone_idx = char_header.index("말투")
warmth_idx = char_header.index("따스함")

# Update rows
for row in char_rows:
    c_name = row[name_idx]
    
    # Try to find match. characters.csv might have Event_ names, but their Name column might match
    lookup_name = c_name
    
    if lookup_name in mbti_data:
        data = mbti_data[lookup_name]
        row[mbti_idx] = data["MBTI"]
        row[tone_idx] = data["말투"]
        row[warmth_idx] = data["따스함"]

with open(characters_path, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(char_header)
    writer.writerows(char_rows)

print("characters.csv updated with MBTI data!")
