import os


__all__ = ['group_rename_files']


def group_rename_files(directory, desired_name, num_digits, source_extension, target_extension, name_range):
    file_counter = 1
    name_start, name_end = name_range

    for filename in os.listdir(directory):
        if filename.endswith(source_extension):
            source_path = os.path.join(directory, filename)
            original_name = filename[name_start-1:name_end]
            new_filename = original_name + desired_name + str(file_counter).zfill(num_digits) + target_extension
            new_path = os.path.join(directory, new_filename)
            os.rename(source_path, new_path)
            file_counter += 1