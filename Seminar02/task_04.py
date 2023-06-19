# Задание №4
# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.


import math
from decimal import *
getcontext().prec = 42

radius: float | None = None
while True:
    try:
        radius = int(
            input("Введите диаметр круга не более 1000: ")) / 2
        if radius * 2 > 1000 or radius * 2 <= 0:
            raise Exception("Не верный диаметр")
        break
    except Exception as err:
        print(err)
        print("Вы ввели не верное значение, попробуйте ещё раз\n")

print(f"Площадь круга равна: {Decimal(math.pi*radius**2)}")
print(
    f"Радиус окружности равен: {Decimal(2*math.pi*radius)}")
