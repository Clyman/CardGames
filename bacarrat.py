import random, math

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
    def __init__(self, Name, cards = []):
        self.Name = Name
        self.cards = cards
        self.total = 0
        self.lastnumber = 0

    def gettotalnumber(self):
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

    def drawcard(self):
        self.total = 0
        lastcard = deckofcards.cardlist[0]
        deckofcards.cardlist.pop(0)
        self.cards.append(lastcard)

    def getlastnumber(self):
        self.lastnumber = self.total % 10


class Player(Person):
    def __init__(self, Name):
        super().__init__(Name)

class Dealer(Person):
    def __init__(self, Name):
        super().__init__(Name)

class Engine:
    def __init__(self, deck, player, dealer):
        self.deck = deck
        self.player = player
        self.dealer = dealer

    def shuffledeck(self):
        random.shuffle(self.deck)

    def firstdraw(self):
        self.player.cards.append(self.deck[0])
        self.deck.cardlist.pop(0)
        self.dealer.cards.append(self.deck[0])
        self.deck.pop(0)

deck = Deck()   
p = Player("Dragoon rider")
d = Dealer("Django")
game = Engine(deck.cardlist, p, d)
game.shuffledeck()
print(game.deck)


