import os

folder_path = './2.flipped'
for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.jpg', '.png', '.jpeg', '.webp')):        
        new_filename = "!" + filename
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))