# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.

import random


def create_guessing_game(answer):
    def guessing_game(attempts):

        for _ in range(attempts):
            guess = int(input('Введите число: '))
            if guess == answer:
                print('Вы угодали число!')
                return
            elif guess < answer:
                print('Число больше!')
            else:
                print('Число меньше!')
        print('Попытки закончились!')

    return guessing_game


num1 = random.randint(1, 100)
num2 = random.randint(1, 10)

create_guessing_game(num1)(num2)
