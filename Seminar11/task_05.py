# Задание №5
# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

class Rectangle:
    def __init__(self, p):
        self.p = p

    def __add__(self, other):
        return Rectangle(self.p + other.p)

    def __sub__(self, other):
        return Rectangle(abs(self.p - other.p))

    def __str__(self):
        return f'{self.p}'


r1 = Rectangle(10)
r2 = Rectangle(5)
print(r1 + r2)
print(r2 - r1)
