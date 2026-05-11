import csv
import os

csv_path = "_data/characters.csv"
img_dir = "assets/images/characters"

with open(csv_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        pic = row.get("Pic", "").strip()
        if not pic:
            continue
            
        if not pic.endswith(".png") and not pic.endswith(".jpg"):
            pic += ".png"
            
        parts = pic.split('/')
        
        current_path = img_dir
        broken = False
        for part in parts:
            if not part:
                continue
            try:
                actual_files = os.listdir(current_path)
            except:
                print(f"Path not found: {current_path}")
                broken = True
                break
                
            if part not in actual_files:
                print(f"Broken Case/Path for {row['ID']}: expected '{part}' in {current_path}")
                broken = True
                break
            current_path = os.path.join(current_path, part)

