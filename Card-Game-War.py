#WAR GAME
from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play.    
    """

    def __init__(self):
        print("Creating a new order deck")
        self.allcards = [ (s,r) for s in SUITE for r in RANKS ]

    def shuffle(self):
        print("Shuffle decks")
        shuffle(self.allcards)

    def split_in_half(self):
        print("Splitting the card in half")
        return (self.allcards[:26], self.allcards[26:])


class Hand:
    """
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. 
    """
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return 'You have {} cards in hand'.format(len(self.cards))

    def __len__(self):
        return len(self.cards)

    def add(self, cards):
        self.cards.extend(cards)

    def remove(self):
        return self.cards.pop(0)

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove()
        print ("{} placed a card: {}".format(self.name, drawn_card))
        return drawn_card

    def remove_war_cards(self):
        return self.hand.cards.pop(0)


    def still_has_card(self):
        return len(self.hand) > 0




######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

# Use the 3 classes along with some logic to play a game of war!
d = Deck()
d.shuffle()
half1, half2 = d.split_in_half()

#Create Players
computer = Player("computer", Hand(half1))
name = raw_input("Please enter your name\n")
user = Player(name, Hand(half2))
print("user: {}".format(half2))

#Set Round count
total_rounds = 0
war_count = 0

#cards on table
table_cards = []

#Lets play
while computer.still_has_card() and user.still_has_card():
    total_rounds += 1


    print("It is time for a new round!")
    print("Here are the current standings: ")
    print(user.name+" count: "+str(len(user.hand.cards)))
    print(computer.name+" count: "+str(len(computer.hand.cards)))
    print("Both players play a card!\n")

    #play cards
    c_card = computer.play_card()
    p_card = user.play_card()

    #add to table_cards
    table_cards.append(c_card)
    table_cards.append(p_card)

    #check War
    if p_card[1] == c_card[1]:
        war_count += 1
        print("We have a match, time for war!")
        print("Each player removes 1 cards 'face down")
        if len(user.hand) == 0 or len(computer.hand) == 0:
            break
        else:
            table_cards.append(user.remove_war_cards())
            table_cards.append(computer.remove_war_cards())

    #check who's card is larger
    else:
        if RANKS.index(p_card[1]) < RANKS.index(c_card[1]):
            print("Computer has the higher card, adding to hand.")
            computer.hand.add(table_cards)
            table_cards = []
        else:
            print(user.name+" has the higher card, adding to hand.")
            user.hand.add(table_cards)
            table_cards = []

#result
if(len(user.hand)  == 0 and len(computer.hand) == 0):
    print("Tie")
elif(len(user.hand) == 0):
    print("Congrat to " + user.name + " win the game")
else:
    print("Congrat to Computer win the game")

print("Great Game, it lasted: "+str(total_rounds))
print("A war occured "+str(war_count)+" times.")
