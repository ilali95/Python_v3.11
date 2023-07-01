# ✔ Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите
# числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку.


from random import random as rnd

generator = (i for i in range(101) if (i % 2 == 0) and (sum(map(int, str(i))) != 8))
for i in range (51):
    print(next(generator))