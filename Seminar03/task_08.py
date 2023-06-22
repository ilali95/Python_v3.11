# ✔ Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.
old_dict = {'Ваня': ('Нож', 'Рюкзак', 'Палатка'),
            'Игорь': ('Котелок', 'Рюкзак', 'Пенка'),
            'Андрей': ('Палатка', 'Спички', 'Рюкзак'),
            }
list_tuple = []
items = {}
items_2 = {}
uni_items = []
all_name = set(old_dict.keys())

for item in old_dict.values():
    list_tuple.append(set(item))

print(list_tuple)

inter_set = list_tuple[0]

for i in range(1, len(list_tuple)):
    inter_set = list_tuple[i] & inter_set

print(inter_set)

for i in list_tuple:
    for item in i:
        if item not in items:
            items[item] = 1
        else:
            items[item] += 1

for i in items:
    if items[i] == 1:
        uni_items.append(i)

print(uni_items)

for name in old_dict:
    for item in old_dict[name]:
        if item not in items_2:
            items_2[item] = [1, {name}]
        else:
            items_2[item][0] += 1
            items_2[item][1].add(name)

for item in items_2:
    if items_2[item][0] == len(old_dict) - 1:
        print(item)
        print(all_name - items_2[item][1])