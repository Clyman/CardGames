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
    #print(ranks)
    #print(suits)
    for x in ranks:
        for y in suits:
            deckofcards = deckofcards + [f"{x}-{y}"]
    #print(deckofcards)
    #print(len(deckofcards))
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
    time.sleep(1)
    print("Dealing first card....")
    time.sleep(1)
    #print(f"Dealer's Cards : {dealer}")
    print(f"Your Cards : {player}")
    player.append(playingdeck.pop(0))
    dealer.append(playingdeck.pop(0))
    print("Dealing second card..")
    time.sleep(1)
    #print("Dealing second card....")
    time.sleep(1)
    #print(f"Dealer's Cards : {dealer}")
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
    return dealer, player, playingdeck, total

def playerhit (playingdeck, player):
    player.append(playingdeck.pop(0))
    print(f"Drawing one card")
    time.sleep(1)
    print(f"Opening your cards")
    time.sleep(1)
    print(f"Your Cards: {player}")
    # Use ace-aware total calculation so soft aces drop to 1 when needed
    _, total = checkandreplaceace(player)
    print(f"Your total number is : {total}")
    return playingdeck, player, total

#Check if Ace is present if bust function
def checkandreplaceace(player):
    newtotal = 0
    acecount = 0
    for card in player:
        rank = card.split("-")[0]
        if rank == "Ace":
            newtotal += 11
            acecount += 1
        elif rank in {"Jack", "Queen", "King"}:
            newtotal += 10
        else:
            newtotal += int(rank)

    # downgrade Aces from 11 to 1 until we are <= 21
    while newtotal > 21 and acecount:
        newtotal -= 10
        acecount -= 1
    
    return player, newtotal

def playerstand (total, dealer, playingdeck):
    playertotal = total
    dealertotal = 0
    dealer = ['2-Diamond', 'King-Diamond', 'Ace-Spade']
    print(f"Dealer's Cards : {dealer}")
    for i, card in enumerate(dealer):
        try:
            left = int(card.split("-")[0])
            dealertotal = dealertotal + left
        except ValueError:
            leftlaser = str(card.split("-")[0])
            if leftlaser in {"Jack", "Queen", "King"}:
                leftlaser = 10
                dealertotal = dealertotal + leftlaser
            elif leftlaser == "Ace":
                leftlaser = 11
                dealertotal = dealertotal + leftlaser
    while True:
        if dealertotal <= 15:
            print(f"Dealer drawing another card")
            time.sleep(1)
            dealer.append(playingdeck.pop(0))
            print(f"Remaining cards in playing deck = {len(playingdeck)}")
            dealertotal = 0     ###Might have an issue here 
            time.sleep(1)
            print(f"Dealer opening cards...")
            print(f"Dealer's Cards : {dealer}")
            print(f"Dealer draws one card from the deck...")
            time.sleep(1)
            for i, card in enumerate(dealer):
                try:
                    left = int(card.split("-")[0])
                    dealertotal = dealertotal + left
                except ValueError:
                    leftlaser = str(card.split("-")[0])
                    if leftlaser in {"Jack", "Queen", "King"}:
                        leftlaser = 10
                        dealertotal = dealertotal + leftlaser
                    elif leftlaser == "Ace":
                        leftlaser = 11
                        dealertotal = dealertotal + leftlaser
                #Check and replace ace function
        if dealertotal > 21:
                    dealer, dealertotal = checkandreplaceace(dealer)
                    has_ace = any(card.split("-")[0] == "Ace" for card in dealer)
                    if dealertotal <= 15 and has_ace:
                        continue
                    else:
                        break
                    
        elif dealertotal > 15 and dealertotal < 21:
            break
        elif dealertotal <= 15:
            print(f"Dealer drawing another card")
            time.sleep(1)
            dealer.append(playingdeck.pop(0))
            print(f"Remaining cards in playing deck = {len(playingdeck)}")
            dealertotal = 0     ###Might have an issue here 
            time.sleep(1)
            print(f"Dealer opening cards...")
            print(f"Dealer's Cards : {dealer}")
            print(f"Dealer draws one card from the deck...")
            time.sleep(1)
            for i, card in enumerate(dealer):
                try:
                    left = int(card.split("-")[0])
                    dealertotal = dealertotal + left
                except ValueError:
                    leftlaser = str(card.split("-")[0])
                    if leftlaser in {"Jack", "Queen", "King"}:
                        leftlaser = 10
                        dealertotal = dealertotal + leftlaser
                    elif leftlaser == "Ace":
                        leftlaser = 11
                        dealertotal = dealertotal + leftlaser

    if dealertotal > 21:
        #Checking condition for ace within the dealer hand           
        print(f"Dealer bust with cards {dealer} and total of {dealertotal}")
        print(f"YOU WIN!!!")
    print(f"Dealers total number is : {dealertotal}")
    print(f"Your total number is : {total}")
    return playertotal, dealertotal
    


def main():
    deckofcards = cardsindeck()
    shuffleddeck = shuffle(deckofcards)
    #print(shuffleddeck)
    while True:
        choice = input("Do you want to play some BlackJack? yes or no: ").strip().casefold()
        if choice not in {"yes", "no"}:
            print("Please input only yes or no")
        elif choice == "yes":
            deckofcards = cardsindeck()
            shuffleddeck = shuffle(deckofcards)
            #print(shuffleddeck)

            print("You chose yes. Get ready for some fun")
            dealer, player, playingdeck, total = initialcardssingleplayer(shuffleddeck)
            if total == 21:
                print("YOU WIN x2!")
                continue
            elif total == 22:
                print("YOU WIN x3!")
                continue
            print(f"Remaining Card Count in deck = {len(playingdeck)}")
            hitorstand = str(input("Do you want to hit or stand? h for hit, s for stand: "))
            if hitorstand == "h": 
                    playingdeck, player, total = playerhit(playingdeck, player)
                    if total > 21:
                        #Checking condition for ace within the player hand

                        print("BUST! YOU LOST!")
                        print(f"Dealer's cards : {dealer}")
                        hitorstand = "null"
                      
                    elif total <= 21:
                        while total <= 21:
                            hitorstand = str(input("Do you want to hit or stand? h for hit, s for stand: "))

                            if hitorstand == "h":
                                playingdeck, player, total = playerhit(playingdeck, player)
                                if total > 21: 
                                    #Checking condition for ace within the player hand
                                    print("BUST! YOU LOST!")
                                    print(f"Dealer's cards : {dealer}")
                                    break
                            elif hitorstand == "s":
                                print("You chose to stand")
                                playertotal, dealertotal = playerstand(total, dealer, playingdeck)
                                if playertotal > dealertotal:
                                    print("Congratulations, You won!!!")
                                elif dealertotal > playertotal and dealertotal <= 21:
                                    print("Sad. You lost")
                                elif playertotal == dealertotal:
                                    print("ITS A DRAW!")
                                break
            elif hitorstand == "s":
                playertotal, dealertotal = playerstand(total, dealer, playingdeck)
                if playertotal > dealertotal:
                    print("Congratulations, You won!!!")
                elif dealertotal > playertotal and dealertotal <= 21:
                    print(f"Dealer total number : {dealertotal}")
                    print("Sad. You lost")
                elif playertotal == dealertotal:
                    print("ITS A DRAW!")
            else:
                break
        elif choice == "no":
                print("Have a great day quitter :)")
                break
    
if __name__ == "__main__":
    main()




        
