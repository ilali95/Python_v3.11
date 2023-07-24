# Задание №3
# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1.

class FactorialGenerator:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            self.start = 1
            self.stop = start + 1
        else:
            self.start = start
            self.stop = stop + 1
        self.step = step
        self.current = self.start

    def factorial(self, n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        result = self.factorial(self.current)
        self.current += self.step
        return result


# Пример использования
generator = FactorialGenerator(1, 5, 2)
for factorial in generator:
    print(factorial)
