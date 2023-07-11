# Задание №2
# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.

import json


def add_user():
    # Загрузка данных из файла (если есть)
    try:
        with open('users.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    while True:
        name = input("Введите имя пользователя: ")
        identifier = input("Введите личный идентификатор: ")
        access_level = input("Введите уровень доступа (от 1 до 7): ")

        # Проверка уникальности идентификатора
        unique_identifier = False
        while not unique_identifier:
            if identifier in data.values():
                print("Идентификатор уже используется. Попробуйте другой.")
                identifier = input("Введите личный идентификатор: ")
            else:
                unique_identifier = True

        # Добавление новой информации в словарь
        if access_level not in data:
            data[access_level] = {}

        data[access_level][identifier] = name

        # Запись данных в файл
        with open('users.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False)

        print("Пользователь успешно добавлен.")

        choice = input("Продолжить добавление пользователей? (y/n): ")
        if choice.lower() != 'y':
            break


add_user()
