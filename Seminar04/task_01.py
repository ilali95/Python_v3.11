# ✔ Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.

def print_words(test):
    words= test.split()
    sorted_words = sorted(words, key=lambda word: (len(word), word))
    max_lenght = len(sorted_words[-1])
    for i, word in enumerate(sorted_words, start=1):
        spaces = max_lenght - len(word) + 1
        print(f"{i:2}. {' ' * spaces}{word}")

text = input('В ведите пример строки: ')
print_words(text)