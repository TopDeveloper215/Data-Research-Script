import os
import shutil

source_folder1 = './2.flipped'
source_folder2 = './5.resized'
destination_folder = './6.result'

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

for filename in os.listdir(source_folder1):
    if filename.lower().endswith(('.jpg', '.png', '.jpeg', '.webp')):
        source_file = os.path.join(source_folder1, filename)
        destination_file = os.path.join(destination_folder, filename)
        shutil.copy2(source_file, destination_file)
        print(f'First folder copied {filename} to {destination_folder}')

for filename in os.listdir(source_folder2):
    if filename.lower().endswith(('.jpg', '.png', '.jpeg', '.webp')):
        source_file = os.path.join(source_folder2, filename)
        destination_file = os.path.join(destination_folder, filename)
        shutil.copy2(source_file, destination_file)
        print(f'Second folder copied {filename} to {destination_folder}')