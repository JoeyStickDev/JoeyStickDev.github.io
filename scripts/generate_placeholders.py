from PIL import Image, ImageDraw
import os

def create_pixel_placeholder(path):
    # Create 128x128 image with a dark theme
    img = Image.new('RGB', (128, 128), color=(30, 34, 42))
    draw = ImageDraw.Draw(img)
    
    # Subtle center square instead of a full checkerboard
    draw.rectangle([32, 32, 95, 95], fill=(40, 44, 52))
    
    # Gold border for premium feel
    draw.rectangle([0, 0, 127, 127], outline=(252, 163, 17), width=4)
    
    # Save the image
    img.save(path)

def main():
    base_dir = "assets/images"
    for root, dirs, files in os.walk(base_dir):
        # Skip the base directory itself and the categories banner folder
        if root == base_dir or "categories" in root:
            continue
            
        # Only create placeholder in leaf folders (category subfolders)
        # or if it's a direct child folder with no subfolders
        placeholder_path = os.path.join(root, "example.png")
        create_pixel_placeholder(placeholder_path)

if __name__ == "__main__":
    main()
