import random

class Deck:
    def __init__(self):
        self.card_list = []
        self.Ranks = ["Ace", "Jack", "Queen", "King"]
        self.Suits = ["Diamond", "Clubs", "Hearts", "Spades"]

    def populate(self):
        for i in range(2, 11):
            for s in self.Suits:
                card = f"{i}-{s}"
                self.card_list.append(card)

        for r in self.Ranks:
            for u in self.Suits:
                card = f"{r}-{u}"
                self.card_list.append(card)

    def shuffle(self):
        random.shuffle(self.card_list)

class Person:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.hand = []

    def drawcard(self, deck):
        self.hand[0] = deck.card_list[0]
        deck.card_list.pop(0)

    #def stand(self):

class Table:
    def __init__(self, prize_pool, *args):
        self.prize_pool = prize_pool
        self.table_cards = []
        self.players = []
        for player in args:
            self.players.append(player)

    def print_players(self):
        print(self.players)

    def next_two_cards(self, deck):
        self.table_cards[0] = deck.card_list[0]
        deck.card_list.pop(0)
        self.table_cards[1] = deck.card_list[0]
        deck.card_list.pop(0)


class Engine:
    def __init__(self, deck, table):
        self.deck = deck
        self.table = table
        self.players = []
    
    def play_round(self):
        self.deck.populate()
        self.deck.shuffle()
        self.balance = int(input(f"Please enter the amount each person should have: "))
        while True:
            print("Please enter Player Names and type end once done")
            name = str(input(f"Player Name: "))
            if name != "end":
                players.append(Person(name, balance))
            else:
                break

        


        
        




deck = Deck()
deck.populate()
deck.shuffle()
players = []
balance = int(input(f"Please enter the amount each person should have: "))
while True:
    print("Please enter Player Names and type end once done")
    name = str(input(f"Player Name: "))
    if name != "end":
        players.append(Person(name, balance))
    else:
        break 
    
table = Table(1000, *players)
print(table.players)
print(deck.card_list)
print(len(deck.card_list))