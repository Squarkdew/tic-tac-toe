def print_board(board):
    print("  0 1 2")
    for i, row in enumerate(board):
        print(i, " ".join(row))

def check_winner(board, player):
    return any(
        all(board[i][j] == player for j in range(3)) or  
        all(board[j][i] == player for j in range(3)) for i in range(3) 
    ) or all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3))

def is_draw(board):
    return all(cell != "-" for row in board for cell in row)

def get_valid_move(board):
    while True:
        move = input("Введите строку и столбец (0 2 через пробел): ").strip()
        if move.count(" ") == 1 and all(x.isdigit() for x in move.split()):
            row, col = map(int, move.split())
            if 0 <= row < 3 and 0 <= col < 3:
                if board[row][col] == "-":
                    return row, col
                else:
                    print("Эта клетка уже занята. Попробуйте снова.")
            else:
                print("Числа должны быть от 0 до 2.")
        else:
            print("Некорректный ввод. Введите два числа через пробел.")

def tic_tac_toe():
    board = [["-" for _ in range(3)] for _ in range(3)]
    players = ["x", "o"]
    turn = 0

    while True:
        print_board(board)
        player = players[turn % 2]
        print(f"Ход игрока {player}")

        row, col = get_valid_move(board)
        board[row][col] = player

        if check_winner(board, player):
            print_board(board)
            print(f"Игрок {player} победил!")
            break

        if is_draw(board):
            print_board(board)
            print("Ничья")
            break

        turn += 1

tic_tac_toe()
