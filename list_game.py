# Simple interacted program that allows a user to:
# Display a list
# Choose an index position and input a value
# Replace value at index position with a user's chosen input 

def display_game(game_list):
  print("Here is the current list: ")
  print(game_list)

def position_choice():
  
  choice = "Wrong"
  accepable_values = ["0", "1", "2"]
  
  while choice not in accepable_values:
    
    choice = input("Pick a position (0, 1, 2): ")
    
    if choice not in accepable_values:
      print("Sorry, invalid choice!")
      
  return int(choice)

def replacement_choice(game_list, position):
  
  user_placement = input("Type a string to be placed at position: ")
  
  game_list[position] = user_placement
  
  return game_list

def gameon_choice():
  
  choice = "Wrong"
  accepable_values = ["Yes", "No"]
  
  while choice not in accepable_values:
    
    choice = input("Would you like to keep playing? (Yes ot No) ")
    
    if choice not in accepable_values:
      print("Sorry, invalid choice!")
      
  if choice == "Yes":
    return True
  else:
    return False
  
game_on = True
game_list = [0,1,2]

while game_on:
  display_game(game_list)
  
  position = position_choice()
  
  game_list = replacement_choice(game_list, position)
  
  display_game(game_list)
  
  game_on = gameon_choice()
  
  
