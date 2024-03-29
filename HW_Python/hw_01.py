# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c — стороны предполагаемого треугольника. 
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
# с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

# a = int(input('Введите длину стороны a: '))
# b = int(input('Введите длину стороны b: '))
# c = int(input('Введите длину стороны c: '))

# if a+b < c or a+c < b or b+c < a:
# 	print('Треугольник не существует.')

# elif a==b==c:
# 	print('Равносторонний триугольник.')

# elif a==b or a==c or b==c:
# 	print('Равнобедренный треугольник.')

# else:
# 	print('Разносторонний треугольник.')



# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)
from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 100000
MAX_TRIES = 10

num = randint(LOWER_LIMIT, UPPER_LIMIT)

tries = 0
guess = None

while tries < MAX_TRIES and guess != num:
    guess = int(input(f'Введите число от {LOWER_LIMIT} до {UPPER_LIMIT}: '))
    if guess < num:
        print('Загадонное число больше')
    elif guess>num:
        print('Загадонное число меньше')
    tries =+ 1
if guess == num:
    print(f'Поздравляем вы угодали число! Загаданное число: {num}')
else:
    print(f'К сожалению, вы не угадали число. Загаданное число: {num}')



# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для проверки: 
# «Число является простым, если делится нацело только на единицуи на себя». 
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.



# if num < LOWER_LIMIT or num > UPPER_LIMIT:
# 	print('Введите число от', LOWER_LIMIT,'до', UPPER_LIMIT)

# else:
# 	is_prime = True
# 	for i in range(2, int(num ** 0.5)+1):
# 		if num % i == 0:
# 			is_prime = False
# 			break

# 	if is_prime:
# 		print('Число', num, 'является простым')
# 	else:
# 		print('Число', num, 'является составным')