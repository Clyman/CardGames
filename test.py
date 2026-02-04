cardlist = []
Ranks = ["Ace", "Jack", "Queen", "King"]
Suits = ["Diamond", "Clubs", "Hearts", "Spades"]
for i in range(2, 11):
    for s in Suits:
        card = f"{i}-{s}"
        print(card)