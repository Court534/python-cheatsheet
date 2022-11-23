# Write a program that simulates the cup and ball game. The program should allow the user to guess the position of the ball within 3 cups.
from random import shuffle

cups = [' ', '0', ' ']

def shuffle_list(cups): 
    shuffle(cups)
    return cups

def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Pick a number: 0, 1, or 2: ")
    return int(guess)

def check_guess(cups, guess):
    if cups[guess] == '0':
        print('Correct!')
        print(cups)
    else:
        print('Wrong guess!')
        print(cups)


mixed_cups = shuffle_list(cups)

guess = player_guess()

check_guess(mixed_cups, guess)