# Create a version of the game BlackJack 

# To create this prject we will need to:
# 1. Create a deck of 52 cards
# 2. Shuffle the deck
# 3. Ask the Player for their bet
# 4. Make sure that the Player's bet does not exceed their available chips
# 5. Deal two cards to the Dealer and two cards to the Player
# 6. Show only one of the Dealer's cards, the other remains hidden
# 7. Show both of the Player's cards
# 8. Ask the Player if they wish to Hit, and take another card
# 9. If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
# 10. If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
# 11. Determine the winner and adjust the Player's chips accordingly
# 12. Ask the Player if they'd like to play again

# Imports
import random 

# Global variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
         'Queen': 10, 'King': 10, 'Ace': 11}

playing = True 

# Card class
class Card:
    
    def __init__(self, suits, rank):
        self.suits = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + " of " + self.suits
    
# Deck class
class Deck:
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for k in rank:
                create_card = Card(suits, rank)
                self.deck.append(create_card)
    
    def __str__(self):
        full_deck = ""
        for card in self.deck:
            full_deck += "\n" + card.__str__()
        return f"The deck has: {full_deck}"
                
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal_one(self):
        return self.deck.pop()
    
class Hand:
    def __init__(self, card, value, aces):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.card.append(card)
        self.value += values[card.rank] 
    
    def adjust_for_ace(self):
        pass
        
        
        