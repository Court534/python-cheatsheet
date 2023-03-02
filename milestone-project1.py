# Tic Tac Toe

# User criteria:
# 2 players should be able to play (on the same computer)
# The board should be printed everytime a player makes a move
# Need to be able to accept input of the player postition and then place a 
# symbol on the board

def display_board(board):
  
  board = ([" ", " ", " "
         " ", " ", " "
         " ", " ", " "])
  
  print("Here is the current board: ")
  print(board)
  
  display_board(board)
  
def player_input():
  
  acceptable_inputs = ["X", "O"]