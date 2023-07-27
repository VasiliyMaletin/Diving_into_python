# Создайте программу для игры в "Крестики-нолики".

size_board = list(range(1, 10))

def board_creation(size_board):
    print("╔═══╦═══╦═══╗")
    count = 3
    for i in range(3):
        print(f"║ {size_board[0 + i * 3]} ║ {size_board[1 + i * 3]} ║\
 {size_board[2 + i * 3]} ║")
        if count > 1:
            print("╠═══╬═══╬═══╣")
        count -= 1
        if count < 1:
            print("╚═══╩═══╩═══╝")

def player_turn(player_symbol):
    valid = False
    while not valid:
        cell_number = input(f"Выберите куда ставим {player_symbol}?\n")
        try:
            cell_number = int(cell_number)
        except:
            print ("Нужно вводить число!")
            continue
        if cell_number > 0 and cell_number < 10:
            if (str(size_board[cell_number - 1]) not in "XO"):
                size_board[cell_number - 1] = player_symbol
                valid = True 
            else:
                print ("Клетка уже занята!")
        else:
            print ("Нужно вводить число соответствующее выбранной\
 свободной клетке.")

def check_win(size_board):
    winning_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                            (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in winning_combinations:
        if size_board[i[0]] == size_board[i[1]] == size_board[i[2]]:
            return size_board[i[0]]
    return False

def main(size_board):
    count = 0
    win = False
    while not win:
        board_creation(size_board)
        if count % 2 == 0:
            player_turn("X")
        else:
            player_turn("O")
        count += 1
        if count > 4:
            temp = check_win(size_board)
            if temp:
                print (temp, "Выиграл!")
                win = True
                break
        if count == 9:
            print ("Ничья!")
            break
    board_creation(size_board)

main(size_board)
