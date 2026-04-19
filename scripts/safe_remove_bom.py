import os

def remove_bom(directory):
    for root, dirs, files in os.walk(directory):
        if '.git' in root: continue
        for filename in files:
            if filename.endswith(('.html', '.md', '.yml', '.csv')):
                filepath = os.path.join(root, filename)
                try:
                    with open(filepath, 'rb') as f:
                        data = f.read()
                    if data.startswith(b'\xef\xbb\xbf'):
                        print(f"Removing BOM from {filepath}")
                        with open(filepath, 'wb') as f:
                            f.write(data[3:])
                except Exception as e:
                    print(f"Error processing {filepath}: {e}")

if __name__ == "__main__":
    remove_bom(".")
