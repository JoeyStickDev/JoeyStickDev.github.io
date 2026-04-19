import csv

def update_active_skills_images():
    path = '_data/active_skills.csv'
    rows = []
    
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            skill_name = row['SkillName']
            # Update to [SkillName].png
            row['SkillImage'] = f"{skill_name}.png"
            row['SkillImage_Filename'] = skill_name
            rows.append(row)
            
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    update_active_skills_images()
