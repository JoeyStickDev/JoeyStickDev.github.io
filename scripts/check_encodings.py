import os

def check_encoding(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    f.read()
                print(f"{filename}: UTF-8 OK")
            except UnicodeDecodeError:
                print(f"{filename}: NOT UTF-8")

if __name__ == "__main__":
    check_encoding("_data")
