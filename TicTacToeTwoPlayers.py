import sys
board = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}


def print_table():
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


def have_space(board,move):
    return board[move] == ""


def symbol():
    letter = ""
    while not(letter =="X" or letter=="O"):
        letter = input("Do you want and X or O: ").upper()
    if letter == "X":
        return ["X","O"]
    else:
        return ["O","X"]


def win_logic(board,letter):
    if board[1] == letter and board[2] == letter and board[3]==letter:
        return True
    elif board[4] == letter and board[5] == letter and board[6] == letter:
        return True
    elif board[7] == letter and board[8] == letter and board[9] == letter:
        return True
    elif board[1] == letter and board[4] == letter and board[7] == letter:
        return True
    elif board[2] == letter and board[5] == letter and board[8] == letter:
        return True
    elif board[3] == letter and board[6] == letter and board[9] == letter:
        return True
    elif board[1] == letter and board[5] == letter and board[9] == letter:
        return True
    elif board[3] == letter and board[5] == letter and board[7] == letter:
        return True


def main():
    result = symbol()
    user_1_letter,user_2_letter = result[0], result[1]
    for i in range(1,6):
        while True:
            user_1_input = int(input("Player 1 Enter the number (1-9): "))
            if have_space(board,user_1_input):
                board[user_1_input] = user_1_letter
                print_table()
                break

            elif not have_space(board,user_1_input):
                print("\nCan't Overwrite Already Filled Space Try Another Place")

        if win_logic(board,user_1_letter) is True:
            sys.exit("Player 1 wins")
        if i == 5: # as player1 last turn which is fifth from nine turns it will break out form the game
            break

        while True:
            user_2_input = int(input("Player 2 Enter the number (1-9):  "))
            if have_space(board, user_2_input):
                board[user_2_input] = user_2_letter
                print_table()
                break

            elif not have_space(board, user_2_input):
                print("\nCan't Overwrite Already Filled Space Try Another Place")

        if win_logic(board,user_2_letter) is True:
            sys.exit("Player 2 wins\n")

    sys.exit("Draw")


if __name__ == "__main__":
    main()
