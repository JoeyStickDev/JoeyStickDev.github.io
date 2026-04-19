import os
import csv
import shutil

# Mapping of dataset name to its category column key
MAPPING = {
    'active_skills': 'SkillType',
    'achievements': 'Category',
    'artisans': 'Tag',
    'buff_skills': 'IsDebuff',
    'characters': 'LocationName',
    'crafting': 'RequiredSklillName',
    'creatures': 'Level',
    'crops': 'Season',
    'fishes': 'Season',
    'items': 'Category',
    'passive_skills': 'SkillType',
    'quests': 'Category_Kor'
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
                # Try multiple possible image name columns
                img_name = (row.get('Image_Filename') or 
                            row.get('SkillImage_Filename') or 
                            row.get('Image') or 
                            row.get('SkillImage') or
                            row.get('ID') or 
                            row.get('QuestID')).replace(".png", "")
                
                if not category or not img_name:
                    continue
                
                cat_dir = os.path.join(base_img_dir, dataset, category)
                
                # Check for example.png in the category folder or the dataset folder
                source_img = os.path.join(cat_dir, "example.png")
                if not os.path.exists(source_img):
                    source_img = os.path.join(base_img_dir, dataset, "example.png")
                
                target_img = os.path.join(cat_dir, f"{img_name}.png")
                
                if os.path.exists(source_img) and not os.path.exists(target_img):
                    try:
                        shutil.copy(source_img, target_img)
                    except Exception as e:
                        pass # Silently skip errors

if __name__ == "__main__":
    sync_images()
