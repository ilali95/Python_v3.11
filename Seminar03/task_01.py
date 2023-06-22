# ✔ Вручную создайте список с целыми числами, которые
# повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходного списка.
# ✔ *Подготовьте два решения, короткое и длинное, которое
# не использует другие коллекции помимо списков.



original_list = [1, 2, 3, 4, 2, 3, 5, 6, 1]

# unique_list = []

# for num in original_list:
# 	if num not in unique_list:
# 		unique_list.append(num)

# print(unique_list)

new_list_2 = list(set(original_list))
print(new_list_2)