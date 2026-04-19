import os
import re

src = 'RowData'
dst = 'lorebook/story'
os.makedirs(dst, exist_ok=True)

def get_content(f):
    path = os.path.join(src, f)
    if not os.path.exists(path):
        return ""
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        # Remove the first H1 if it's a title
        if lines and lines[0].startswith('#'):
            return ''.join(lines[1:])
        return ''.join(lines)

# Process Chapters 1 and 2 (Merged)
chapters_data = {
    1: {
        "title": "제 1장. 이야기의 시작, 그리고 남겨진 따스함",
        "files": ['Chapter_1_Part1.md', 'Chapter_1_Part2.md', 'Chapter_1_Part3.md', 'Chapter_1_Part4.md']
    },
    2: {
        "title": "제 2장. 과거의 열쇠와 윈터캠프",
        "files": ['Chapter_2_Part1.md', 'Chapter_2_Part2-3.md', 'Chapter_2_Part4-5.md']
    }
}

# Add all other chapters
for i in range(3, 30):
    chapters_data[i] = {
        "title": f"제 {i}장",
        "files": [f"Chapter_{i}.md"]
    }

# Write files
for i in range(1, 30):
    data = chapters_data[i]
    if not any(os.path.exists(os.path.join(src, f)) for f in data['files']):
        continue

    output_path = os.path.join(dst, f"chapter-{i:02d}.md")
    prev_link = f"/lorebook/story/chapter-{i-1:02d}/" if i > 1 else ""
    prev_title = chapters_data.get(i-1, {}).get("title", f"제 {i-1}장") if i > 1 else ""
    next_link = f"/lorebook/story/chapter-{i+1:02d}/" if i < 29 else ""
    next_title = chapters_data.get(i+1, {}).get("title", f"제 {i+1}장") if i < 29 else ""

    content = ""
    for f in data['files']:
        content += get_content(f) + "\n\n"

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("---\n")
        f.write("layout: story\n")
        f.write(f"title: \"{data['title']}\"\n")
        f.write(f"chapter_num: {i}\n")
        if prev_link:
            f.write(f"prev_chapter: \"{prev_link}\"\n")
            f.write(f"prev_title: \"{prev_title}\"\n")
        if next_link:
            f.write(f"next_chapter: \"{next_link}\"\n")
            f.write(f"next_title: \"{next_title}\"\n")
        f.write("---\n\n")
        f.write(content)

print("Story chapters processed successfully.")
