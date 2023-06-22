# Создайте вручную кортеж содержащий элементы разных типов.
# Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

data = (1, 1.56, '123', 4, 53.78, '342', [1, 2, 3], [1, 7, 9])
new_dict = {}

for i in data:
    if type(i).__name__ not in new_dict.keys():
        new_dict[type(i).__name__] = [i]
    else:
        new_dict[type(i).__name__].append(i)

print(new_dict)