import os
import csv
import shutil

# Mapping of dataset name to its category column key
MAPPING = {
    'active_skills': 'SkillType',
    'artisans': 'Tag',
    'buff_skills': 'IsDebuff',
    'characters': 'Job',
    'crafting': 'RequiredSklillName',
    'creatures': 'Level',
    'crops': 'Season',
    'fishes': 'Season',
    'items': 'Category',
    'passive_skills': 'SkillType',
    'quests': 'QuestType'
}

def sync_images():
    base_img_dir = "assets/images"
    
    for dataset, cat_key in MAPPING.items():
        csv_path = f"_data/{dataset}.csv"
        if not os.path.exists(csv_path):
            continue
            
        print(f"Syncing images for {dataset}...")
        
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                category = row.get(cat_key, "").strip()
                # Use Image_Filename, fallback to Image, fallback to RowName/ID
                img_name = row.get('Image_Filename') or row.get('Image') or row.get('ID') or row.get('RowName')
                
                if not category or not img_name:
                    continue
                
                # Normalize category folder name (matching how folders were created)
                safe_cat = category # Assuming folders exist as is
                cat_dir = os.path.join(base_img_dir, dataset, safe_cat)
                
                source_img = os.path.join(cat_dir, "example.png")
                target_img = os.path.join(cat_dir, f"{img_name}.png")
                
                if os.path.exists(source_img) and not os.path.exists(target_img):
                    try:
                        shutil.copy(source_img, target_img)
                    except Exception as e:
                        print(f"Error copying to {target_img}: {e}")

if __name__ == "__main__":
    sync_images()
