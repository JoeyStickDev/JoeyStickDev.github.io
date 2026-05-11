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
            
        full_path = os.path.join(img_dir, pic)
        
        if not os.path.exists(full_path):
            print(f"Missing: {pic} for character {row['ID']}")

