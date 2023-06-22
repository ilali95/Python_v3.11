# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

my_list = [1, 2, 3, 4, 2, 3, 5, 6, 7, 4, 8, 9, 1, 10, 10]

unique_list = []
for item in my_list:
    if my_list.count(item) == 2:
        unique_list.append(item)

print(unique_list)