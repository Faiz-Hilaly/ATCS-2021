import random

class TicTacToe:
  def __init__(self):
    self.board = [[0,0,0],[0,0,0],[0,0,0]]

  @staticmethod
  def print_instructions():
    print("It's tic tac toe. You'll figure it out.")

  def print_board(self):
    print("  0 1 2")
    for i in [0,1,2]:
      row = ""
      for j in [0,1,2]:
        if self.board[i][j] == 0:
          row = row + "– "
        elif self.board[i][j] == 1:
          row = row + "X "
        elif self.board[i][j] == -1:
          row = row + "O "
      
      print(str(i)+ " " + row)

  def is_valid_move(self, row, col):
    if 0 > min(row,col) or max(row,col) > 2: return False
    return self.board[row][col] == 0
    

  def place_player(self, player, row, col):    
    self.board[row][col] = player

  def take_manual_turn(self, player):
    row = int(input("Please enter a row number between 0 and 2: "))
    col = int(input("Please enter a column number between 0 and 2: "))

    while not self.is_valid_move(row,col):
      row = int(input("Please enter a valid row number: "))
      col = int(input("Please enter a valid column number: "))

    self.place_player(player,row,col)
  
  def take_random_turn(self, player):
    row = random.randint(0,2)
    col = random.randint(0,2)
    
    while not self.is_valid_move(row,col):
      row = random.randint(0,2)
      col = random.randint(0,2)
      
    return self.place_player(player,row,col)

  def take_turn(self, player):
    if player == 1:
      print("It is player " + str(player) + "'s turn")
      self.take_manual_turn(player)
    if player == -1:
      print("It is player " + str(player*-2) + "'s turn")
      self.take_minimax_turn(player)

  def take_minimax_turn(self, player):
    score, row, col = self.minimax(player)
    self.place_player(player, row, col)

  def minimax(self, player):
    # Base case: Player 1 (X) tries to minimize, player -1 (O) maximizes
    if self.check_win(-1): return 10, None, None
    if self.check_win(1): return -10, None, None
    if self.check_tie(): return 0, None, None

    bestscore, row, col = player*20, None, None
    for i in [0,1,2]:
      for j in [0,1,2]:
        if self.is_valid_move(i, j):
          self.place_player(player, i, j)
          #temp_result = self.minimax(-1*player)
          #score, r, c = temp_result
          score, r, c = self.minimax(-1*player)
          if player*(score - bestscore) < 0:
            bestscore, row, col = score, i, j
          self.place_player(0, i, j)
    return bestscore, row, col

  def check_win(self, player):
    b = self.board
    def check_three(x1,y1,x2,y2,x3,y3):
      return b[x1][y1] == player and b[x2][y2] == player and b[x3][y3] == player
    for row in [0,1,2]:
      if check_three(row,0,row,1,row,2): return True
    for col in [0,1,2]:
      if check_three(0,col,1,col,2,col): return True
    if check_three(0,0,1,1,2,2): return True
    if check_three(0,2,1,1,2,0): return True
    return False

  def check_tie(self):
    for i in [0,1,2]:
      if 0 in self.board[i]: return False
    return not self.check_win(1) and not self.check_win(-1)

  def play_game(self):
    TicTacToe.print_instructions()
    player = 1
    while True:
      self.print_board()
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
      player = -1*player