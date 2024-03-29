import random

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 
            'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
class Card:
    
    def __init__(self, suite, rank):
        self.suite = suite
        self.rank = rank
        self.values = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suite
    
class Deck:
    
    def __init__(self):
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                create_card = Card(suit, rank)
                self.all_cards.append(create_card) 
    
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()
    
class Player:
    
    def __init__(self, name):
        self.name = name
        self.all_cards = []
     
    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards"
           
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_card(self, new_cards):
        if type(new_cards) == type([]):
            # a list of multiple card objects
            self.all_cards.extend(new_cards)
        else:
            # a list of a single card object
            self.all_cards.append(new_cards)
 
# Game Logic

# Assign the players           
player_one = Player("One")
player_two = Player("Two")

# Create a new deck and then shuffle the deck
new_deck = Deck()
new_deck.shuffle()

# Split the deck between the two players (26 cards each)
for i in range(26):
    player_one.add_card(new_deck.deal_one())
    player_two.add_card(new_deck.deal_one())

# Check to see if the game needs to carry on or stop and count the rounds   
game_on = True
round_num = 0

while game_on == True:
    round_num += 1 
    print(f"Round {round_num}")
    
    if len(player_one.all_cards) == 0:
        print("Player One, out of cards! Player Two is the winner!")
        game_on = False
        break
    
    if len(player_two.all_cards) == 0: 
        print("Player Two, out of cards! Player One is the winner!")
        game_on = False
        break

    # Start new round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    
    # at_war
    
    at_war = True
    
    while at_war:
        
        if player_one_cards[-1].values > player_two_cards[-1].values:
            
            player_one.add_card(player_one_cards)
            player_one.add_card(player_two_cards)
            
            at_war = False
            
        elif player_one_cards[-1].values < player_one_cards[-1].values:
            
            player_two.add_card(player_one_cards)
            player_two.add_card(player_two_cards)
            
            at_war = False
        
        else:
            print("WAR!")
            
            if len(player_one.all_cards) < 5:
                
                print("Player One unable to play war")
                print("Player Two wins!")
                
                game_on = False
                break
            
            elif len(player_two.all_cards) < 5:
                
                print("Player Two unable to play war")
                print("Player One wins!")
                
                game_on = False
                break
            
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
              
    
    