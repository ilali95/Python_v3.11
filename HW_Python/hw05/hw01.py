# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов:
# путь, имя файла, расширение файла.

def file_info(file_path):
    path, file_name = file_path.rsplit('/', 1)
    file_name, file_extension = file_name.rsplit('.', 1)
    return path, file_name, file_extension


file_path = input('Введите строку: ')
path, file_name, file_extension = file_info(file_path)
result = (path, file_name, file_extension)

print('\n', result, '\n')
print(f'Путь: {path}, Имя файла: {file_name}, Расширение файла: {file_extension}')

# print('Путь:', path)
# print('Имя файла:', file_name)
# print('Расширение файла:', file_extension)
