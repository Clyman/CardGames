import random, math, time

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
            left, suits = card.split("-")

            rankdisplay = cls.RANK_DISPLAY[str(left)]
            suitdisplay = cls.SUIT_SYMBOL[suits]
            top_label = rankdisplay.ljust(2)
            bot_label = rankdisplay.rjust(2)

            ascii_card = f"""+-------+
|{top_label}     |
|   {suitdisplay}   |
|     {bot_label}|
+-------+"""

            ascii_blocks.append(ascii_card.splitlines())

        if not ascii_blocks:
            return

        num_lines = len(ascii_blocks[0])

        for i in range(num_lines):
            row_parts = [block[i] for block in ascii_blocks]
            line = "  ".join(row_parts)
            print(f"{color_prefix}{line}{color_suffix}")

def print_win_banner():
    colors = [
        "\033[91m",
        "\033[93m",
        "\033[92m",
        "\033[96m",
        "\033[94m",
        "\033[95m",
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
    colors = [
        "\033[91m",
        "\033[93m",
        "\033[92m",
        "\033[96m",
        "\033[94m",
        "\033[95m",
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
    colors = [
        "\033[91m",
        "\033[93m",
        "\033[92m",
        "\033[96m",
        "\033[94m",
        "\033[95m",
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
        CardArt.print_side_by_side(self.cards, color="green")
        print(f"\033[92mYour Cards : {self.cards}\033[0m")
        print(f"\033[92mYour final number is {self.lastnumber}\033[0m")

    def printcards(self):
        CardArt.print_side_by_side(self.cards, color="green")
        print(f"\033[92mYour Cards : {self.cards}\033[0m")


class Dealer(Person):
    def __init__(self, Name):
        super().__init__(Name)

    def dealerwin(self):
        CardArt.print_side_by_side(self.cards, color="red")
        print(f"\033[91mDjango's cards : {self.cards}\033[0m")
        print(f"\033[91mDjango's final number is {self.lastnumber}\033[0m")

    def printcards(self):
        CardArt.print_side_by_side(self.cards, color="red")
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
        self.player.printcards()
        self.dealing()
        self.dealer.cards.append(self.deck[0])
        self.deck.pop(0)
        self.player.cards.append(self.deck[0])
        self.deck.pop(0)
        print(f"Drawing Second Card...")
        self.dealing()
        self.player.printcards()
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
            CardArt.print_side_by_side(self.dealer.cards, color="red")
            print(f"\033[91mDealer Django's Final Number is {self.dealer.lastnumber}\033[0m")
            print_win_banner()
            return
        elif self.player.lastnumber < self.dealer.lastnumber:
            self.dealer.dealerwin()
            print(f"Your Final Number is {self.player.lastnumber}")
            print_lose_banner()
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
                    print(f"Dealer Drawing one Card...")
                    dealerlastcard = self.deck[0]
                    self.dealing()
                    self.deck.pop(0)
                    self.dealer.cards.append(dealerlastcard)
                    print(f"Dealer is done drawing and now has 3 cards on hand")
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
                    self.player.gettotalnumber()
                    self.dealer.gettotalnumber()
                    print(f"Opening Cards...")
                    self.dealing()
                    self.conclusion()
                    return
                else:
                    print(f"Opening Cards...")
                    self.dealing()
                    self.conclusion()
                    return
            
            else:
                print(f"Please input only either y or n")


    def dealing(self):
        time.sleep(1.5)

    def tie(self):
        CardArt.print_side_by_side(self.dealer.cards, color="red")
        print(f"Dealer Django's Cards : \033[91m{self.dealer.cards}\033[0m")
        print(f"Your Final Number is {self.player.lastnumber}")
        print(f"\033[91mDealer Django's Final Number is {self.dealer.lastnumber}\033[0m")
        print_draw_banner()

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
