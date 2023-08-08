# Напишите к ним тесты.
# 2-5 тестов на задачу в трёх вариантах:
# ○ doctest,
# ○ unittest,
# ○ pytest.

from collections import deque as deq
import unittest
import pytest

class TestFactorial:

    def test_factorial_calculation(self):
        f = Factorial(2)
        assert str(f(5)) == '{5: 120}'
        assert str(f(7)) == '{5: 120, 7: 5040}'
        assert str(f(3)) == '{7: 5040, 3: 6}'
        assert str(f(4)) == '{3: 6, 4: 24}'
        assert str(f(2)) == '{4: 24, 2: 2}'


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

class Factorial:
    """
    Класс для вычисления факториалов и отслеживания максимальных факториалов.

    >>> f = Factorial(2)
    >>> str(f(5))
    '{5: 120}'
    >>> str(f(7))
    '{5: 120, 7: 5040}'
    >>> str(f(3))
    '{7: 5040, 3: 6}'
    >>> str(f(4))
    '{3: 6, 4: 24}'
    >>> str(f(2))
    '{4: 24, 2: 2}'
    """


if __name__ == '__main__':
    unittest.main()
    pytest.main([__file__])


def __init__(self, k):
    f = Factorial(2)
    print(f(5))
    print(f(7))
    print(f(3))
    print(f(4))
    print(f(2))