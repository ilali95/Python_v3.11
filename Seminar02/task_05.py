# Задание №5
# ✔ Напишите программу, которая решает
# квадратные уравнения даже если
# дискриминант отрицательный.
# ✔ Используйте комплексные числа
# для извлечения квадратного корня.

import cmath

# a = float(input("Введите коэффициент a: "))
# b = float(input("Введите коэффициент b: "))
# c = float(input("Введите коэффициент c: "))

# d = b**2 - 4*a*c

# if d >= 0:
#     x1 = (-b + cmath.sqrt(d)) / (2*a)
#     x2 = (-b - cmath.sqrt(d)) / (2*a)
#     print("Корни уравнения:", x1, x2)
# else:
#     x1 = (-b + cmath.sqrt(-d)) / (2*a)
#     x2 = (-b - cmath.sqrt(-d)) / (2*a)
#     print("Корни уравнения:", x1, x2)
    
a = float(input('Введите коэффициент a: '))
b = float(input('Введите коэффициент b: '))
c = float(input('Введите коэффициент c: '))

d = b**2-4 * a * c

if d > 0:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print('Корни уравнения,', x1, x2)
elif d == 0:
    print('Корень уравнения =', -b / (2 * a))
else:
    d = complex(b**2-4 * a * c)
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print('комплексные корни уравнения,', x1, x2)
