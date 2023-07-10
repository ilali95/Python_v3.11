# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

# import random
# import string

# def generate_pseudonyms(num_pseudonyms):
#     vowels = 'aeiou'
#     pseudonyms = []
    
#     for _ in range(num_pseudonyms):
#         name_length = random.randint(4, 7)
#         name = random.choice(string.ascii_uppercase)  # Начинаем имя с заглавной буквы
        
#         for _ in range(name_length - 1):
#             name += random.choice(string.ascii_lowercase)  # Добавляем остальные буквы имени
       
#         if not any(vowel in name for vowel in vowels):  # Проверяем, что в имени есть хотя бы одна гласная
#             name += random.choice(vowels)
        
#         pseudonyms.append(name)
    
#     with open('task_02.txt', 'w') as file:
#         file.write('\n'.join(pseudonyms))

# # Пример использования
# generate_pseudonyms(10)

import random


def fill_file(name,count_lines):
    with open(name,'a',encoding='UTF-8') as f:
        for j in range (count_lines):
            length=random.randint(4,7)
            check=True
            while check:
                password=''
                for i in range(length):
                    tmp=chr(random.randint(97,122))
                    password=password+tmp
                    if tmp in ['a','o','u','i','e']:
                        check=False

            print(password.capitalize(),file=f)

fill_file('task02.txt',10)