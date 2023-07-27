# Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

from datetime import date

bank = 0
count = 0
percent_take = 0.015
percent_add = 0.03
percent_tax = 0.01

def add_bank(cash: float) -> None:
    global bank
    global count
    bank += cash
    count += 1
    if count % 3 == 0:
        bank = bank + percent_add * bank
        print("Начислены проценты в размере: ", percent_add * bank)

def take_bank(cash: float) -> None:
    global bank
    global count
    bank -= cash
    count += 1

    if cash * percent_take < 30:
        bank -= 30
        print("Комиссия за снятие: ", 30)
    elif cash * percent_take > 600:
        bank -= 600
        print("Комиссия за снятие: ", 600)
    else:
        bank -= cash * percent_take
        print("Комиссия за снятие: ", cash * percent_take)
    if count % 3 == 0:
        bank = bank + percent_add * bank
        print("Начислены проценты в размере: ", percent_add * bank)


def exit_bank():
    print("Будем рады видеть Вас снова!\n")
    exit()

def check_bank() -> int:
    while True:
        cash = int(input("Введите сумму кратную 50: "))
        if cash % 50 == 0:
            return cash

list_operation = []

while True:
    action = input("\nДобро пожаловать в меню!\n1 - Внести\n2 - Снять\n3 - Баланс\
    \n4 - Историю операций\n5 - Выход\nВвведите номер операции: ")
    match action:
        case '1':
            cash = check_bank()
            add_bank(cash)
            if bank > 5_000_000:
                bank = bank - bank * percent_tax
                print("Списан налог на богатство: ", bank * percent_tax)
            print("Баланс: ", bank)

            list_operation.append([str(date.today()), cash])
        case '2':
            if bank > 5_000_000:
                bank = bank - bank * percent_tax
                print("Списан налог на богатство: ", bank * percent_tax)
            cash = check_bank()
            if cash < bank:
                take_bank(cash)

                list_operation.append([str(date.today()), -1 * cash])
            else:
                print("Недостаточно средств\n")
            if bank > 5_000_000:
                bank = bank - bank * percent_tax
                print("Списан налог на богатство: ", bank * percent_tax)
            print("Баланс: ", bank)
        case '3':
            print("Баланс: ", bank)
        case '4':
            print(list_operation)
        case '5':
            exit_bank()
