# Задание №3
# ✔ Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего
# результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода
# в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно

BINARY = 2
OCTAL = 8


def get_result(num: int, divider: int):
    result = ""
    while num > 0:
        result = str(num % divider) + result
        num //= divider
    return result


num = None
while True:
    try:
        num = int(input("Введите целое число: "))
        break
    except Exception as err:
        print(err)
        print("Вы ввели не верное значение, попробуйте ещё раз\n")

print(f"{bin(num)} == {get_result(num, BINARY)}")
print(f"{oct(num)} == {get_result(num, OCTAL)}")