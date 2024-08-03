import csv
import os
import shutil

file_path = './8.passed_image_filter/data.csv'
image_folder = './0.origin_images'
filtered_folder = './8.passed_image_filter'

lists = []
passed_list = []
unique_names = set()

os.makedirs(filtered_folder, exist_ok=True)
with open(file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    for row in reader:
        if not row:
            continue
        file_path = row[2]
        lists.append(file_path)
        name_component = file_path.split('\\')[1]
        unique_names.add(name_component)

unique_names = sorted(list(unique_names))
print("All names:")
for i, name in enumerate(unique_names, start=1):
    print(f"{i}. {name}")

name_index = int(input("Please select name")) - 1
name_input = unique_names[name_index]

type_input = input("Please input type: ")
for list in lists:
    list_component = list.split('\\')
    if len(list_component) > 3:
        name = list_component[1]
        type = list_component[2]
        if name == name_input and type == type_input:
            each_passed_list = list_component[3]
            passed_list.append(each_passed_list)
    elif len(list_component) == 3:
        name = list_component[1]
        if name == name_input:
            each_passed_list = list_component[2]
            print(each_passed_list)
            passed_list.append(each_passed_list)

all_images = os.listdir(image_folder)
filtered_images = [image for image in all_images if image in passed_list]
for image in filtered_images:
    source_path = os.path.join(image_folder, image)
    output_path = os.path.join(filtered_folder, image)
    shutil.move(source_path, output_path)
    # print(f"Moved {image} to {filtered_folder}")



       