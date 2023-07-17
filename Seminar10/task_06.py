# Задание №6
# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс
# Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class Horse(Animal):
    def __init__(self, name, age, power):
        super().__init__(name, age)
        self.power = power

    def get_power(self):
        return self.power


class Fish(Animal):
    def __init__(self, name, age, tail_length):
        super().__init__(name, age)
        self.tail_length = tail_length

    def get_tail_length(self):
        return self.tail_length


class Bird(Animal):
    def __init__(self, name, age, fly_speed):
        super().__init__(name, age)
        self.fly_speed = fly_speed

    def get_fly_speed(self):
        return self.fly_speed


h1 = Horse('Spirit', 5, 60)
print(h1.get_name())
print(h1.get_age())
print(h1.get_power())

p1 = Fish('Saroka', 2, 100)
print(p1.get_name())
print(p1.get_age())
print(p1.get_tail_length())
