# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на
# единицу и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.


min_limit = 0
max_limit = 100000
count = 0
flag = True

while flag == True:
    try:
        num = int(input('Введите число: '))

        if  min_limit < num < max_limit:
            for i in range(2, num // 2 + 1):
                if (num % i == 0):
                    count += 1
            if (count <= 0):
                print("Число простое")
            else:
                print("Число составное")
            flag = False
        else:
            print('Число не входит в допустимый диапозон!')
    except ValueError:
        print('Нужно вводить число!')
