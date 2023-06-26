# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

# def sorted_unique_unicode(text):
#     unique_unicode = sorted(set(ord(char) for char in text), reverse=True)
#     return unique_unicode

# text = input("В ведите пример строки: ")
# result = sorted_unique_unicode(text)
# print(result)


def unicode_list(tmp):
    chr_list = []
    set_of_chr = set(tmp)
    for i in set_of_chr:
        chr_list.append(ord(i))
    return sorted(chr_list, reverse=True)


data = input('Введите строку: ')

print(unicode_list(data))