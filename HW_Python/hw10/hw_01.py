# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.


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


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, name, age, *args):
        if animal_type == "Horse":
            return Horse(name, age, *args)
        elif animal_type == "Fish":
            return Fish(name, age, *args)
        elif animal_type == "Bird":
            return Bird(name, age, *args)
        else:
            raise ValueError("Недопустимый тип животного")



h1 = AnimalFactory.create_animal('Horse', 'Spirit', 5, 60)
print(h1.get_name())
print(h1.get_age())
print(h1.get_power())

p1 = AnimalFactory.create_animal('Fish', 'Saroka', 2, 100)
print(p1.get_name())
print(p1.get_age())
print(p1.get_tail_length())

a1 = AnimalFactory.create_animal('Bird', 'Bird', 3, 12)
print(a1.get_name())
print(a1.get_age())
print(a1.get_fly_speed())
