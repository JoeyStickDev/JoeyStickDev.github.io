import json
import re
import os

def clean_text(text):
    if not text: return ""
    # Remove NSLOCTEXT tags and return only the text part
    match = re.search(r'\",\s*\"(.*?)\"\)', text)
    if match:
        return match.group(1).replace("\\'", "'")
    return text

def process_quests():
    try:
        data = json.load(open('Quest_DT.json', encoding='utf-16'))
    except Exception as e:
        print(f"Error loading JSON: {e}")
        return

    # Ensure data is a list
    if not isinstance(data, list):
        data = list(data.values())

    dst_base = 'lorebook/story'
    
    for row in data:
        qid = row.get('QuestID', '')
        qtype = ""
        if qid.startswith('S_'): qtype = 'sub-quests'
        elif qid.startswith('SK_'): qtype = 'skill-quests'
        else: continue # Skip main or others already handled
        
        target_dir = os.path.join(dst_base, qtype)
        os.makedirs(target_dir, exist_ok=True)
        
        name = clean_text(row.get('QuestName', 'Untitled'))
        before = " ".join([clean_text(t) for t in row.get('BeforeDetail', [])])
        progress = " ".join([clean_text(t) for t in row.get('ProgressDetail', [])])
        complete = " ".join([clean_text(t) for t in row.get('CompleteDetail', [])])
        
        # Safe filename
        safe_name = re.sub(r'[^\w\s-]', '', name).strip().replace(' ', '-')
        fname = f"{qid}-{safe_name}.md".lower()
        
        with open(os.path.join(target_dir, fname), 'w', encoding='utf-8') as f:
            f.write("---\n")
            f.write("layout: story\n")
            f.write(f"title: \"{name}\"\n")
            f.write(f"quest_id: \"{qid}\"\n")
            f.write(f"category: \"{qtype}\"\n")
            f.write("---\n\n")
            f.write(f"## {name}\n\n")
            f.write(f"### 퀘스트 배경\n{before}\n\n")
            f.write(f"### 진행 상황\n{progress}\n\n")
            f.write(f"### 완료\n{complete}\n")

if __name__ == "__main__":
    process_quests()
    print("Sub and Skill quests processed into storybook.")
