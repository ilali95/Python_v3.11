from hw01 import quadratic_roots
from hw02 import generate_csv
from hw03 import solve_quadratic_equation_with_csv
from hw04 import save_to_json

# Проверка функции quadratic_roots
roots = quadratic_roots(1, -4, 3)
print(roots)

# Проверка функции generate_csv
generate_csv('random_numbers.csv', 100)

# Проверка декорированной функции с использованием декоратора solve_quadratic_equation_with_csv
@solve_quadratic_equation_with_csv
def solve_quadratic(a, b, c):
    return quadratic_roots(a, b, c)

solve_quadratic('random_numbers.csv')

# Проверка декорированной функции с использованием декоратора save_to_json
@save_to_json
def multiply(a, b):
    return a * b

result = multiply(2, 3)
print(result)
