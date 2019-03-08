# Vinh Pham
# 11/29/16
# Lab 13 - Thirty-One; Write a program for the game ThirtyOne

class Card(object): 
    def __init__(self,new_suit,new_value):  # To create cards with attributes suit and value.
        self.suit = new_suit
        self.value = new_value
    def __str__(self):
        return "{} of {}".format(self.value,self.suit)
    def is_greater_than(self,other_card):
        if self.value.lower() in ["jack", "queen", "king"]:
            self_value = 10
        elif self.value.lower() == "ace":
            self_value = 11
        else:
            self_value = self.value
            
        if other_card.value.lower() in ["jack", "queen", "king"]:
            other_card_value = 10
        elif other_card.value == "ace":
            other_card_value = 11
        else:
            other_card_value = other_card.value
    
        if int(self_value) > int(other_card_value):
            return True
        else:
            return False
    

class Deck(object): 
    def __init__(self): # To generate a deck of cards (shuffled)
        list_of_cards = []
        for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for value in ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]:
                list_of_cards.append(Card(suit,value))
        self.list_of_cards = list_of_cards           
        self.shuffle()
    def __str__(self):  # Using return would instead create list of memory locations.
        my_str = ""
        for card in self.list_of_cards:
            my_str = my_str + str(card) + ","
        list_of_cards = my_str.split(",")
        list_of_cards.pop() #Takes off the "," as the last item
        return list_of_cards
    def shuffle(self):
        import random
        random.shuffle(self.list_of_cards)
    def deal(self):
       return self.list_of_cards.pop()
    def empty(self):
        if len(self.list_of_cards) == 0:
            return True
        else:
            return False

def test(): # To test classes and methods.
    my_card = Card("Hearts","Jack")
    your_card = Card("Spades","9")
    print (my_card.__str__())
    print (my_card.is_greater_than(your_card))

    my_deck = Deck()
    print (my_deck.__str__())
    print (my_deck.shuffle())
    print (my_deck.deal())
    print (my_deck.empty())


def main():
    my_deck = Deck()    #Initialize a shuffled deck
    player1_hand = []   
    player2_hand = []
    for n in range(3):  #Deal 3 cards per player
        player1_hand.append(my_deck.deal())
        player2_hand.append(my_deck.deal())

    turn_counter = 1
    player1_knock, player2_knock = "n","n"
    discard_card = 0

    print ("Welcome to Thirty-One!")
    
    while player1_knock != "y" or len(my_deck.list_of_cards) == 0: #Cards run out or player 1 knocks
        if player2_knock == "y":
            print ("\nIt's Player 1's FINAL turn!")
        else:
            print ("\nIt's Player 1's turn number {}.".format(turn_counter))
        print ("Player 1 has: ",end="")
        for card in player1_hand:
            print (card,end=", ")       
        action = input("\nWould you like to (1) draw from discard or (2) draw from the deck?: ")
        while action not in ["1","2"]:  #They must choose (1) or (2).
            action = input("That is not an option. Please pick (1) or (2).")
        if action == "1":
            if discard_card == 0:   #No other choice if first turn.
                print ("There is no discard card. You must draw from the deck.")
                player1_hand.append(my_deck.deal())
            else:
                player1_hand.append(discard_card)
        elif action == "2":
            player1_hand.append(my_deck.deal())                     
        print ("Player 1 has: ",end="")
        for card in player1_hand:
            print (card,end=", ")
        print("\nWhich card would you like to discard? \n (1) {} \n (2) {} \n (3) {} \n (4) {}"\
                             .format(player1_hand[0],player1_hand[1],player1_hand[2],player1_hand[3]))
        discard_index = int(input())
        while discard_index not in [1,2,3,4]:   #In case card doesn't exist
            discard_index = int(input("That option doesn't exist. Please select a card: "))
        discard_card = player1_hand[discard_index-1]
        player1_hand.pop(discard_index-1)
        if player2_knock == "y":
            break
        player1_knock = input("Would Player 1 like to knock? (y/n): ")
        
        

        if player1_knock == "y":
            print ("\nIt's Player 2's FINAL turn!")
        else:
            print ("\nIt's Player 2's turn number {}.".format(turn_counter))
        print ("Player 2 has: ",end="")
        for card in player2_hand:
            print (card,end=", ")
        print ("\nThe discard card is {}: ".format(discard_card))
        action = input("Would you like to (1) draw from discard or (2) draw from the deck?: ")
        while action not in ["1","2"]:  #They must choose (1) or (2)
            action = input("That is not an option. Please pick (1) or (2).")
        if action == "1":
            player2_hand.append(discard_card)
        elif action == "2":
            player2_hand.append(my_deck.deal())
        print("Which card would you like to discard? \n (1) {} \n (2) {} \n (3) {} \n (4) {}"\
                             .format(player2_hand[0],player2_hand[1],player2_hand[2],player2_hand[3]))
        discard_index = int(input())
        while discard_index not in [1,2,3,4]:   #In case card doesn't exist
            discard_index = int(input("That option doesn't exist. Please select a card: "))
        discard_card = player2_hand[discard_index-1]
        player2_hand.pop(discard_index-1)
        if player1_knock == "y":
            break
        player2_knock = input("Would Player 2 like to knock? (y/n): ")

        turn_counter+=1

        
    # Time to generate the scores
    print ("\n")
    print ("The game is now over.")
    player1_scores = {"Spades":0, "Clubs":0, "Diamonds":0, "Hearts":0}  #Dictionary to keep suit values
    player2_scores = {"Spades":0, "Clubs":0, "Diamonds":0, "Hearts":0}
    player1_spades,player1_clubs,player1_diamonds,player1_hearts = 0,0,0,0
    player2_spades,player2_clubs,player2_diamonds,player2_hearts = 0,0,0,0

    # Convert, and calculate scores.
    for card in player1_hand:
        if card.value.lower() in ["jack", "queen", "king"]:
            card_value = 10
        elif card.value.lower() == "ace":
            card_value = 11
        else:
            card_value = card.value
            
        if card.suit.lower() == "spades":
            player1_scores["Spades"] += int(card_value)
        elif card.suit.lower() == "clubs":
            player1_scores["Clubs"] += int(card_value)
        elif card.suit.lower() == "diamonds":
            player1_scores["Diamonds"] += int(card_value)
        else:
            player1_scores["Hearts"] += int(card_value)
            
    for card in player2_hand:
        if card.value.lower() in ["jack", "queen", "king"]:
            card_value = 10
        elif card.value.lower() == "ace":
            card_value = 11
        else:
            card_value = card.value

        if card.suit.lower() == "spades":
            player2_scores["Spades"] += int(card_value)
        elif card.suit.lower() == "clubs":
            player2_scores["Clubs"] += int(card_value)
        elif card.suit.lower() == "diamonds":
            player2_scores["Diamonds"] += int(card_value)
        else:
            player2_scores["Hearts"] += int(card_value)

    player1_suit = max(player1_scores,key=player1_scores.get)   #Readability purposes
    player1_value = player1_scores[max(player1_scores,key=player1_scores.get)]
    player2_suit = max(player2_scores,key=player2_scores.get)
    player2_value = player2_scores[max(player2_scores,key=player2_scores.get)]

    # And the winner is...
    print ("Player 1 has {} points in {}!"\
           .format(player1_value,player1_suit))
    print ("Player 2 has {} points in {}!"\
           .format(player2_value,player2_suit))

    if player1_value > player2_value:
        print ("Player 1 wins!")
    elif player1_value < player2_value:
        print ("Player 2 wins!")

