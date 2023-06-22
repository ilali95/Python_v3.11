# ✔ Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами
# нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы.

my_list = [1, 2, 3, 4, 2, 3, 5, 6, 7, 4, 8, 9, 1, 10, 10]
new_list = []
new_list_2 = []

for i in range(0, len(my_list)):
    if my_list[i]%2 == 1:
        new_list.append(i+1)
new_list_2 = list(set(my_list))

print(new_list)
print(new_list_2)