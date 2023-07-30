# Задание №2
# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.

def get_analog(dictionary, key, default_value=None):
    try:
        return dictionary[key]
    except KeyError:
        return default_value


if __name__ == '__main__':
	my_dict = {'apple': 1, 'banana': 2, 'orange': 3}

	# Попробуем получить значение для существующего ключа
	result1 = get_analog(my_dict, 'banana', 'Not found')
	print(result1)  # Вывод: 2

	# Попробуем получить значение для несуществующего ключа
	result2 = get_analog(my_dict, 'grape', 'Not found')
	print(result2)  # Вывод: 'Not found'

	# Попробуем получить значение для несуществующего ключа без задания дефолтного значения
	result3 = get_analog(my_dict, 'grape')
	print(result3)  # Вывод: None
