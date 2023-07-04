# 3. Создайте функцию генератор чисел Фибоначчи (см. Википедию)


# def fibonacci_generator():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b

# fib_gen = fibonacci_generator()

# for i in range(10):
#     print(next(fib_gen))

def fib(n):
    a, b = 0, 1
    for __ in range(n):
        yield a
        a, b = b, a + b

print(list(fib(10)))