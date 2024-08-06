import os
from PIL import Image

src_folder = './0.origin_images'
flip_folder = './3.flipped'
output_folder = './1.converted_to_jpg'

if not os.path.exists(flip_folder):
    os.makedirs(flip_folder)
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(src_folder):
    try:
        if filename.lower().endswith(('.jpg', '.png', '.jpeg', '.webp')):
            src_path = os.path.join(src_folder, filename)
            image = Image.open(src_path).convert("RGB")
            output_path = os.path.join(flip_folder, filename)            
            temp_image = image.transpose(Image.FLIP_LEFT_RIGHT)
            rotated_image = temp_image.transpose(Image.FLIP_LEFT_RIGHT)
            rotated_image.save(output_path)
            # print(f'Flipped {filename} and saved it to {os.path.basename(output_path)}')
        else:
            print(f"Skipping {filename} as it is not a supported image format.")
    except (IOError):
        print(f"Error processing {filename}. Skipping...")
        continue

for filename in os.listdir(flip_folder):
    try:
        if filename.lower().endswith(('.jpg', '.png', '.jpeg', '.webp')):
          output_path = os.path.join(flip_folder, filename)
          dst_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.jpg')
          with Image.open(output_path) as rotated_image:
              rotated_image.save(dst_path, 'JPEG', quality=90)
          os.remove(output_path)
        #   print(f'Converted {filename} to {os.path.basename(dst_path)}')
    except (IOError):
        print(f"Error processing {filename}. Skipping...")
        continue