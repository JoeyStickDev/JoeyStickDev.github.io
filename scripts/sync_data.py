import csv
import os
import re

# Paths
ROW_DATA_DIR = r"f:\Git\JoeyStickDev.github.io\RowData"
OUTPUT_DATA_DIR = r"f:\Git\JoeyStickDev.github.io\_data"

# Ensure output directory exists
os.makedirs(OUTPUT_DATA_DIR, exist_ok=True)

def clean_nsloctext(text):
    if not text:
        return ""
    # Matches NSLOCTEXT("...", "...", "Actual Text")
    match = re.search(r'NSLOCTEXT\(".*?",\s*".*?",\s*"(.*?)"\)', text)
    if match:
        return match.group(1)
    # Sometimes it's missing the middle part or has different quotes
    match = re.search(r'NSLOCTEXT\(.*?,.*?,.*?"(.*?)"\)', text)
    if match:
        return match.group(1)
    return text

def clean_unreal_path(path):
    if not path or path == "None":
        return ""
    # Extract filename from path like /Game/.../Fire_PNG.Fire_PNG
    match = re.search(r'\.([^.]+)$', path)
    if match:
        filename = match.group(1)
        return filename
    return path

def clean_ingredients(ing_str):
    if not ing_str or ing_str == "()":
        return ""
    # Format: (("Item_ID", count), ("Item_ID", count))
    items = re.findall(r'\("?([^",\s]+)"?,\s*(\d+)\)', ing_str)
    if not items:
        # Try another format if needed
        items = re.findall(r'([^",\s]+):\s*(\d+)', ing_str)
    
    cleaned = []
    for item_id, count in items:
        name = item_id.replace("Material_", "").replace("Crops_", "").replace("Seed_", "")
        cleaned.append(f"{name} x{count}")
    return ", ".join(cleaned)

def process_csv(filename, output_name, mapping=None, key_field=None):
    input_path = os.path.join(ROW_DATA_DIR, filename)
    output_path = os.path.join(OUTPUT_DATA_DIR, output_name)
    
    if not os.path.exists(input_path):
        print(f"File not found: {input_path}")
        return

    encodings = ['utf-8-sig', 'utf-16', 'utf-16-le', 'utf-8', 'cp1252']
    
    for enc in encodings:
        rows = []
        try:
            with open(input_path, 'r', encoding=enc) as f:
                # Check if file has content
                sample = f.read(1024)
                if not sample: continue
                f.seek(0)
                
                # Check for Unreal header
                first_line = f.readline()
                if first_line.startswith('---'):
                    header = first_line.strip().split(',')
                    header[0] = 'ID'
                else:
                    f.seek(0)
                    header = None
                
                reader = csv.DictReader(f, fieldnames=header)
                if header is None:
                    # DictReader consumes first line as header, so we don't need to skip
                    pass
                
                for row in reader:
                    cleaned_row = {}
                    for k, v in row.items():
                        if k is None: continue
                        
                        val = v
                        if isinstance(val, str):
                            val = clean_nsloctext(val)
                            # Image filename handling
                            if any(x in k for x in ["Image", "PicData", "Icon"]):
                                img_fn = clean_unreal_path(val)
                                if img_fn:
                                    cleaned_row[k + "_Filename"] = img_fn
                            
                            # Clean other Unreal paths
                            if any(x in k for x in ["BP", "Class", "Mesh"]):
                                val = clean_unreal_path(val)
                            
                            if k == "Ingridient":
                                val = clean_ingredients(val)
                        
                        cleaned_row[k] = val
                    
                    # Name mapping
                    for mk in [key_field, 'ID', 'RowName', 'SkillRowName', 'ItemRowName', 'QuestRowName']:
                        if mk in cleaned_row:
                            kv = cleaned_row[mk]
                            if kv in mapping:
                                cleaned_row["DisplayName"] = mapping[kv]
                                break
                    
                    rows.append(cleaned_row)
            
            if rows:
                fieldnames = rows[0].keys()
                with open(output_path, 'w', encoding='utf-8', newline='') as f_out:
                    writer = csv.DictWriter(f_out, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)
                print(f"Processed {filename} -> {output_name} ({len(rows)} rows) using {enc}")
                return # Success
        except Exception as e:
            continue
            
    print(f"Failed to process {filename}")

def load_mapping():
    mapping = {}
    st_path = os.path.join(ROW_DATA_DIR, "ItemName_ST_DT.csv")
    if not os.path.exists(st_path): return mapping

    for enc in ['utf-8-sig', 'utf-16', 'utf-16-le', 'utf-8']:
        try:
            with open(st_path, 'r', encoding=enc) as f:
                reader = csv.DictReader(f)
                for row in reader:
                    mapping[row['Key']] = row['SourceString']
            return mapping
        except:
            continue
    return mapping

def main():
    mapping = load_mapping()
    
    # Skills
    process_csv("Skills_DT.csv", "active_skills.csv", mapping, "SkillName")
    process_csv("PassiveSkill_DT.csv", "passive_skills.csv", mapping, "SkillName")
    process_csv("BuffData_DT.csv", "buff_skills.csv", mapping, "BuffName")
    
    # World
    process_csv("PlantData_DT.csv", "crops.csv", mapping, "PlantRowName")
    process_csv("FishData_DT.csv", "fishes.csv", mapping, "FishRowName")
    process_csv("Quest_DT.csv", "quests.csv", mapping, "QuestRowName")
    
    # Economy
    process_csv("CraftData_DT.csv", "crafting.csv", mapping, "RowName")
    process_csv("ItemData_DT.csv", "items.csv", mapping, "RowName")
    process_csv("MakingData_DT.csv", "artisans.csv", mapping, "RowName")
    
    # Characters
    process_csv("NPC_DT.csv", "characters.csv", mapping, "NPCRowName")

if __name__ == "__main__":
    main()
