# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче 2.
# Проверяйте различные случайные варианты и выведите 4 успешных расстановки.

from Seminars.seminar_6.DZ.package_task_2.task_2 import eight_queen
from random import randint


def perfect_position(count_successful):
    position = []
    n = 8
    count = 1
    count_iter = 0
    while count <= count_successful:
        count_iter += 1
        i = 0
        while i < n:
            x = randint(1, 8)
            y = randint(1, 8)
            if [x, y] not in position:
                position.append([x, y])
                i += 1

        if eight_queen(position):
            print(position, 'iter = ', count_iter)
            count += 1
        position.clear()


if __name__ == '__main__':
    print(eight_queen([[3, 2], [4, 1], [7, 2], [5, 8], [5, 1], [8, 4], [6, 3], [7, 6]]))
    perfect_position(4)
