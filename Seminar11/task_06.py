# Задание №6
# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

class Rectangle:
    def __init__(self, p):
        self.p = p

    def __add__(self, other):
        return Rectangle(self.p + other.p)

    def __sub__(self, other):
        return Rectangle(abs(self.p - other.p))

    def __str__(self):
        return f'{self.p}'

    def __eq__(self, other):
        return self.p == other.p

    def __ne__(self, other):
        return self.p != other.p

    def __lt__(self, other):
        return self.p < other.p

    def __le__(self, other):
        return self.p <= other.p

    def __gt__(self, other):
        return self.p > other.p

    def __ge__(self, other):
        return self.p >= other.p


rect1 = Rectangle(4)
rect2 = Rectangle(5)
rect3 = Rectangle(4)

print(rect1 == rect2)
print(rect1 != rect2)
print(rect1 < rect2)
print(rect1 <= rect3)
print(rect1 > rect2)
print(rect1 >= rect3)
