import os
import shutil
from PIL import Image

source_folder1 = './2.flipped'
source_folder2 = './5.resized'
temp_folder = './6.converted_to_png'
output_folder = './7.final_result'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

if not os.path.exists(temp_folder):
    os.makedirs(temp_folder)

for filename in os.listdir(source_folder1):
    if filename.lower().endswith(('.jpg', '.png', '.jpeg', '.webp')):
        source_file = os.path.join(source_folder1, filename)
        output_file = os.path.join(temp_folder, filename)
        shutil.copy2(source_file, output_file)

for filename in os.listdir(source_folder2):
    if filename.lower().endswith(('.jpg', '.png', '.jpeg', '.webp')):
        source_file = os.path.join(source_folder2, filename)
        output_file = os.path.join(temp_folder, filename)
        shutil.copy2(source_file, output_file)
        print(f'All folder copied {filename} to {output_folder}')

for filename in os.listdir(temp_folder):
    try:
        if filename.lower().endswith(('.jpg', '.png', '.jpeg', '.webp')):
          output_path = os.path.join(temp_folder, filename)
          dst_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.png')
          with Image.open(output_path) as rotated_image:
              rotated_image.save(dst_path, 'PNG', quality=90)
          os.remove(output_path)
    except (IOError):
        print(f"Error processing {filename}. Skipping...")
        continue