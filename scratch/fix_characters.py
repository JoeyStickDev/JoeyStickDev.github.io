import csv
import os

csv_path = "_data/characters.csv"
temp_path = "_data/characters_temp.csv"

with open(csv_path, "r", encoding="utf-8") as f, open(temp_path, "w", encoding="utf-8", newline="") as out:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(out, fieldnames=fieldnames)
    writer.writeheader()
    
    for row in reader:
        pic = row.get("Pic", "")
        if pic:
            # Fix double slashes
            pic = pic.replace("//", "/")
            # Append .png if missing
            if not pic.lower().endswith(".png") and not pic.lower().endswith(".jpg"):
                pic += ".png"
            row["Pic"] = pic
        writer.writerow(row)

os.replace(temp_path, csv_path)
print("Finished fixing characters.csv")
