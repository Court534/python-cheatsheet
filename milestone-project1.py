# Tic Tac Toe

# User criteria:
# 2 players should be able to play (on the same computer)
# The board should be printed everytime a player makes a move
# Need to be able to accept input of the player postition and then place a 
# symbol on the board

import random from randit

def display_board():
  
  board = ["7", "8", "9", "4", "5", "6", "1", "2", "3"]
  
  print("Here is the current board: ")
  print(board[6] + "|" + board[7] + "|" + board[8])
  print(board[3] + "|" + board[4] + "|" + board[5])
  print(board[0] + "|" + board[1] + "|" + board[2])
  
display_board()

def player_input():
  
  choice = "Wrong!"
  acceptable_inputs = ["X", "O"]
  
  while choice not in acceptable_inputs:
    
    choice = input("Please ")