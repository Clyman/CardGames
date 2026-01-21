import random

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
    def shuffle(self):
        random.shuffle(self.cardlist)

class Player:
    def __init__(self, Name, cards):
        self.Name = Name
        self.cards = cards
        
deckofcards = Deck()
print(deckofcards.cardlist)
print(len(deckofcards.cardlist))

deckofcards.shuffle()
print(deckofcards.cardlist)
