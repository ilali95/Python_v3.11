num_stars = int(input("Введите количество звездочек в пирамиды: "))

for i in range(num_stars):
    print(" " * (num_stars - i - 1) + "*" * (2 * i + 1))
