# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.
string_tmp = 'Hello, world! Python is best'
my_dict = {key: ord(key) for key in string_tmp}

my_iter = iter(my_dict.items())
for i in range(5):
    key, value = next(my_iter)
    print(f"{key} => {value}")