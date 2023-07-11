import os

def rename_files_group(desired_name, num_digits, source_extension, target_extension, name_range):
    directory = os.getcwd()

    files = [file for file in os.listdir(directory) if file.endswith(source_extension)]

    for i, file in enumerate(files):
        original_name = file[:name_range[0]-1] + desired_name + str(i+1).zfill(num_digits) + target_extension
        original_path = os.path.join(directory, file)
        new_path = os.path.join(directory, original_name)

        os.rename(original_path, new_path)

        print(f"Переименован файл {file} в {original_name}")


rename_files_group("new_name", 3, ".txt", ".docx", [3, 6])