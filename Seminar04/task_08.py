def balance(tmp_dict):
    final_balance = []
    for i in tmp_dict.values():
        final_balance.append(sum(i))
    return all([i if i > 0 else 0 for i in final_balance])


old_dict = {'Вода': [5000, 1000, -3000],
            'Нож': [2000, -1000, -7000],
            }
print(balance(old_dict))