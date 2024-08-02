import os
from PIL import Image

source_folder = "./2.flipped"
destination_folder = "./3.rotated"

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

for filename in os.listdir(source_folder):
    try:
        if filename.lower().endswith(('.jpg', '.png', '.jpeg', '.webp')):
            image_path = os.path.join(source_folder, filename)
            image = Image.open(image_path)
            rotated_image = image.rotate(10)
            rotated_image_path = os.path.join(destination_folder, "!" + filename)
            rotated_image.save(rotated_image_path)
    except IOError:
        print(f"File not found: {filename}. Skipping...")
        continue