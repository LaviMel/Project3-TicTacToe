import os


def print_board():
    print("Board:")
    formatted_board = '\n________\n'.join(['| '.join(row) for row in board])
    print(formatted_board + "\n")


def play_turn(a):
    valid = False
    while not valid:
        row_num = int(input(f"{a} Plays:\nPlease enter 1, 2, or 3 for your desired row: ")) - 1
        col_num = int(input("Please enter 1, 2, or 3 for your desired position within the row: ")) - 1
        if board[row_num][col_num] == " ":
            board[row_num][col_num] = a
            valid = True
            os.system('cls')
            print_board()
        else:
            print("Theres already value in this cell, select again.")


def check(p):
    if (board[0][0] == p and board[1][1] == p and board[2][2] == p) or \
            (board[0][2] == p and board[1][1] == p and board[2][0] == p):
        return True
    for i in range(3):
        if (board[i][0] == p and board[i][1] == p and board[i][2] == p) or \
                (board[0][i] == p and board[1][i] == p and board[2][i] == p):
            return True
    return False


def again(num):
    os.system('cls')
    global round_num, board

    if num == 1 or num == 2:
        print(f"The winner is player {num}! Congratulations!!\n")
    start = input("\nThat's the end of the game. Would you like to play again? y or n. ").lower()
    if start == 'n':
        print("Goodbye.")
        return False
    else:
        print("Get Ready!\n")
        round_num = 0
        board = [[' ' for _ in range(3)] for _ in range(3)]
        return True


board = [[' ' for _ in range(3)] for _ in range(3)]
play = True
round_num = 0

while play:
    round_num += 1
    if round_num == 1:
        print("Let's begin!\n")

    play_turn('X')
    if round_num >= 3:
        if check('X'):
            play = again(1)
            continue

    if round_num >= 9:
        play = again(0)
        continue

    round_num += 1
    play_turn('O')
    if round_num >= 3:
        if check('O'):
            play = again(2)
            continue

