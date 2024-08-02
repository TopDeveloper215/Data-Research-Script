import os
import shutil
from PIL import Image

source_folder1 = './2.flipped'
source_folder2 = './5.resized'
output_folder = './6.final_result'
target_size = (1280, 960)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(source_folder1):
    if filename.lower().endswith(('.jpg', '.png', '.jpeg', '.webp')):
        source_file = os.path.join(source_folder1, filename)
        destination_file = os.path.join(output_folder, filename)
        shutil.copy2(source_file, destination_file)

for filename in os.listdir(source_folder2):
    if filename.lower().endswith(('.jpg', '.png', '.jpeg', '.webp')):
        source_file = os.path.join(source_folder2, filename)
        destination_file = os.path.join(output_folder, filename)
        shutil.copy2(source_file, destination_file)
        print(f'All folder copied {filename} to {output_folder}')

for filename in os.listdir(output_folder):
    if filename.lower().endswith(('.jpg', '.png', '.jpeg', '.webp')):
        file_path = os.path.join(output_folder, filename)
        image = Image.open(file_path)
        resized_image = image.resize(target_size, resample=Image.BICUBIC)
        output_file_path = os.path.join(output_folder, filename)
        resized_image.save(output_file_path)
        print(f'Final result images has been resized')