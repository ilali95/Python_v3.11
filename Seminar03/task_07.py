# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают
# или не совпадают в ваших решениях.


data = input('Введите строку: ')
new_dict = {}
new_dict_2 = {}

for item in data:
    if item == ' ':
        continue

    if item not in new_dict.keys():
        new_dict[item] = 1
    else:
        new_dict[item] += 1

for item in data:
    if item == ' ':
        continue

    if item not in new_dict_2.keys():
        new_dict_2[item] = data.count(item)
    else:
        continue

print(new_dict)
print(new_dict_2)