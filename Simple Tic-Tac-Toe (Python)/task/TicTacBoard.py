import re

class TicTacBoard:

    def __init__(self):
        self.boardRow1 = [" ", " ", " "]
        self.boardRow2 = [" ", " ", " "]
        self.boardRow3 = [" ", " ", " "]
        self.board = [self.boardRow1, self.boardRow2, self.boardRow3]

    # Logic to add a symbole on the board
    # Return true if there's an error in the input so user can retry
    def add_symbole(self,input, symbole):
        row= int(input.split(" ")[0])
        column = int(input.split(" ")[1])
        # Decrease the inputs so it works with our indexes
        row -= 1
        column -= 1
        # Call the cell_is_empty method to see if we can add an X or O in that position
        self.board[row][column] = symbole
        self.printBoard()

    # Call this method to end the game
    def game_is_done(self):

        x_win = self.determine_winner("X")
        o_win = self.determine_winner("O")

        # TODO Make a better if statement
        if not o_win and not x_win and " "  in self.boardRow1 and " "  in self.boardRow2 and " "  in self.boardRow3:
            # print("Game not finished")
            return False

        if not o_win and not x_win and " " not in self.boardRow1 and " " not in self.boardRow2 and " " not in self.boardRow3:
            print("Draw")
            return True

        if x_win:
            print("X wins")
            return True

        if o_win:
            print("O wins")
            return True
    def printBoard(self):
        try:
            print("""
            ---------
            | {} {} {} |
            | {} {} {} |
            | {} {} {} |
            ---------
            """.format(*self.boardRow1, *self.boardRow2, *self.boardRow3))
        except AttributeError:
            pass
    def determine_winner(self, char):
        # TODO the loop is unecessary
        for i in range(0, len(self.board)):
            for j in range(0, len(self.boardRow1)):
                if i == 0 and j == 0:
                    # Horizontal 🟢
                    if self.board[i][j] == self.board[i][j + 1] == self.board[i][j + 2] == char or self.board[i + 1][j] == self.board[i + 1][j + 1] == self.board[i + 1][j + 2] == char or self.board[i + 2][j] == self.board[i + 2][j + 1] == self.board[i + 2][j + 2] == char:
                        return True
                    # # Diagonal 🟢
                    elif self.board[i][j] == self.board[i + 1][j + 1] == self.board[i + 2][j + 2] == char or self.board[i][j + 2] == self.board[i + 1][j + 1] == self.board[i + 2][j] == char:
                        return True
                #     Vertical 🟢
                    elif self.board[i][j] == self.board[i + 1][j] == self.board[i + 2][j] == char or self.board[i][j + 1] == self.board[i + 1][j + 1] == self.board[i + 2][j + 1] == char or self.board[i][j + 2] == self.board[i + 1][j + 2] == self.board[i + 2][j + 2] == char:
                        return True
                    else:
                        return False


