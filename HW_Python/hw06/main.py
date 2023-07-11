import argparse
from HW_Python.hw07.hw01 import check_date, check_year
from hw02 import eight_queens


# Создаем парсер аргументов командной строки
parser = argparse.ArgumentParser(description='Проверка даты')
parser.add_argument(
    'date', help='Дата проверки в формате ДД.ММ.ГГГГ')

# Получаем аргументы из командной строки
args = parser.parse_args()

# Получаем дату из аргумента командной строки
date_to_check = args.date

# Проверяем год
is_leap_year = check_year(date_to_check)
print(f"Високосный год: {is_leap_year}")

# Проверяем дату
is_valid_date = check_date(date_to_check)
print(f"Действительна дата: {is_valid_date}")

eight_queens()