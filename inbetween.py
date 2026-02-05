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


class Table:
    def __init__(self):
        self.deck = Deck()
        self.table_cards = []
        self.players = []

    def initialise_players(self):
        while True:
            try:
                self.balance = int(input(f"Please enter the amount each person should have: "))
                break
            except ValueError:
                print(f"Please only input a whole number")
        while True:
            print("Please enter Player Name and type end once done")
            name = str(input(f"Player Name: "))
            if name != "end":
                self.players.append(Person(name, self.balance))
            if name == "end":
                break
            elif name == int or name == float:
                print("Please enter an appropriate value")
                continue
    
    def starting_to_prize_pool(self):
        while True:
            try:
                buy_in = int(input(f"Enter the Buy-In amount for each player: "))
                break
            except ValueError:
                print(f"Please enter only a whole number!!!")
                continue

        no_of_players = len(self.players)
        self.prize_pool = no_of_players * buy_in
        print(f"Total amount in Prize Pool : {self.prize_pool}")

    def print_players(self):
        print(f"Player List for this round of Bacarrat: ")
        for i, name in enumerate(self.players):
            print(f"{self.players[i].name}  ---  Balance : {self.players[i].balance}")

    def next_two_cards(self, deck):
        self.table_cards[0] = deck.card_list[0]
        deck.card_list.pop(0)
        self.table_cards[1] = deck.card_list[0]
        deck.card_list.pop(0)


class Engine:
    def __init__(self, table):
        self.table = table
    
    def play_round(self):
        self.table.deck.populate()
        self.table.deck.shuffle()
        self.table.initialise_players()
        self.table.print_players()
        self.table.starting_to_prize_pool()

table = Table()
game = Engine(table)
game.play_round()