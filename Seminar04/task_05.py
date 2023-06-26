# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.


# def calculate_premium(names, rate, bonus):
#     result = {}
#     for i in range(len(names)):
#         bonus_percentage = float(bonus[i].rstrip('%'))
#         bonus_amount = rate[i] * (bonus_percentage / 100)
#         result[names[i]] = bonus_amount
#     return result


# names = ['Alice', 'Bob', 'Charlie']
# rate = [1000, 2000, 1500]
# bonus = ['10.25%', '5.5%', '7.75%']


# result = calculate_premium(names, rate, bonus)
# print(result)

from decimal import Decimal


def extrasalary(names, salary, extrasalary):
    final_dict = {}
    for i in range(len(names)):
        final_dict[names[i]] = Decimal(salary[i]) * Decimal(extrasalary[i].replace('%', ''))
    return final_dict


list_of_names = ['Иван', 'Дмитрий', 'Мария']
list_of_salary = [100, 120, 140]
list_of_extrasalary = ['10.2%', '14.3%', '15.6%']

# print(extrasalary(list_of_names, list_of_salary, list_of_extrasalary))
for name, award in extrasalary(list_of_names, list_of_salary, list_of_extrasalary).items():
    print(f"{name} => {award}")