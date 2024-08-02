import os
import shutil

source_folder = './1.size_changed'
output_folder = './2.flipped'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(source_folder):
    if filename.lower().endswith(('.jpg', '.png', '.jpeg', '.webp')):
        source_file = os.path.join(source_folder, filename)
        destination_file = os.path.join(output_folder, filename)
        shutil.copy2(source_file, destination_file)
