# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.


def eight_queen(position: list[list[int]]) -> bool:
    n = 8
    x = []
    y = []

    for i in range(n):
        x.append(position[i][0])
        y.append(position[i][1])
    flag = True
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                flag = False
            break
    if flag:
        return True
    else:
        return False


if __name__ == '__main__':
    print(eight_queen([[3, 2], [4, 1], [7, 2], [5, 8], [5, 1], [8, 4], [6, 3], [7, 6]]))
