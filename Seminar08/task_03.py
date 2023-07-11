# Задание №3
# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.

import json
import csv
import random

def json_to_csv():
    # Загрузка данных из файла JSON
    try:
        with open('users.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Файл JSON не найден.")
        return

    # Создание имени CSV-файла
    csv_filename = 'users.csv'

    # Создание списка пользователей
    users = []
    for access_level, level_data in data.items():
        for identifier, name in level_data.items():
            users.append([name, identifier, access_level])

    # Запись данных в CSV-файл
    try:
        with open(csv_filename, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Имя', 'Идентификатор', 'Уровень доступа'])
            writer.writerows(users)
    except IOError:
        print("Ошибка записи в CSV-файл.")
        return

    print(f"Данные успешно сохранены в файле {csv_filename}.")

json_to_csv()
