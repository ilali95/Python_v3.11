# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.


def calculate_sum(numbers, index1, index2):
    start_index = min(index1, index2)
    end_index = max(index1, index2)

    if start_index < 0:
        start_index = 0
    if end_index >= len(numbers):
        end_index = len(numbers) - 1

    total_sum = sum(numbers[start_index:end_index+1])

    return total_sum

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index1 = 2
index2 = 6
result = calculate_sum(numbers, index1, index2)
print(result)
