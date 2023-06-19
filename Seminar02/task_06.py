# Задание №6
# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег


bank = 0
count = 0


def add_bank(cash):
    global bank, count
    bank += cash
    count += 1
    print('Ваш баланс: ', bank)


def take_bank(cash):
    global bank, count
    if cash < bank:
        if (cash / 100 * 1.5) < 30:
            bank -= 30
        elif 30 < (cash / 100 * 1.5) < 600:
            bank -= cash / 100 * 1.5
        elif (cash / 100 * 1.5) > 600:
            bank -= 600
    else:
        print('Недостаточно средств!')
    bank -= cash
    count += 1
    print('Ваш баланс: ', bank)


def exit_bank():
    print('Не забудьте забрать карту.')
    exit()


def check_bank():
    while True:
        cash = int(input('Введите сумму кратную 50 '))
        if cash % 50 == 0:
            return cash


while True:
    action = input('1 - снять\n2 - пополнить\n3 - выйти\n')
    if bank >= 5_000_000:
        bank *= 0.9
    match action:
        case '1':
            take_bank(check_bank())

        case '2':
            add_bank(check_bank())

        case '3':
            exit_bank()

    if count == 3:
        bank *= 1.03
        count = 0