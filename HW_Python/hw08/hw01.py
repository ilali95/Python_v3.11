# Решить задачи, которые не успели решить на семинаре.
# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.
# Соберите из созданных на уроке и в рамках домашнего задания функций
# пакет для работы с файлами разных форматов.

import os
import json
import csv
import pickle


def traverse_directory(directory):
    results = []
    total_size = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            results.append({
                'path': file_path,
                'type': 'file',
                'size': file_size,
                'parent_directory': root
            })
            total_size += file_size

        for dir in dirs:
            dir_path = os.path.join(root, dir)
            dir_size = get_directory_size(dir_path)
            results.append({
                'path': dir_path,
                'type': 'directory',
                'size': dir_size,
                'parent_directory': root
            })
            total_size += dir_size

    json_file = 'results.json'
    with open(json_file, 'w') as f:
        json.dump(results, f, indent=4)

    csv_file = 'results.csv'
    with open(csv_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(
            f, fieldnames=['path', 'type', 'size', 'parent_directory'])
        writer.writeheader()
        writer.writerows(results)

    pickle_file = 'results.pickle'
    with open(pickle_file, 'wb') as f:
        pickle.dump(results, f)

    return total_size


def get_directory_size(directory):
    total_size = 0
    for path, dirs, files in os.walk(directory):
        for f in files:
            fp = os.path.join(path, f)
            total_size += os.path.getsize(fp)
    return total_size


directory = 'Python\HW_Python'
total_size = traverse_directory(directory)
print(f"Total size: {total_size} bytes")
