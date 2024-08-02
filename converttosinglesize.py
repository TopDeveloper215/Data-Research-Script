import os
from PIL import Image

folder_path = './0.origin_images'
output_folder = './1.size_changed'
target_size = (1280, 960)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.jpg', '.png', '.jpeg', '.webp')):
        file_path = os.path.join(folder_path, filename)
        image = Image.open(file_path)
        resized_image = image.resize(target_size, resample=Image.BICUBIC)
        output_file_path = os.path.join(output_folder, filename)
        resized_image.save(output_file_path)