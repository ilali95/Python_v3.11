# Задание №6
# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину
# на дескриптор с валидацией размера.

class Range:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def validate(self, value):
        if value <= 0:
            raise ValueError('Значение должно быть больше нуля')

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.name, value)


class Rectangle:
    a = Range()
    b = Range()

    def __init__(self, a, b=None):
        self.a = a
        self.b = a if not b else b

    def get_length(self):
        return 2 * (self.a + self.b)

    def get_area(self):
        return self.a * self.b

r = Rectangle(10, 5)
print(r.a)