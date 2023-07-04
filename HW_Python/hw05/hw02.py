# Напишите однострочный генератор словаря, который принимает на вход три списка 
# одинаковой длины: имена str, ставка int, премия str с 
# указанием процентов вида «10.25%». В результате получаем словарь с 
# именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается

def generate_dictionary(names, rates, bonuses):
    return {name: round(rate * float(bonus.rstrip('%')) / 100, 2) for name, rate, bonus in zip(names, rates, bonuses)}

names = ["Алиса", "Боб", "Вася"]
rates = [100, 200, 150]
bonuses = ["10.25%", "5.5%", "8.75%"]

result = generate_dictionary(names, rates, bonuses)
print(result)
