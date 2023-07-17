# Задание №3
# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.

class Person:
    def __init__(self, name, age, heighd):
        self.name = name
        self.__age = age
        self.height = heighd

    def get_name(self):
        return self.name

    def get_age(self):
        return self.__age

    def get_heighd(self):
        return self.height

    def birthday(self):
        self.__age += 1
        return self.get_age()


p1 = Person('Иванов Иванов Иванович', 44, 26)

print(p1.get_name())
print(p1.get_age())
print(p1.height())
print(p1.birthday())
