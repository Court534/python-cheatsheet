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
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + " of " + self.suit
    
# Deck class
class Deck:
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                create_card = Card(suit, rank)
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
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank] 
        if card.rank == "Ace":
            self.aces += 1
            
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1        
            
class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet 
    
    def lose_bet(self):
        self.total -= self.bet
    
    def take_bet(self, chips):
        while True:
            try:
                chips.bet = int(input("How many chips would you like to bet? ")) 
                chips.total -= chips.bet
                return f"You just bet {chips.bet}, you have {chips.total} chips left" 
            except:
                print("Sorry, please provide an integer")
            else:
                if chips.bet > chips.total:
                    return f"You dont have enough chips, you only have {chips.total} chips left"
                else:
                    break
                
    def hit(self, deck, hand):
        hand.add_card()
        hand.adjust_for_ace()
        
    def hit_or_stand(self, deck, hand):
        global playing
        
        while True:
            x = input("Hit or Stand?")
            
            if x.lower() == "hit":
                hit(deck, hand)   
            elif x.lower() == "stand":
                print("Player stands, Dealers turn")
                playing = False
            else:
                print("Sorry, Please enter Hit or Stand")
                continue
            break
        
    def show_some(self, player, dealer):
        print("\n Dealers hand: ")
        print("First card hidden!")
        print(dealer.card[1])
        
        print("\n Players cards: ")
        for card in player.cards:
            print(card)
            
    def show_all(self, player, dealer):
        print("\n Dealers final hand: ")
        for card in dealer.cards:
            print(cards)
        print(f"The value of the Dealers hand is: {dealer.value}")
         
        print("Players final hand: ")   
        for card in player.cards:
            print(cards)
        print(f"The value of the Players hand is: {player.value}")
        
    def player_busts(self, player, dealer, chips):
        #if player.cards.value > dealer.cards.value:
            chips.lose_bet()
            print("Player busts! Dealer is the winner")
        
    def player_wins(self, player, dealer, chips):
        #if player.cards.value  <= 21 and player.cards.value > dealer.cards.value:
            chips.win_bet()
            print("Player wins!")

    def dealer_busts(self, player, dealer, chips):
        #if dealer.cards.value > 21:
            chips.lose_bet
            print(f"Dealer busts with {dealer.cards.value}, Player wins!")
        
    def dealer_wins(self, player, dealer, chips):
        # if dealer.cards.value <= 21 and dealer.cards.value > player.cards.value:
            chips.win_bet
            print("Dealer wins!")
        
    def push(self, player, dealer):
        print("It's a tie!")
        
while True:
    print("Welcome to BlackJack!")
        
    # Create and shuffle the deck
    deck = Deck()
    deck.shuffle()
        
    # Create players hand
    player_hand = Hand()
    player_hand.add_card(deck.deal_one())
    player_hand.add_card(deck.deal_one())
        
    # Create dealers hand 
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal_one())
    dealer_hand.add_card(deck.deal_one())
        
    # Assign the player 100 chips
    player_chips = Chips()
        
    # Ask the player how many chips he would like to bet
    take_bet(player_chips)
        
    # Show cards
    show_some(player_hand, dealer_hand)
        
    while playing:
            
        # Player Hit or Stand? 
        hit_or_stand(deck, player_hand)
            
        # Show cards but keep one of the dealers hidden
        show_some(player_hand, dealer_hand)
            
        # If player busts
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            
        # If player has not busted dealer will keep playing until his cards >= 17
        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(deack, dealer_hand)
                
        # Show all cards
        show_all(dealer_hand, player_hand)
            
        # Show the winner
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
                
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
                
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
            
        else: 
            push(player_hand, dealer_hand)
                
        # Let the player know their chip total
        print(f"Player total chips: {player_chips.total}")
            
        new_game = input("Would you like to play again? Yes or No")
        if new_game[0].lower() == "y":
            playing = True
        else:
            print("Thank you for playing :)")
            break
        
        
        
        
                
        
        
        
    