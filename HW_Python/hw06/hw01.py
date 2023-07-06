# 1.В модуль с проверкой даты добавьте возможность запуска в терминале
#  с передачей даты на проверку.

from datetime import datetime as dt
from calendar import isleap
import sys

__all__ = ['check_year', 'check_date']


def check_year(current_date):
    try:
        day, month, year = map(int, current_date.split('.'))
    except:
        return False
    return isleap(year)


def check_date(current_date):
    try:
        day, month, year = map(int, current_date.split('.'))
    except:
        return False
    try:
        dt(year=year, month=month, day=day)
    except:
        return False
    return True


if __name__ == '__main__':
    if len(sys.argv) > 1:
        date_to_check = sys.argv[1]
        print(check_year(date_to_check))
        print(check_date(date_to_check))
    else:
        print("Укажите дату в качестве аргумента.")
