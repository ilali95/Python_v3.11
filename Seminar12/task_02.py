# Задание №2
# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.

import json
from collections import deque as deq


class Factorial:
    def __init__(self, k):
        self.max_k = deq(maxlen=k)
        self.values = deq(maxlen=k)

    def __call__(self, value):
        result = 1
        for i in range(1, value + 1):
            result *= i
        self.max_k.append(result)
        self.values.append(value)
        return self

    def __str__(self):
        return str({i: j for i, j in zip(self.values, self.max_k)})


class FactorialContextManager:
    def __init__(self, factorial_instance, filename):
        self.factorial_instance = factorial_instance
        self.filename = filename

    def __enter__(self):
        return self.factorial_instance

    def __exit__(self, exc_type, exc_value, traceback):
        data = {str(k): v for k, v in zip(
            self.factorial_instance.values, self.factorial_instance.max_k)}
        with open(self.filename, 'w') as f:
            json.dump(data, f)


if __name__ == "__main__":
    f = Factorial(2)

    with FactorialContextManager(f, 'factorial_values.json'):
        print(f(5))
        print(f(7))
        print(f(3))
        print(f(4))
        print(f(2))