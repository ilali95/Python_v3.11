# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.

def two_num_unicode (input_string):
	num1, num2 = map(int, input_string.split())

	start_num = min(num1, num2)
	end_num = max(num1, num2)

	unicode_dict = {}

	for num in range(start_num, end_num + 1):
		unicode_dict[chr(num)] = num

	return unicode_dict

input_str = input('В ведите значение: ')
dict_new = two_num_unicode(input_str)
print(dict_new)