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
        print(f"Your Cards : {self.cards}")
        print(f"Your final number is {self.lastnumber}. YOU WIN!!!!")

    def printcards(self):
        print(f"Your Cards : {self.cards}")


class Dealer(Person):
    def __init__(self, Name):
        super().__init__(Name)

    def dealerwin(self):
        print(f"Django's cards : {self.cards}")
        print(f"Django's final number is {self.lastnumber}. YOU LOSE!!!")

    def printcards(self):
        print(f"Django's Cards : {self.cards}")

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
        print(f"Your Cards : {self.player.cards}")
        self.dealing()
        self.dealer.cards.append(self.deck[0])
        self.deck.pop(0)
        #print(self.dealer.cards)
        self.player.cards.append(self.deck[0])
        self.deck.pop(0)
        self.dealing()
        print(self.player.cards)
        self.player.gettotalnumber()
        self.dealer.cards.append(self.deck[0])
        self.deck.pop(0)
        self.dealer.gettotalnumber()
        #print(self.dealer.cards)

    def conclusion(self):
        if self.player.lastnumber == self.dealer.lastnumber:
            self.tie()
            return
        elif self.player.lastnumber > self.dealer.lastnumber:
            self.player.playerwin()
            return
        elif self.player.lastnumber < self.dealer.lastnumber:
            self.dealer.dealerwin()
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
                    self.dealer.printcards()
                    self.dealer.gettotalnumber()
                    self.conclusion()
                    return
                else:
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
        print(f"It's a draw :((((")

    def play_round(self):
        print("Shuffling Deck....")
        self.dealing()
        self.shuffledeck()
        print("Drawing cards")
        self.dealing()
        self.firstdraw()
        if self.player.lastnumber >= 8 and self.player.lastnumber > self.dealer.lastnumber:
            self.player.playerwin()
            return
        if self.dealer.lastnumber >= 8 and self.dealer.lastnumber > self.player.lastnumber:
            self.dealer.dealerwin()
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



