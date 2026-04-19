import os

def check_all_files(root_dir):
    exts = ['.csv', '.md', '.html', '.yml']
    for root, dirs, files in os.walk(root_dir):
        if '.git' in root: continue
        for filename in files:
            if any(filename.endswith(ext) for ext in exts):
                filepath = os.path.join(root, filename)
                try:
                    with open(filepath, 'rb') as f:
                        content = f.read()
                    content.decode('utf-8')
                except UnicodeDecodeError:
                    print(f"ENCODING ERROR: {filepath}")

if __name__ == "__main__":
    check_all_files(".")
