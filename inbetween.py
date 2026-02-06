import random

class Deck:
    def __init__(self):
        self.card_list = []
        self.Ranks = ["Ace", "Jack", "Queen", "King"]
        self.Suits = ["Diamond", "Clubs", "Hearts", "Spades"]

    def populate(self):
        self.card_list = []
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
        self.hand = [None]

    def draw_card(self, deck):
        self.hand[0] = deck.card_list[0]
        deck.card_list.pop(0)


class Table:
    def __init__(self):
        self.deck = Deck()
        self.table_cards = [None, None]
        self.players = []
    

    def next_two_cards(self):
        self.table_cards[0] = self.deck.card_list[0]
        self.deck.card_list.pop(0)
        self.table_cards[1] = self.deck.card_list[0]
        self.deck.card_list.pop(0)


class Engine:
    def __init__(self, table):
        self.table = table

    def initialise_players(self):
        while True:
            try:
                self.table.balance = int(input(f"Please enter the amount each person should have: "))
                break
            except ValueError:
                print(f"Please only input a whole number")
        while True:
            print("Please enter Player Name and type end once done")
            name = str(input(f"Player Name: "))
            if name != "end" and name != "":
                self.table.players.append(Person(name, self.table.balance))
            if name == "end":
                break
            elif name == "":
                print("Please enter an appropriate value")
                continue
            elif name == int or name == float:
                print("Please enter an appropriate value")
                continue

    def print_players(self):
        print(f"Player List for this round of Bacarrat: ")
        for i, name in enumerate(self.table.players):
            print(f"{self.table.players[i].name}  ---  Balance : {self.table.players[i].balance}")
        self.print_prize_pool()

    def print_prize_pool(self):
        print(f"The amount in the prize pool is left with {self.table.prize_pool}")

    def starting_to_prize_pool(self):
        while True:
            try:
                buy_in = int(input(f"Enter the Buy-In amount for each player: "))
                break
            except ValueError:
                print(f"Please enter only a whole number!!!")
                continue

        no_of_players = len(self.table.players)
        self.table.prize_pool = no_of_players * buy_in
        for index, name in enumerate(self.table.players):
            self.table.players[index].balance = self.table.players[index].balance - buy_in
        self.print_players()
        print(f"Total amount in Prize Pool : {self.table.prize_pool}")

    def table_two_cards(self):
        confirmation = input(f"Press Enter for next two cards.")
        while True:
            if confirmation == "":
                self.table.next_two_cards()
                print(self.table.table_cards)
                break
            else:
                print("Please only use Enter to continue")
                continue

    def compute_cards(self, index, bet):
        RANK_VALUE = {
            "Ace": 1,
            "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
            "7": 7, "8": 8, "9": 9, "10": 10,
            "Jack": 11, "Queen": 12, "King": 13,
        }
        next_index = (index + 1) % len(self.table.players)
        table_first = RANK_VALUE[self.table.table_cards[0].split("-")[0]]
        table_second = RANK_VALUE[self.table.table_cards[1].split("-")[0]]
        player_first = RANK_VALUE[self.table.players[index].hand[0].split("-")[0]]
        low, high = sorted((table_first, table_second))

        if player_first == low or player_first == high:
            print(f"OHHHHHH {self.table.players[index].name} TIANG TIANG TIANG. PAY DOUBLE %@#$^@!")
            tiang = bet * 2
            self.table.prize_pool = self.table.prize_pool + tiang
            self.table.players[index].balance = self.table.players[index].balance - tiang
            self.print_players()
            print(f"{self.table.players[next_index].name}'s turn")
            
        elif player_first > low and player_first < high:
            print(f"{self.table.players[index].name} WINS!!!")
            self.table.prize_pool = self.table.prize_pool - bet
            self.table.players[index].balance = self.table.players[index].balance + bet 
            self.print_players()
            print(f"{self.table.players[next_index].name}'s turn")
            
        elif player_first < low or player_first > high:
            print(f"{self.table.players[index].name} LOSES!!! PAY UP")
            self.table.prize_pool = self.table.prize_pool + bet
            self.table.players[index].balance = self.table.players[index].balance - bet
            self.print_players()
            print(f"{self.table.players[next_index].name}'s turn")




    def player_turn(self, index):
        print(f"It's {self.table.players[index].name}'s turn")
        self.table_two_cards()
        while True:
            bet = input(f"How much would {self.table.players[index].name} like to bet? Input skip if you want to skip.").strip()
            if bet.lower() == "skip":
                print(f"{self.table.players[index].name} has chosen to skip. On to the next player")
                self.print_players()
                return
            try:
                bet = int(bet)
            except ValueError:
                print(f"Please input either an integer for bet or skip if you want to skip !!!!")
                continue
            if bet <= 0:
                print("Please input a positive whole number for the bet.")
                continue

            double_confirm = input(f"Are you sure you want to bet this amount : {bet}? Enter again for yes n for no").strip().lower()
            if double_confirm == "":
                self.table.players[index].draw_card(self.table.deck)
                print(self.table.players[index].hand)
                self.compute_cards(index, bet)
                return
            if double_confirm == "n":
                print(f"Please input your bet again {self.table.players[index].name}")
                continue
            print("Please type y or n.")
                    
        
    def play_round(self):
        self.table.deck.populate()
        self.table.deck.shuffle()
        print(self.table.deck.card_list)
        self.initialise_players()
        self.starting_to_prize_pool()
        if len(self.table.players) == 0:
            return

        current_index = 0
        del self.table.deck.card_list[:45]
        while True:

            if len(self.table.deck.card_list) >= 3:
                print(self.table.deck.card_list)
                self.player_turn(current_index)
                current_index = (current_index + 1) % len(self.table.players)
            else:
                self.table.deck.populate()
                self.table.deck.shuffle()
                continue

        

table = Table()
game = Engine(table)
game.play_round()
