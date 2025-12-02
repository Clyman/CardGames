import random, time

def cardsindeck ():
    deckofcards = []
    suits = ["Diamond", "Clubs", "Hearts", "Spade"]
    ranks = []
    for x in range (1, 11, 1):
        if x == 1:
            x = "Ace"
            ranks = ranks + [x]
        else:
            ranks += [x]
    ranks += ["Jack", "Queen", "King"]
    print(ranks)
    print(suits)
    for x in ranks:
        for y in suits:
            deckofcards = deckofcards + [f"{x}-{y}"]
    print(deckofcards)
    print(len(deckofcards))
    return deckofcards

def shuffle (x):
    random.shuffle(x)
    shuffleddeck = x
    return shuffleddeck

def initialcardssingleplayer (playingdeck):
    dealer = []
    player = []
    player.append(playingdeck.pop(0))
    dealer.append(playingdeck.pop(0))
    print("Dealing first card..")
    time.sleep(1)
    print("Dealing first card....")
    time.sleep(1)
    #print(f"Dealer's Cards : {dealer}")
    print(f"Your Cards : {player}")
    player.append(playingdeck.pop(0))
    dealer.append(playingdeck.pop(0))
    print("Dealing second card..")
    time.sleep(1)
    print("Dealing second card....")
    time.sleep(1)
    #print(f"Dealer's Cards : {dealer}")
    print(f"Your Cards : {player}")
    return dealer, player, playingdeck

def playerhit (playingdeck, player):
    player.append(playingdeck.pop(0))
    print(f"Your Cards: {player}")
    return playingdeck, player


def main():
    deckofcards = cardsindeck()
    shuffleddeck = shuffle(deckofcards)
    print(shuffleddeck)
    #print(input("Do"))
    dealer, player, playingdeck = initialcardssingleplayer(shuffleddeck)
    playingdeck, player = playerhit(playingdeck, player)
    print(len(playingdeck))


if __name__ == "__main__":
    main()




        
