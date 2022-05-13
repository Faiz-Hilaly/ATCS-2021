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
    self.five_in_a_row = []
        #check rows
    for row in range(0,7):
      for col in range(0,3):
        self.five_in_a_row.append([row,col,row,col+1,row,col+2,row,col+3,row,col+4])
    #check columns
    for row in range(0,3):
      for col in range(0,7):
          self.five_in_a_row.append([row,col,row+1,col,row+2,col,row+3,col,row+4,col])
    #check diagonals
    for row in range(0,3):
      for col in range(0,3):
          self.five_in_a_row.append([row,col,row+1,col+1,row+2,col+2,row+3,col+3,row+4,col+4])
          self.five_in_a_row.append([6-row,col,5-row,col+1,4-row,col+2,3-row,col+3,2-row,col+4])

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
    old_row = int(input("Please enter the row number of the piece you would like to move: "))
    old_col = int(input("Please enter the column number of the piece you would like to move: "))
    while not self.is_valid_piece(player,old_row,old_col):
      old_row = int(input("Please enter your piece's row number: "))
      old_col = int(input("Please enter your piece's column number: "))

    new_row = int(input("Please enter the piece's new row number: "))
    new_col = int(input("Please enter the piece's new column number: "))
    while not self.is_valid_move(new_row,new_col):
      new_row = int(input("Please enter a valid new row number: "))
      new_col = int(input("Please enter a valid new column number: "))

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
    #get every possible two pieces it has, then once you have them remove them and place them in 
    # a new place of every possible two places
    #generate a list of every space on the board where the alogirthm has pieces
    #generate a list of every empty space on the board
    #generate list of every pair of spaces and a list of every pair of pieces the alogirthm has
    #consider the board where you remoe those two pieces and plcae it in those two spaces
    best_pieces_removed = []
    best_pieces_added = []
    best_score = 1000
    score = 0

    #create list of all the algorithms current pieces and all the empty spaces on the board
    alg_pieces = []
    empty_spaces = []
    for row in range(0,7):
      for col in range(0,7):
        if self.is_valid_piece(player,row,col):
          alg_pieces.append([row,col])
        if self.board[row][col] == 0: 
          empty_spaces.append([row,col])

    #create list of every possible pair of algorithm current pieces
    alg_paired_pieces = []
    for a in range(0,len(alg_pieces)-1):
      for b in range(a+1,len(alg_pieces)):
        alg_paired_pieces.append([alg_pieces[a],alg_pieces[b]])

    #create list of every possible pair of empty spaces
    empty_paired_pieces = []
    for a in range(0,len(empty_spaces)-1):
      for b in range(a+1,len(empty_spaces)):
        empty_paired_pieces.append([empty_spaces[a],empty_spaces[b]])

  def take_turn(self, player):
    if player == 1:
      print("It is player " + str(player) + "'s turn")
      self.take_manual_turn(player)
    if player == -1:
      print("It is player " + str(player*-2) + "'s turn")
      self.take_algorithm_turn(player)


  def board_score(self):
    #Lower score means player 1 is better, higher score means player 2 is better
    score = 0
    b = self.board

    for group_of_five_squares in self.five_in_a_row:
      num_pOne_appearances = 0
      num_pTwo_appearances = 0

      row1 = group_of_five_squares[0]
      col1 = group_of_five_squares[1]
      row2 = group_of_five_squares[2]
      col2 = group_of_five_squares[3]
      row3 = group_of_five_squares[4]
      col3 = group_of_five_squares[5]
      row4 = group_of_five_squares[6]
      col4 = group_of_five_squares[7]
      row5 = group_of_five_squares[8]
      col5 = group_of_five_squares[9]

      if b[row1][col1] == 1: num_pOne_appearances += 1
      if b[row2][col2] == 1: num_pOne_appearances += 1
      if b[row3][col3] == 1: num_pOne_appearances += 1
      if b[row4][col4] == 1: num_pOne_appearances += 1
      if b[row5][col5] == 1: num_pOne_appearances += 1

      if b[row1][col1] == -1: num_pTwo_appearances += 1
      if b[row2][col2] == -1: num_pTwo_appearances += 1
      if b[row3][col3] == -1: num_pTwo_appearances += 1
      if b[row4][col4] == -1: num_pTwo_appearances += 1
      if b[row5][col5] == -1: num_pTwo_appearances += 1

      winning_score = 1000000000

      alg_unblocked_four_score = 500
      player_unblocked_four_score = 600
      alg_unblocked_three_score = 300
      player_unblocked_three_score = 400
      alg_unblocked_two_score = 100
      player_unblocked_two_score = 150
      alg_unblocked_one_score = 50
      player_unblocked_one_score = 75

      if num_pOne_appearances == 5 and num_pTwo_appearances == 0: score += winning_score
      if num_pOne_appearances == 0 and num_pTwo_appearances == 5: score -= winning_score
      if num_pOne_appearances == 4 and num_pTwo_appearances == 0: score += player_unblocked_four_score
      if num_pOne_appearances == 0 and num_pTwo_appearances == 4: score -= alg_unblocked_four_score
      if num_pOne_appearances == 3 and num_pTwo_appearances == 0: score += player_unblocked_three_score
      if num_pOne_appearances == 0 and num_pTwo_appearances == 3: score -= alg_unblocked_three_score
      if num_pOne_appearances == 2 and num_pTwo_appearances == 0: score += player_unblocked_two_score
      if num_pOne_appearances == 0 and num_pTwo_appearances == 2: score -= alg_unblocked_two_score
      if num_pOne_appearances == 1 and num_pTwo_appearances == 0: score += player_unblocked_one_score
      if num_pOne_appearances == 0 and num_pTwo_appearances == 1: score -= alg_unblocked_one_score

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
            for i in range(0,2):
              print("Moving piece", str(i+1))
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
