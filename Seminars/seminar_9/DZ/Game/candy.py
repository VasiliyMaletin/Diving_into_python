# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# Делаем игру против бота
# а) Подумайте как наделить бота ""интеллектом""

from random import choice, randint

print('Игра "2021 конфета"')
print()
print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▄░░░░░░░")
print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████▄░░░░░░")
print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█████▄░░░░░")
print("░░░░░░░░░░░░░░░░░░▄▄▄▄▄░░░░▄███████▄░░░░")
print("░░░░░░░░░░░░░░▄██████████████████████▄▄░")
print("░░░░░░░░░░░▄███████████░░▀▀█████████████")
print("░░░░░░░░░░▄█▀███████████░░░░█████▀▀▀▀░░░")
print("░░░░░░░░░▄█▀░████████████░░░░██░░░░░░░░░")
print("░░░░░░░░░██░░█████████████░░░░██░░░░░░░░")
print("░░░░░░░░░██░░▀████████████░░░░██░░░░░░░░")
print("░░░░░░░░░██░░░█████████████░░██░░░░░░░░░")
print("░░░░░░░▄▄██▄░░░████████████░▄█▀░░░░░░░░░")
print("████████████▄░░░█████████████▀░░░░░░░░░░")
print("▀██████████████▄▄▀█████████▀░░░░░░░░░░░░")
print("░░░▀█████████▀▀▀▀█████▀▀▀░░░░░░░░░░░░░░░")
print("░░░░░███████░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
print("░░░░░▀█████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
print("░░░░░░░▀██▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
print("На столе лежит 2021 конфета.\n\
Играют два игрока делая ход друг после друга.\n\
За один ход можно забрать не более чем 28 конфет.\n\
Все конфеты оппонента достаются сделавшему последний ход.")
print()
input("Нажмите Enter для продолжения")
print()
print("Добро пожаловать в игру!!!")

def lot_player(first_player, second_player):
    input("Нажмите Enter для определения кто ходит первым.")
    lot = [first_player, second_player]
    first_move = choice(lot)
    return first_move

def candies_the_ending(candies):
    amount = candies
    while amount > 20:
        amount %= 10
    if amount == 0 or 4 < amount < 21:
        the_ending = "конфет"
    elif amount % 10 == 1:
        the_ending = "конфета"
    elif amount % 10 < 5:
        the_ending = "конфеты"
    return the_ending

def picks_up_candies(picks_up):
    amount = picks_up
    while amount > 20:
        amount %= 10
    if 4 < amount < 21:
        the_ending = "конфет"
    elif amount % 10 == 1:
        the_ending = "конфету"
    elif amount % 10 < 5:
        the_ending = "конфеты"
    return the_ending

def computer_hard(candies):
    picks_up = candies % 29
    if picks_up == 0:
        picks_up += 1
    return picks_up

def computer_easy():
    picks_up = randint(1, 29)
    return picks_up

mode = int(input("Выберите режим игры: 1 - Против Компьютера,\
 2 - Против другого игрока\n"))
candies = 2021
if mode == 1:
    level = int(input("Выберите уровень сложности: 1 - Тяжёлый,\
 2 - Лёгкий\n"))
    print()
    player = input("Введите Ваше имя: ")
    computer = "Стив"
    print(f"Приятно познакомиться, {player}. Меня зовут Стив.")
    print()
    move = lot_player(player, computer)
    print(f"Первым ходит игрок {move}")
    print()
    while candies > 0:
        if move == computer:
            if level == 1:
                picks_up = computer_hard(candies)
            elif level == 2:
                picks_up = computer_easy()
            print(f"На столе {candies} {candies_the_ending(candies)}. {move},\
 забирает {picks_up} {picks_up_candies(picks_up)}.")
            candies -= picks_up
            if candies == 0:
                break
            move = player
        print(f"На столе {candies} {candies_the_ending(candies)}. {move},\
 сколько конфет будешь брать?")
        number = int(input())
        if 0 < number < 29 and number <= candies:
            candies -= number
            if candies == 0:
                break
            if move == player:
                move = computer
        else: print("нельзя взять столько конфет!!!")
        continue
    print(f"Поздравляю! В этот раз победитель {move}! {move},\
 забирает все конфеты!")
elif mode == 2:
    player_1 = input("Введите имя первого игрока: ")
    player_2 = input("Введите имя второго игрока: ")
    print("Приятно познакомиться, меня зовут Стив.")
    print()
    move = lot_player(player_1, player_2)
    print(f"Первым ходит игрок {move}")
    print()
    while candies > 0:
        print(f"На столе {candies} {candies_the_ending(candies)}. {move},\
 сколько конфет будешь брать?")
        number = int(input())
        if 0 < number < 29 and number <= candies:
            candies -= number
            if candies == 0:
                break
            if move == player_1:
                move = player_2
            elif move == player_2:
                move = player_1
        else: print("нельзя взять столько конфет!!!")
        continue
    print(f"Поздравляю! В этот раз победитель {move}! {move},\
 забирает все конфеты!")
