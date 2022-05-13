#Version 2
#5/1/2022
import random
import time

class TicTacToe:
  def __init__(self):
    self.board = [[0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0]]

  @staticmethod
  def print_instructions():
    print("This game is played between two players, where players alternate taking turns.")
    print("On any given turn, a player may choose to either (1)place a new piece or (2)move two pieces to new positions on the board")
    print("The first player to connect 5 pieces in a row is the winner.")

  def print_board(self):
    print("  0 1 2 3 4 5 6")
    for i in range(0,7):
      row = ""
      for j in range(0,7):
        if self.board[i][j] == 0:
          row = row + "– "
        elif self.board[i][j] == 1:
          row = row + "X "
        elif self.board[i][j] == -1:
          row = row + "O "
      
      print(str(i)+ " " + row)

  def is_valid_move(self, row, col):
    if 0 > min(row,col) or max(row,col) > 6: return False
    return self.board[row][col] == 0
   
  def is_valid_piece(self, player, row, col):
      return self.board[row][col] == player

  def place_player(self, player, row, col):    
    self.board[row][col] = player

  def remove_player(self, player, row, col):
    self.board[row][col] = 0

  def move_piece(self,player):
    old_row = int(intput("Please enter the row number of the piece you would like to move: "))
    old_col = int(intput("Please enter the column number of the piece you would like to move: "))
    while not self.is_valid_piece(row,col):
      old_row = int(input("Please enter your piece's row number: "))
      old_col = int(input("Please enter your piece's column number: "))

    new_row = int(intput("Please enter the row number of the piece you would like to move: "))
    new_col = int(intput("Please enter the column number of the piece you would like to move: "))
    while not self.is_valid_move(row,col):
      new_row = int(input("Please enter a valid row number: "))
      new_col = int(input("Please enter a valid column number: "))

    self.remove_player(player, old_row, old_col)
    self.place_player(player, new_row, new_col)


  def take_manual_turn(self, player):
    row = int(input("Please enter a row number between 0 and 6: "))
    col = int(input("Please enter a column number between 0 and 6: "))

    while not self.is_valid_move(row,col):
      row = int(input("Please enter a valid row number: "))
      col = int(input("Please enter a valid column number: "))

    self.place_player(player,row,col)

  def check_threat(self,player)
      b = self.board
    def check_three(x1,y1,x2,y2,x3,y3):
      return b[x1][y1] == player and b[x2][y2] == player and b[x3][y3] == player
    for row in range(0,7):
      if check_three(row,0,row,1,row,2): return 1
      if check_three(row,1,row,2,row,3): return 2
      if check_three(row,2,row,3,row,4): return 2
      if check_three(row,3,row,4,row,5): return 2
      if check_three(row,4,row,5,row,6): return 3
    for col in range(0,7):
      if check_three(0,col,1,col,2,col): return 4
      if check_three(1,col,2,col,3,col): return 5
      if check_three(2,col,3,col,4,col): return 5
      if check_three(3,col,4,col,5,col): return 5
      if check_three(4,col,5,col,6,col): return 6
    if check_three(0,0,1,1,2,2): return 7
    if check_three(1,1,2,2,3,3): return 8
    if check_three(2,2,3,3,4,4): return 8
    if check_three(3,3,4,4,5,5): return 8
    if check_three(4,4,5,5,6,6): return 9
    if check_three(0,6,1,5,2,4): return 10
    if check_three(1,5,2,4,3,3): return 11
    if check_three(2,4,3,3,4,2): return 11
    if check_three(3,3,4,2,5,1): return 11
    if check_three(4,2,5,1,6,0): return 12
    return False  
    
    def check_four(x1,y1,x2,y2,x3,y3,x4,y4):
      return b[x1][y1] == player and b[x2][y2] == player and b[x3][y3] == player and b[x4][y4] == player and b[x5][y5] == player
    for row in range(0,7):
      if check_four(row,0,row,1,row,2,row,3): return True
      if check_four(row,1,row,2,row,3,row,4): return True
      if check_four(row,2,row,3,row,4,row,5): return True
      if check_four(row,3,row,4,row,5,row,6): return True
    for col in range(0,7):
      if check_four(0,col,1,col,2,col,3,col): return True
      if check_four(1,col,2,col,3,col,4,col): return True
      if check_four(2,col,3,col,4,col,5,col): return True
      if check_four(3,col,4,col,5,col,6,col): return True
    if check_four(0,0,1,1,2,2,3,3): return True
    if check_four(1,1,2,2,3,3,4,4): return True
    if check_four(2,2,3,3,4,4,5,5): return True
    if check_four(3,3,4,4,5,5,6,6): return True
    if check_four(0,6,1,5,2,4,3,3): return True
    if check_four(1,5,2,4,3,3,4,2): return True
    if check_four(2,4,3,3,4,2,5,1): return True
    if check_four(3,3,4,2,5,1,6,0): return True
    return False


  def check_win(self, player):
    b = self.board
    def check_five(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5):
      return b[x1][y1] == player and b[x2][y2] == player and b[x3][y3] == player and b[x4][y4] == player and b[x5][y5] == player
    for row in range(0,7):
      if check_five(row,0,row,1,row,2,row,3,row,4): return True
      if check_five(row,1,row,2,row,3,row,4,row,5): return True
      if check_five(row,2,row,3,row,4,row,5,row,6): return True
    for col in range(0,7):
      if check_five(0,col,1,col,2,col,3,col,4,col): return True
      if check_five(1,col,2,col,3,col,4,col,5,col): return True
      if check_five(2,col,3,col,4,col,5,col,6,col): return True

    for row in range(0,3):
      for col in range(0,3):
        if check_five(row,col,row+1,col+1,row+2,col+2,row+3,col+3,row+4,col+4): return True
        if check_five(6-row,col,5-row,col+1,4-row,col+2,3-row,col+3,2-row,col+4): return True
    return False

  def check_tie(self):
    for i in range(0,7):
      if 0 in self.board[i]: return False
    return not self.check_win(1) and not self.check_win(-1)

  def play_game(self):
    c = 0
    TicTacToe.print_instructions()
    player = 1
    while True:
      self.print_board()
      if(c >= 2):
        if player == 1:
          turn_type = int(input("Would you like to (1)place a new piece or (2)move existing pieces."+
                                "Please type the number that corresponds with your choice: "))
          while not (turn_type == 1 or turn_type == 2):
            turn_type = int(input("Please select your choice by typing 1 or 2: "))
          if turn_type == 1:
            self.take_turn(player)
          if turn_type == 2:
            self.move_piece(player)
        if player == -1:
          self.take_turn(player)         
      else:
        self.take_turn(player)

      if self.check_win(player):
        if player == 1: print("Player " + str(player) + " wins.")
        if player == -1: print("Player " + str(player*-2) + " wins.")
        self.print_board()
        break
      if self.check_tie():
        print("It's a tie.")
        self.print_board()
        break
      c=c+0.5
      player = -1*player
