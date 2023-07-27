# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать "больше" или "меньше" после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

find_num = randint(0, 1000)
count = 10
flag = True

while flag == True:
    try:
        while count > 0:
            num = int(input('Введите число от 0 до 1000, чтобы угадать загаданное: '))

            if 0 <= num < 1000:
                if find_num > num:
                    print('Загаданное число больше')
                    count -= 1
                    print(f'Осталось попыток: {count}')
                elif find_num < num:
                    print('Загаданное число меньше')
                    count -= 1
                    print(f'Осталось попыток: {count}')
                else:
                    print('Вы угадали!')
                    count -= 1
                    print(f'Осталось попыток: {count}')
                    flag = False
                    break
            else:
                print('Ваше число не входит диапозон загаданного!')
                count -= 1
                print(f'Осталось попыток: {count}')
        else:
            print('Ваши попытки закончились')
            print(f'Загаданное число: {find_num}')
            flag = False

    except ValueError:
        print('Нужно вводить число!')