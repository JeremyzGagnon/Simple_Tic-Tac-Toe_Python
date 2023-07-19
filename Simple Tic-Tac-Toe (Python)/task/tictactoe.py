from TicTacBoard import TicTacBoard
import re
def main():

    game_board = TicTacBoard()
    game_board.printBoard()

    got_a_winner = False

    symbole = "X"
    flag = 0
    while(not got_a_winner):
        # TODO Improve the CPU process time if removed?
        if flag % 2 == 0:
            symbole = "X"
        else:
            symbole = "O"

        user_coordinate = input().strip()
        if not check_input_validity(user_coordinate, game_board):
            continue
        game_board.add_symbole(user_coordinate, symbole)
        got_a_winner = game_board.game_is_done()
        if got_a_winner:
             break
        flag += 1

def check_input_validity(input, board):
    # Check input is correct format using regular expressions
    # TODO Allow spaced numbers like    1       1
    if not re.match("\d\ \d", input):
        print("You should enter numbers!")
        return False
    # Split the string input and convert them to integers
    row = int(input.split(" ")[0])
    column = int(input.split(" ")[1])

    # Check if the user input is in the range of our board 3 rows and 3 columns
    if row > 3 or row <= 0 or column > 3 or column <= 0:
        print("Coordinates should be from 1 to 3!")
        return False

    if not  cell_is_empty(board,row, column):
        return False
    else:
        return True

    return True

def cell_is_empty(board,row, column):
    if " " in board.board[row - 1][column - 1]:
        return True
    else:
        print("This cell, is occupied! Choose another one!")
        return False

if __name__ == '__main__':
    main()