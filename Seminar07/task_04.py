# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.


import random


def file_extensions(extensions, min_length=6, max_length=30, min_bytes=256, max_bytes=4096):
    for extension in extensions:
        for i in range(extensions[extension]):
            name = ''
            for j in range(random.randint(min_length, max_length)):
                tmp = chr(random.randint(97, 122))
                name = name + tmp
            with open(f'{name}.{extension}', 'w', encoding='UTF-8') as f:
                for k in range(random.randint(min_bytes, max_bytes)):
                   print(chr(random.randint(97, 122)), file=f, end='')


file_extensions({'jpg':1, 'pdf':2})