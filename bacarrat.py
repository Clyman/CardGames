import random, math, time

class Deck:
    def __init__(self):
        self.cardlist = []
        ranks = ["Ace", "Jack", "Queen", "King"]
        suits = ["Diamond", "Clubs", "Hearts", "Spades"]
        for i in range (2, 11):
            for s in suits:
                card = f"{i}-{s}"
                self.cardlist.append(card)
        for r in ranks:
            for s in suits:
                card = f"{r}-{s}"
                self.cardlist.append(card)

class Person:
    def __init__(self, Name):
        self.Name = Name
        self.cards = []
        self.total = 0
        self.lastnumber = 0

    def gettotalnumber(self):
        self.total = 0
        for card in self.cards:
            try:
                left = int(card.split("-")[0])
                self.total = self.total + left
            except ValueError:
                left = str(card.split("-")[0])
                if left in {"Jack", "Queen", "King"}:
                    self.total = self.total + 10
                if left == "Ace":
                    self.total = self.total + 1
        self.lastnumber = self.total % 10

    def printcards(self):
        print(self.cards)


class Player(Person):
    def __init__(self, Name):
        super().__init__(Name)

    def playerwin(self):
        print(f"\033[92mYour Cards : {self.cards}\033[0m")
        print(f"\033[92mYour final number is {self.lastnumber}\033[0m")

    def printcards(self):
        print(f"\033[92mYour Cards : {self.cards}\033[0m")


class Dealer(Person):
    def __init__(self, Name):
        super().__init__(Name)

    def dealerwin(self):
        print(f"\033[91mDjango's cards : {self.cards}\033[0m")
        print(f"\033[91mDjango's final number is {self.lastnumber}\033[0m")

    def printcards(self):
        print(f"\033[91mDjango's Cards : {self.cards}\033[0m")

class Engine:
    def __init__(self, deck, player, dealer):
        self.deck = deck
        self.player = player
        self.dealer = dealer

    def shuffledeck(self):
        print("Shuffling Deck....")
        random.shuffle(self.deck)
        self.dealing()

    def firstdraw(self):
        print("Drawing cards")
        self.player.cards.append(self.deck[0])
        self.deck.pop(0)
        print(f"\033[92mYour Cards : {self.player.cards}\033[0m")
        self.dealing()
        self.dealer.cards.append(self.deck[0])
        self.deck.pop(0)
        self.player.cards.append(self.deck[0])
        self.deck.pop(0)
        print(f"Drawing Second Card...")
        self.dealing()
        print(f"\033[92m{self.player.cards}\033[0m")
        self.player.gettotalnumber()
        self.dealer.cards.append(self.deck[0])
        self.deck.pop(0)
        self.dealer.gettotalnumber()

    def conclusion(self):
        if self.player.lastnumber == self.dealer.lastnumber:
            self.tie()
            return
        elif self.player.lastnumber > self.dealer.lastnumber:
            self.player.playerwin()
            print(f"Dealer Django's Final Number is {self.dealer.lastnumber}")
            print("YOU WIN!!!")
            return
        elif self.player.lastnumber < self.dealer.lastnumber:
            self.dealer.dealerwin()
            print(f"Your Final Number is {self.player.lastnumber}")
            print("YOU LOSE!!!")
            return
    

    def drawcard(self):
        while True:
            rubbercard = input(f"Do you want to draw a card? y for yes, n for no: ")
            if rubbercard == "y":
                self.player.total = 0
                print("You draw one card.....")
                self.dealing()
                lastcard = self.deck[0]
                self.deck.pop(0)
                self.player.cards.append(lastcard)
                self.player.printcards()
                self.player.gettotalnumber()
                if self.dealer.lastnumber < 5:
                    self.dealer.total = 0
                    dealerlastcard = self.deck[0]
                    self.dealing()
                    self.deck.pop(0)
                    self.dealer.cards.append(dealerlastcard)
                    self.player.printcards()
                    self.player.gettotalnumber()
                    self.dealer.gettotalnumber()
                    decision = input(f"Ready to open Dealer Cards? Press Enter when ready")
                    if decision == "":
                        self.conclusion()
                        return
                else:
                    decision = input(f"Ready to open Dealer Cards? Press Enter when ready")
                    if decision == "":
                        self.conclusion()
                        return
     
            elif rubbercard == "n":
                if self.dealer.lastnumber < 5:
                    self.dealer.total = 0
                    dealerlastcard = self.deck[0]
                    print(f"Dealer Django drawing card....")
                    self.dealing()
                    self.deck.pop(0)
                    self.dealer.cards.append(dealerlastcard)
                    self.player.printcards()
                    self.player.gettotalnumber()
                    self.dealer.printcards()
                    self.dealer.gettotalnumber()
                    self.conclusion()
                    return
                else:
                    self.conclusion()
                    return
            
            else:
                print(f"Please input only either y or n")


    def dealing(self):
        time.sleep(1.5)

    def tie(self):
        print(f"Dealer Django's Cards : \033[91m{self.dealer.cards}\033[0m")
        print(f"Your Final Number is {self.player.lastnumber}")
        print(f"Dealer Django's Final Number is {self.dealer.lastnumber}")
        print(f"It's a draw :((((")

    def play_round(self):
        self.shuffledeck()
        self.dealing()
        self.firstdraw()
        if self.player.lastnumber >= 8 and self.player.lastnumber > self.dealer.lastnumber:
            self.conclusion()
            return
        if self.dealer.lastnumber >= 8 and self.dealer.lastnumber > self.player.lastnumber:
            self.conclusion()
            return
        if self.player.lastnumber >=8 and self.player.lastnumber == self.dealer.lastnumber:
            self.tie()
            return
        else:
            self.drawcard()

        
            
        



deck = Deck()   
p = Player(input("What is your name?"))
d = Dealer("Django")
print(f"Welcome {p.Name}, my name is {d.Name}, get ready for some Bacarrat")
d = Dealer("Django")
game = Engine(deck.cardlist, p, d)
game.play_round()
