# ✔ Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку.


string_tmp = 'Hello, world! Python is best'
my_dict = {key: ord(key) for key in string_tmp}
# my_dict = {}
# for ch in string_tmp:
#     my_dict[ch]=ord(ch)


for expression, expr_hash in my_dict.items():
    print(f"{expression} => {expr_hash}")
