# Добавь логирование ошибок и полезной
# информации. Также реализуйте возможность запуска из
# командной строки с передачей параметров.

import sys
import logging
import argparse
from collections import deque as deq
import unittest

class TestFactorial(unittest.TestCase):

    def test_factorial_calculation(self):
        f = Factorial(2)
        self.assertEqual(str(f(5)), '{5: 120}')
        self.assertEqual(str(f(7)), '{5: 120, 7: 5040}')
        self.assertEqual(str(f(3)), '{7: 5040, 3: 6}')
        self.assertEqual(str(f(4)), '{3: 6, 4: 24}')
        self.assertEqual(str(f(2)), '{4: 24, 2: 2}')

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

def main():
    parser = argparse.ArgumentParser(description="Вычислять и отслеживать факториалы.")
    parser.add_argument("values", nargs="+", type=int, help="Значения для расчета факториала")
    parser.add_argument("-k", "--history-size", type=int, default=2, help="Размер истории для отслеживания")
    args = parser.parse_args()

    logging.basicConfig(filename="factorial.log", level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")

    f = Factorial(args.history_size)
    try:
        for value in args.values:
            result = f(value)
            logging.info(f"Factorial for {value}: {result}")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}", exc_info=True)

if __name__ == "__main__":
    main()
    unittest.main()