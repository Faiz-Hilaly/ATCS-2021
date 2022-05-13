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

  def take_algorithm_turn(self,player):
    #make it so that human can make a move 
    #then computer makes a move based on which ever gets the highest score
    best_row = 0
    best_col = 0
    best_score = -10000

    for row in range(0,7):
      for col in range(0,7):
        if self.is_valid_move(row,col):
          self.place_player(player,row,col)
          score = self.board_score(player)+self.board_score(-player)
          print(score)
          if score > best_score:
            best_score = score
            best_row = row
            best_col = col
            self.place_player(0,row,col)
          else:
            self.place_player(0,row,col)
    self.place_player(player,best_row,best_col)


  def take_turn(self, player):
    if player == 1:
      print("It is player " + str(player) + "'s turn")
      self.take_manual_turn(player)
    if player == -1:
      print("It is player " + str(player*-2) + "'s turn")
      self.take_algorithm_turn(player)

  
  def board_score(self, player):
    score = 0
    score_four = player*-100
    score_three = player*-50
    b = self.board

    #Lower score means player 1 is better, higher score means player 2 is better
    #need to create an algorithm that recognizes boards where opponent has many pieces in a row are bad
    #and board where algorithm has many points in a row is good
    #make a test that looks at 5 squares and does a test to see what is in those 5 squares.
    def check_three(x1,y1,x2,y2,x3,y3):
      return b[x1][y1] == player and b[x2][y2] == player and b[x3][y3] == player
    for row in range(0,7):
      if check_three(row,0,row,1,row,2): score = score + score_three
      if check_three(row,1,row,2,row,3): score = score + score_three
      if check_three(row,2,row,3,row,4): score = score + score_three
      if check_three(row,3,row,4,row,5): score = score + score_three
      if check_three(row,4,row,5,row,6): score = score + score_three
    for col in range(0,7):
      if check_three(0,col,1,col,2,col): score = score + score_three
      if check_three(1,col,2,col,3,col): score = score + score_three
      if check_three(2,col,3,col,4,col): score = score + score_three
      if check_three(3,col,4,col,5,col): score = score + score_three
      if check_three(4,col,5,col,6,col): score = score + score_three
    for row in range(0,5):
      for col in range(0,5):
        if check_three(row,col,row+1,col+1,row+2,col+2): score = score + score_three
        if check_three(6-row,col,5-row,col+1,4-row,col+2): score = score + score_three

    def check_four(x1,y1,x2,y2,x3,y3,x4,y4):
      return b[x1][y1] == player and b[x2][y2] == player and b[x3][y3] == player and b[x4][y4] == player
    for row in range(0,7):
      if check_four(row,0,row,1,row,2,row,3): score = score + score_four
      if check_four(row,1,row,2,row,3,row,4): score = score + score_four
      if check_four(row,2,row,3,row,4,row,5): score = score + score_four
      if check_four(row,3,row,4,row,5,row,6): score = score + score_four
    for col in range(0,7):
      if check_four(0,col,1,col,2,col,3,col): score = score + score_four
      if check_four(1,col,2,col,3,col,4,col): score = score + score_four
      if check_four(2,col,3,col,4,col,5,col): score = score + score_four
      if check_four(3,col,4,col,5,col,6,col): score = score + score_four
    
    for row in range(0,4):
      for col in range(0,4):
        if check_four(row,col,row+1,col+1,row+2,col+2,row+3,col+3): score = score + score_four
        if check_four(6-row,col,5-row,col+1,4-row,col+2,3-row,col+3): score = score + score_four 
    return score


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
