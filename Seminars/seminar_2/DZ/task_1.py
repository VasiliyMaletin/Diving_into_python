# Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

HEXADECIMAL = 16

def get_result(num: int, divider: int):
    result = ""
    while num > 0:
        temp = num % divider
        if num == 10:
            temp = 'a'
        elif num == 11:
            temp = 'b'
        elif num == 12:
            temp = 'c'
        elif num == 13:
            temp = 'd'
        elif num == 14:
            temp = 'e'
        elif num == 15:
            temp = 'f'

        result += str(temp)
        num //= divider
    return result[::-1]

while True:
    try:
        num = int(input("Введите целое число: "))
        break
    except Exception as err:
        print(err)
        print("Вы ввели не верное значение, попробуйте ещё раз\n")

print(f'{hex(num)} == 0x{get_result(num, HEXADECIMAL)}')
