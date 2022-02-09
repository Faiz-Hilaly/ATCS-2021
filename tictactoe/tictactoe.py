import random
from array import *

class TicTacToe:
    def __init__(self):
        # TODO: Set up the board to be '-'
        self.board = [[0,0,0],[0,0,0],[0,0,0]]

    @staticmethod
    def print_instructions():
        # TODO: Print the instructions to the game
        print("It's tic tac toe. Player 1 is X and Player 2 is O.")

    def print_board(self):
        # TODO: Print the board
        print("  0 1 2")
        for i in range(len(self.board)):
            row = ""
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    row = row + "– "
                elif self.board[i][j] == 1:
                    row = row + "X "
                elif self.board[i][j] == 2:
                    row = row + "O "
            
            print(str(i)+ " " + row)

    def is_valid_move(self, row, col):
        # TODO: Check if the move is valid
        if (0 > row and row > 2) and (0 > col and col > 2):
            return False

        if self.board[row][col] != 0:
            return False
        
        return True
        

    def place_player(self, player, row, col):
        while not self.is_valid_move(row,col):
            row = int(input("Please enter a valid row number: "))
            col = int(input("Please enter a valid column number: "))
        
        self.board[row][col] = player
        return

    def take_manual_turn(self, player):
        # TODO: Ask the user for a row, col until a valid response
        #  is given them place the player's icon in the right spot
        print("It is player " + str(player) + "'s turn")

        row = int(input("Please enter a row number between 0 and 2: "))
        col = int(input("Please enter a column number between 0 and 2: "))

        self.place_player(player,row,col)
        

    def take_turn(self, player):
        # TODO: Simply call the take_manual_turn function
        self.take_manual_turn(player)
        return

    def check_col_win(self, player):
        for i in range(len(self.board)):
                if (player == self.board[0][i]) and (self.board[0][i] == self.board[1][i]) and (self.board[1][i] == self.board[2][i]):
                    return True
        return False

    def check_row_win(self, player):
        for i in range(len(self.board)):
                if (player == self.board[i][0]) and (self.board[i][0] == self.board[i][1]) and (self.board[i][1] == self.board[i][2]):
                    return True
        return False

    def check_diag_win(self, player):
        if (player == self.board[0][0]) and (self.board[0][0] == self.board[1][1]) and (self.board[1][1] == self.board[2][2]):
            return True
        if (player == self.board[0][2]) and (self.board[0][2] == self.board[1][1]) and (self.board[1][1] == self.board[2][0]):
            return True
        return False

    def check_win(self, player):
        if self.check_col_win(player) or self.check_row_win(player) or self.check_diag_win(player):
            return True
        return False

    def check_tie(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    return False
        return True

    def play_game(self):
        TicTacToe.print_instructions()
        self.print_board()

        while not (self.check_win(1) or self.check_win(2) or self.check_tie()):
            self.take_turn(1)
            self.print_board()
            if self.check_win(1):
                print("Player 1 wins.")
                return
            if self.check_tie():
                print("It's a tie.")
                return
            
            self.take_turn(2)
            self.print_board()
            if self.check_win(2):
                print("Player 2 wins.")
                return 
            if self.check_tie():
                print("It's a tie.")
                return
        return

