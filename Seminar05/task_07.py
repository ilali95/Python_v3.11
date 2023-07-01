# Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

def simple_dif(tmp):
    for i in range(2, tmp):
        check = False

        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                check = True
                break
        if not check:
            yield i


dig = int(input('Введите целое число: '))
func = simple_dif(dig)
for k in range(2, 10):
    print(next(func))
