# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.

def list_sort(tmp_list):
    for i in range(len(tmp_list)):
        for j in range(len(tmp_list) - 1):
            if tmp_list[j] > tmp_list[j + 1]:
                tmp_list[j], tmp_list[j + 1] = tmp_list[j + 1], tmp_list[j]
    return tmp_list


list_of_numbers = [1, 4, 5, 12, 2, 6, 7, 8]

print(list_sort(list_of_numbers))