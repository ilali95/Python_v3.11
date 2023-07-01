# ✔ Напишите программу, которая выводит
# на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа
# должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение

some_generator1 = (("FizzBuzz" for x in range(1, 101) if x % 3 == 0))
for i in range (51):
    print(next(some_generator1))


some_generator2 = (
    ("FizzBuzz" if x % 3 == 0 and x % 5 == 0 else "Fizz" if x % 3 == 0 else "Buzz" if x % 5 == 0 else x) for x in
    range(1, 101))
for i in range (51):
    print(next(some_generator2))

# for i in range(1, 101):
#     if (i % 3 == 0) and (i % 5 == 0):
#         print(f'{i} = FizzBuzz')
#     elif (i % 3 == 0):
#         print(f'{i} = Fizz')
#     else:
#         print(i)

