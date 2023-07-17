# Задание №1
# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.


import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2*math.pi * self.radius

    def area(self):
        return math.pi * self.radius**2


my_circle = Circle(5)

circumference = my_circle.circumference()
print('Длина окружности: ', circumference)

area = my_circle.area()
print('Площадь окружности:', area)