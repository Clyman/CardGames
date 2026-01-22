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
        print(self.total)
        self.lastnumber = self.total % 10
        print(self.lastnumber)


class Player(Person):
    def __init__(self, Name):
        super().__init__(Name)

    def playerwin(self):
        print(f"Your final number is {self.player.lastnumber}. YOU WIN!!!!")

class Dealer(Person):
    def __init__(self, Name):
        super().__init__(Name)

    def dealerwin(self):
        print(f"Django's final number is {self.dealer.lastnumber}. YOU LOSE!!!")

class Engine:
    def __init__(self, deck, player, dealer):
        self.deck = deck
        self.player = player
        self.dealer = dealer

    def shuffledeck(self):
        random.shuffle(self.deck)

    def firstdraw(self):
        self.player.cards.append(self.deck[0])
        self.deck.pop(0)
        print(self.player.cards)
        self.dealing()
        self.dealer.cards.append(self.deck[0])
        self.deck.pop(0)
        #print(self.dealer.cards)
        self.player.cards.append(self.deck[0])
        self.deck.pop(0)
        self.dealing()
        print(self.player.cards)
        self.dealer.cards.append(self.deck[0])
        self.deck.pop(0)
        #print(self.dealer.cards)
    

    def drawcard(self):
        while True:
            rubbercard = input(f"Do you want to draw a card? y for yes, n for no")
            if rubbercard == "y":
                self.total = 0
                lastcard = self.deck[0]
                self.deck.pop(0)
                self.cards.append(lastcard)
            
            elif rubbercard == "n":
                return
            else:
                print(f"Please input only either y or n")

    def printcards(self):
        print(self.cards)

    def dealing(self):
        time.sleep(2)


    def play_round(self):
        print("Shuffling Deck....")
        self.dealing()
        self.shuffledeck()
        print("Drawing cards")
        self.dealing()
        self.firstdraw()
        self.player.gettotalnumber()
        self.dealer.gettotalnumber()
        if self.player.lastnumber >= 8 and self.player.lastnumber > self.dealer.lastnumber:
            self.player.playerwin()
        if self.dealer.lastnumber >= 8 and self.dealer.lastnumber > self.player.lastnumber:
            self.dealer.dealerwin()
        if self.player.lastnumber == self.dealer.lastnumber:
            print(f"It's a draw :((((")
        else:
            self.drawcard()



deck = Deck()   
p = Player(input("What is your name?"))
print(f"Welcome {p.Name}, my name is Django, get ready for some Bacarrat")
d = Dealer("Django")
game = Engine(deck.cardlist, p, d)
game.play_round()



