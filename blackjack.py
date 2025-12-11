import random, time
class CardArt:
    RANK_DISPLAY = {
        "Ace":   "A",
        "2":     "2",
        "3":     "3",
        "4":     "4",
        "5":     "5",
        "6":     "6",
        "7":     "7",
        "8":     "8",
        "9":     "9",
        "10":    "10",
        "Jack":  "J",
        "Queen": "Q",
        "King":  "K",
    }

    SUIT_SYMBOL = {
        "Spades":   "♠",
        "Hearts":   "♥",
        "Clubs":    "♣",
        "Diamond": "♦",
    }

    @classmethod
    def print_side_by_side(cls, cards, color=None):
        # Optional ANSI coloring for the full ASCII card output
        color_prefix = ""
        color_suffix = ""
        if color == "red":
            color_prefix = "\033[31m"
            color_suffix = "\033[0m"
        elif color == "green":
            color_prefix = "\033[32m"
            color_suffix = "\033[0m"
       
        ascii_blocks = []

        for card in cards:
            left, suits = card.split("-")   # <-- here is the "-" split

            rankdisplay = cls.RANK_DISPLAY[str(left)]
            suitdisplay = cls.SUIT_SYMBOL[suits]
            top_label = rankdisplay.ljust(2)
            bot_label = rankdisplay.rjust(2)

            ascii_card = f"""+-------+
|{top_label}     |
|   {suitdisplay}   |
|     {bot_label}|
+-------+"""

            # split into lines for side-by-side printing
            ascii_blocks.append(ascii_card.splitlines())

        if not ascii_blocks:
            return  # nothing to print

        num_lines = len(ascii_blocks[0])

        for i in range(num_lines):
            row_parts = [block[i] for block in ascii_blocks]
            line = "  ".join(row_parts)
            print(f"{color_prefix}{line}{color_suffix}")

def print_win_banner():
    # ANSI color codes for rainbow effect
    colors = [
        "\033[91m",  # red
        "\033[93m",  # yellow
        "\033[92m",  # green
        "\033[96m",  # cyan
        "\033[94m",  # blue
        "\033[95m",  # magenta
    ]
    reset = "\033[0m"

    text = " YOU WIN! "
    rainbow = ""

    for i, ch in enumerate(text):
        if ch == " ":
            rainbow += " "
        else:
            color = colors[i % len(colors)]
            rainbow += color + ch + reset

    print("\n" * 2)
    print("💰" * 28)
    print("💰  🎉🎉🎉   JACKPOT VICTORY!   🎉🎉🎉  💰")
    print("💰" * 28)
    print(r"""
                                       _         
 __   __                     _        | |         
 \ \ / /__  _   _  __      _(_)_ __   | |
  \ V / _ \| | | | \ \ /\ / / | '_ \  | |
   | | (_) | |_| |  \ V  V /| | | | |  _
   |_|\___/ \__,_|   \_/\_/ |_|_| |_| (_)
""")
    print(" " * 10 + rainbow)
    print("\n" + "✨" * 40 + "\n")

def print_lose_banner():
    # ANSI color codes for rainbow effect (for the YOU LOST! line)
    colors = [
        "\033[91m",  # red
        "\033[93m",  # yellow
        "\033[92m",  # green
        "\033[96m",  # cyan
        "\033[94m",  # blue
        "\033[95m",  # magenta
    ]
    reset = "\033[0m"

    text = " YOU LOST! "
    rainbow = ""

    for i, ch in enumerate(text):
        if ch == " ":
            rainbow += " "
        else:
            color = colors[i % len(colors)]
            rainbow += color + ch + reset

    big_ascii = r"""
***********************************************
*   YY   YY   OOOOO    UU   UU                *
*    YY YY   OO   OO   UU   UU                *
*     YYY    OO   OO   UU   UU                *
*      Y     OO   OO   UU   UU                *
*      Y      OOOO      UUUUU                 *
*                                             *
*   LL       OOOOO    SSSSSS   EEEEEEE        *
*   LL      OO   OO  SS        EE             *
*   LL      OO   OO   SSSSS    EEEE           *
*   LL      OO   OO        SS  EE             *
*   LLLLLL   OOOO    SSSSSS   EEEEEEE         *
***********************************************
"""

    print("\n" * 2)
    print("💀" * 28)
    print("💀      💣  DEALER WINS THIS ROUND  💣      💀")
    print("💀" * 28)
    print(big_ascii)
    print(" " * 10 + rainbow)
    print("\n" + "💔" * 40 + "\n")

def print_draw_banner():
    # ANSI color codes for rainbow effect (for the IT'S A DRAW! line)
    colors = [
        "\033[91m",  # red
        "\033[93m",  # yellow
        "\033[92m",  # green
        "\033[96m",  # cyan
        "\033[94m",  # blue
        "\033[95m",  # magenta
    ]
    reset = "\033[0m"

    text = " IT'S A DRAW! "
    rainbow = ""

    for i, ch in enumerate(text):
        if ch == " ":
            rainbow += " "
        else:
            color = colors[i % len(colors)]
            rainbow += color + ch + reset

    big_ascii = r"""
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||                                                            ||
||                        IT'S A DRAW!                        ||
||                    NOBODY WINS THIS ROUND                  ||
||                                                            ||
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
"""

    print("\n" * 2)
    print("🤝" * 28)
    print("🤝     🤝  IT'S A DRAW — NO WINNER  🤝     🤝")
    print("🤝" * 28)
    print(big_ascii)
    print(" " * 10 + rainbow)
    print("\n" + "✨" * 40 + "\n")

def cardsindeck ():
    deckofcards = []
    suits = ["Diamond", "Clubs", "Hearts", "Spades"]
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
    CardArt.print_side_by_side(player)
    print(f"\033[32mYour Cards : {player}\033[0m")
    player.append(playingdeck.pop(0))
    dealer.append(playingdeck.pop(0))
    print("Dealing second card..")
    time.sleep(1)
    print("Dealing second card....")
    time.sleep(1)
    #print(f"Dealer's Cards : {dealer}")
    CardArt.print_side_by_side(player)
    print(f"\033[32mYour Cards: {player}\033[0m")
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
    print(f"Your total number is : \033[32m{total}\033[0m")
    return dealer, player, playingdeck, total

def playerhit (playingdeck, player):
    player.append(playingdeck.pop(0))
    print(f"Drawing one card")
    time.sleep(1)
    print(f"Opening your cards")
    time.sleep(1)
    CardArt.print_side_by_side(player)
    print(f"\033[32mYour Cards: {player}\033[0m")
    print(f"Remaining Card Count in deck = {len(playingdeck)}")
    # Use ace-aware total calculation so soft aces drop to 1 when needed
    _, total = checkandreplaceace(player)
    print(f"Your total number is : \033[32m{total}\033[0m")
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
    time.sleep(1)
    print(f"Dealer opening cards..")
    time.sleep(1)
    print(f"Dealer opening cards....")
    time.sleep(1)
    #print(f"\033[31mDealer's Cards : {dealer}\033[0m")
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
            print(f"Dealer drawing another card..")
            time.sleep(1)
            dealer.append(playingdeck.pop(0))
            print(f"Remaining Card Count in deck = {len(playingdeck)}")
            dealertotal = 0     ###Might have an issue here 
            time.sleep(1)
            print(f"Dealer opening cards...")
            time.sleep(1)
            #print(f"\033[31mDealer's Cards : {dealer}\033[0m")
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
                    
        elif dealertotal > 15 and dealertotal <= 21:
            CardArt.print_side_by_side(dealer, color="red")
            print(f"\033[31mDealer's Cards : {dealer}\033[0m")
            break
        elif dealertotal <= 15:
            print(f"Dealer drawing another card")
            time.sleep(2)
            dealer.append(playingdeck.pop(0))
            print(f"Remaining Card Count in deck = {len(playingdeck)}")
            dealertotal = 0     ###Might have an issue here 
            time.sleep(2)
            #print(f"Dealer opening cards...")
            #print(f"Dealer's Cards : {dealer}")
            #print(f"Dealer draws one card from the deck...")
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
        CardArt.print_side_by_side(dealer, color="red")
        print(f"\033[31mDealer's Cards : {dealer}\033[0m")           
        print(f"Dealer bust with cards \033[31m{dealer}\033[0m and total of \033[31m{dealertotal}\033[0m")
        print_win_banner()
    print(f"Dealers total number is : \033[31m{dealertotal}\033[0m")
    print(f"Your total number is : \033[32m{total}\033[0m")
    return playertotal, dealertotal
    


def main():
    blackjack_banner = r"""
                    ╔══════════════════════════════════════╗
                    ║          WELCOME TO THE              ║
                    ║            CASINO HALL               ║
                    ╚══════════════════════════════════════╝

            ┌─────────┐       ┌─────────┐       ┌─────────┐
            │A        │       │K        │       │Q        │
            │    ♠    │       │    ♥    │       │    ♦    │
            │        A│       │        K│       │        Q│
            └─────────┘       └─────────┘       └─────────┘

    ██████╗ ██╗      █████╗  ██████╗██╗  ██╗     ██╗ █████╗  ██████╗██╗  ██╗
    ██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝     ██║██╔══██╗██╔════╝██║ ██╔╝
    ██████╔╝██║     ███████║██║     █████╔╝      ██║███████║██║     █████╔╝ 
    ██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██   ██║██╔══██║██║     ██╔═██╗ 
    ██████╔╝███████╗██║  ██║╚██████╗██║  ██╗╚█████╔╝██║  ██║╚██████╗██║  ██╗
    ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝

                    ♦  Try to hit 21 without busting!  ♣
                    ♠  Dealer must stand on 16+      ♥
    """

    print(blackjack_banner)

    deckofcards = cardsindeck()
    shuffleddeck = shuffle(deckofcards)
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
                        print_lose_banner()
                        hitorstand = "null"
                      
                    elif total <= 21:
                        while total <= 21:
                            hitorstand = str(input("Do you want to hit or stand? h for hit, s for stand: "))

                            if hitorstand == "h":
                                playingdeck, player, total = playerhit(playingdeck, player)
                                if total > 21: 
                                    #Checking condition for ace within the player hand
                                    print("BUST! YOU LOST!")
                                    print_lose_banner()
                                    break
                            elif hitorstand == "s":
                                print("You chose to stand")
                                playertotal, dealertotal = playerstand(total, dealer, playingdeck)
                                if playertotal > dealertotal:
                                    print_win_banner()
                                elif dealertotal > playertotal and dealertotal <= 21:
                                    print("Sad. You lost")
                                    print_lose_banner()
                                elif playertotal == dealertotal:
                                    print("ITS A DRAW!")
                                    print_draw_banner()
                                break
            elif hitorstand == "s":
                playertotal, dealertotal = playerstand(total, dealer, playingdeck)
                if playertotal > dealertotal:
                    #print(f"\033[31mDealer's Cards : {dealer}\033[0m")
                    #print(f"Dealers total number is : \033[31m{dealertotal}\033[0m")
                    #print("Congratulations, You won!!!")
                    print_win_banner()
                elif dealertotal > playertotal and dealertotal <= 21:
                    #print(f"\033[31mDealer's Cards : {dealer}\033[0m")
                    #print(f"Dealers total number is : \033[31m{dealertotal}\033[0m")
                    print("Sad. You lost")
                    print_lose_banner()
                elif playertotal == dealertotal:
                    #print(f"\033[31mDealer's Cards : {dealer}\033[0m")
                    #print(f"Dealers total number is : \033[31m{dealertotal}\033[0m")
                    print("ITS A DRAW!")
                    print_draw_banner()
            else:
                break
        elif choice == "no":
                print("Have a great day quitter :)")
                break
    
if __name__ == "__main__":
    main()




        
