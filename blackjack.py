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
    total = 0
    player.append(playingdeck.pop(0))
    dealer.append(playingdeck.pop(0))
    print("Dealing first card..")
    #time.sleep(1)
    print("Dealing first card....")
    #time.sleep(1)
    #print(f"Dealer's Cards : {dealer}")
    print(f"Your Cards : {player}")
    player.append(playingdeck.pop(0))
    dealer.append(playingdeck.pop(0))
    print("Dealing second card..")
    #time.sleep(1)
    #print("Dealing second card....")
    time.sleep(1)
    #print(f"Dealer's Cards : {dealer}")
    #Testing function
    #player = ["10-Diamond", "Ace-Spade"]
    print(f"Your Cards : {player}")
    #Sum for total amount
    laserace = 0
    laserblackjack = 0
    for i, card in enumerate(player):
        try:
            left = int(card.split("-")[0])
            total = total + left
            if left == 10:
                laserblackjack = 1
        except ValueError:
            leftlaser = str(card.split("-")[0])
            if leftlaser in {"Jack", "Queen", "King"}:
                leftlaser = 10
                total = total + leftlaser
                laserblackjack = 1
            elif leftlaser == "Ace":
                leftlaser = 11
                total = total + leftlaser
                laserace = laserace + 1
    if laserblackjack == laserace and laserblackjack != 0:
        print("BLACKJACK! YOU WIN x2")
    if laserace == 2:
        print("BAN BAN! YOU WIN x3")
    print(f"Your total number is : {total}")
    return dealer, player, playingdeck

def playerhit (playingdeck, player):
    total = 0
    player.append(playingdeck.pop(0))
    print(f"Your Cards: {player}")
    for i, card in enumerate(player):
        try:
            left = int(card.split("-")[0])
            total = total + left
        except ValueError:
            leftlaser = str(card.split("-")[0])
            if leftlaser in {"Jack", "Queen", "King"}:
                leftlaser = 10
                total = total + leftlaser
            elif leftlaser == "Ace":
                leftlaser = 11
                total = total + leftlaser
    print(f"Your total number is : {total}")
    return playingdeck, player, total


def main():
    deckofcards = cardsindeck()
    shuffleddeck = shuffle(deckofcards)
    print(shuffleddeck)
    while True:
        choice = input("Do you want to play some BlackJack? yes or no: ").strip().casefold()
        if choice == "yes":
            print("You chose yes. Get ready for some fun")
            dealer, player, playingdeck = initialcardssingleplayer(shuffleddeck)
            print(f"Remaining Card Count in deck = {len(playingdeck)}")
            hitorstand = str(input("Do you want to hit or stand? h for hit, s for stand: "))
            if hitorstand == "h": 
                    playingdeck, player, total = playerhit(playingdeck, player)
                    if total > 21:
                        print("BUST! YOU LOST!")
                        hitorstand = "null"
                        break
                    elif total < 21:
                        while total <= 21:
                            hitorstand = str(input("Do you want to hit or stand? h for hit, s for stand: "))
                            playingdeck, player, total = playerhit(playingdeck, player)
                            if total > 21: 
                                print("BUST! YOU LOST!")
                                break
                    #while total <= 21:
                     #   if total <= 21:
                      #      hitorstand = str(input("Do you want to hit or stand? h for hit, s for stand: "))
                       #     while hitorstand == "h":
                        #        playingdeck, player, total = playerhit(playingdeck, player)
                         #       print(f"Remaining Card Count in deck = {len(playingdeck)}")
                          #      if total > 21:
                           #         print("BUST! YOU LOST!")
                            #        hitorstand = "null"
                             #       break    
                        break                  
            else:
                break
            print(f"Remaining Card Count in deck = {len(playingdeck)}")
            deckofcards = cardsindeck()
            shuffleddeck = shuffle(deckofcards)
            print(shuffleddeck)
        if choice == "no":
            print("Have a great day quitter :)")
            break
        else:
            print("Please input only either yes or no")
    
if __name__ == "__main__":
    main()




        
