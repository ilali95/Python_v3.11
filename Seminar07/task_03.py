# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.


def func(name1, name2, name3):
    with open(name1, encoding='UTF-8') as f1, \
            open(name2, encoding='UTF-8') as f2, \
            open(name3, 'w', encoding='UTF-8') as f3:
        text1 = f1.readlines()
        text2 = f2.readlines()
        max_length = max(len(text1), len(text2))
        i1 = 0
        i2 = 0
        for i in range(max_length):
            a, b = text1[i1].split('|')
            a = int(a)
            b = float(b)
            c = a * b
            name_tmp = text2[i2]
            if c < 0:
                print(f'{name_tmp.strip().lower()} {abs(c)}', file=f3)
            else:
                print(f'{name_tmp.strip().upper()} {round(c)}', file=f3)
            i1 += 1
            i2 += 1
            if i1 >= len(text1):
                i1 = 0
            if i2 >= len(text2):
                i2 = 0


func('task01.txt', 'task02.txt', 'task03.txt')
