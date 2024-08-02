import os
from PIL import Image

input_folder = './4.cropped'
output_folder = './5.resized'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    try:
        if filename.lower().endswith(('.jpg', '.png', '.jpeg', '.webp')):  
            image_path = os.path.join(input_folder, filename)
            image = Image.open(image_path)
            width, height = image.size
            width_1 = int(width /0.88) 
            height_1 = int(height/ 0.76) 
            zoomed_image = image.resize((width_1, height_1), resample=Image.BICUBIC)
            output_path = os.path.join(output_folder, filename)
            zoomed_image.save(output_path)
    except IOError:
        print(f"File not found: {filename}. Skipping...")
        continue