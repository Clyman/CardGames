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

def print_win_banner_x2():
    colors = [
        "\033[91m",
        "\033[93m",
        "\033[92m",
        "\033[96m",
        "\033[94m",
        "\033[95m",
    ]
    reset = "\033[0m"

    text = " WIN x2! "
    rainbow = ""

    for i, ch in enumerate(text):
        if ch == " ":
            rainbow += " "
        else:
            color = colors[i % len(colors)]
            rainbow += color + ch + reset

    print("\n" * 2)
    print("💰" * 28)
    print("💰   🎉🎉🎉   DOUBLE PAYOUT!   🎉🎉🎉   💰")
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

def print_win_banner_x3():
    colors = [
        "\033[91m",
        "\033[93m",
        "\033[92m",
        "\033[96m",
        "\033[94m",
        "\033[95m",
    ]
    reset = "\033[0m"

    text = " WIN x3! "
    rainbow = ""

    for i, ch in enumerate(text):
        if ch == " ":
            rainbow += " "
        else:
            color = colors[i % len(colors)]
            rainbow += color + ch + reset

    print("\n" * 2)
    print("💰" * 28)
    print("💰   🎉🎉🎉   TRIPLE PAYOUT!   🎉🎉🎉   💰")
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

def print_front_page():
    title = "DJANGO'S BACARRAT SALOON"
    border = "=" * (len(title) + 6)
    cowboy = r'''
            _____
           /_____\
          /_____ _\
          \     /
           \___/
         .-""""-.
        /  .  .  \
       /   (__)   \
       |  \____/  |
        \  /\/\  /
         '.___.'
           /|\
          / | \
         /  |  \
            |
           / \
          /   \
    '''
    colors = [
        "\033[91m",
        "\033[93m",
        "\033[92m",
        "\033[96m",
        "\033[94m",
        "\033[95m",
    ]
    reset = "\033[0m"

    print("\n" * 2)
    print(border)
    print(f"   {title}   ")
    print(border)
    for i, line in enumerate(cowboy.splitlines()):
        if line.strip() == "":
            print(line)
        else:
            color = colors[i % len(colors)]
            print(f"{color}{line}{reset}")
    name = "DJANGO"
    rainbow = ""
    for i, ch in enumerate(name):
        color = colors[i % len(colors)]
        rainbow += color + ch + reset
    print(rainbow)
    print("Dealer: Django")
    print("Press Enter to start the game.")
    input("")

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

    def get_total_number(self):
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

    def print_cards(self):
        print(self.cards)

    def check_three_picture(self):
        if len(self.cards) != 3:
            return False
        for card in self.cards:
                try:
                    int(card.split("-")[0])
                    return False
                except ValueError:
                    continue
        return True
class Player(Person):
    def __init__(self, Name):
        super().__init__(Name)

    def player_win(self):
        CardArt.print_side_by_side(self.cards, color="green")
        print(f"\033[92mYour Cards : {self.cards}\033[0m")
        print(f"\033[92mYour final number is {self.lastnumber}\033[0m")

    def print_cards(self):
        CardArt.print_side_by_side(self.cards, color="green")
        print(f"\033[92mYour Cards : {self.cards}\033[0m")

    def check_times_two(self):
        if len(self.cards) == 2:
            first_suit = str(self.cards[0].split("-")[1])
            second_suit = str(self.cards[1].split("-")[1])
            try:
                first_number = int(self.cards[0].split("-")[0])
            except ValueError:
                first_number = str(self.cards[0].split("-")[0])
            try:
                second_number = int(self.cards[1].split("-")[0])
            except ValueError:
                second_number = str(self.cards[1].split("-")[0])
            
            if first_suit == second_suit or first_number == second_number:
                return True
            else:
                return False

    def check_times_three(self):
        if len(self.cards) == 3:
            first_suit = str(self.cards[0].split("-")[1])
            second_suit = str(self.cards[1].split("-")[1])
            third_suit = str(self.cards[2].split("-")[1])
            try:
                first_number = int(self.cards[0].split("-")[0])
            except ValueError:
                first_number = str(self.cards[0].split("-")[0])
            try:
                second_number = int(self.cards[1].split("-")[0])
            except ValueError:
                second_number = str(self.cards[1].split("-")[0])
            try:
                third_number = int(self.cards[2].split("-")[0]) 
            except ValueError:
                third_number = str(self.cards[2].split("-")[0])
            if first_suit == second_suit == third_suit or first_number == second_number == third_number:
                return True
            else:
                return False
    
            

class Dealer(Person):
    def __init__(self, Name):
        super().__init__(Name)

    def dealer_win(self):
        CardArt.print_side_by_side(self.cards, color="red")
        print(f"\033[91mDjango's cards : {self.cards}\033[0m")
        print(f"\033[91mDjango's final number is {self.lastnumber}\033[0m")

    def print_cards(self):
        CardArt.print_side_by_side(self.cards, color="red")
        print(f"\033[91mDjango's Cards : {self.cards}\033[0m")


    def print_first_with_facedown(self):
        if not self.cards:
            print("Dealer has no cards.")
            return

        left, suits = self.cards[0].split("-")
        rankdisplay = CardArt.RANK_DISPLAY[str(left)]
        suitdisplay = CardArt.SUIT_SYMBOL[suits]
        top_label = rankdisplay.ljust(2)
        bot_label = rankdisplay.rjust(2)

        faceup = [
            "+-------+",
            f"|{top_label}     |",
            f"|   {suitdisplay}   |",
            f"|     {bot_label}|",
            "+-------+",
        ]
        facedown = [
            "+-------+",
            "|░░░░░░░|",
            "|░░░░░░░|",
            "|░░░░░░░|",
            "+-------+",
        ]

        color_prefix = "\033[91m"
        color_suffix = "\033[0m"
        for i in range(len(faceup)):
            print(f"{color_prefix}{faceup[i]}  {facedown[i]}{color_suffix}")

class Engine:
    def __init__(self, deck: Deck, player: Player, dealer: Dealer):
        self.deck = deck
        self.player = player
        self.dealer = dealer

    def shuffle_deck(self):
        print("Shuffling Deck....")
        random.shuffle(self.deck)
        self.dealing()

    def first_draw(self):
        print("Drawing cards")
        self.player.cards.append(self.deck[0])
        self.deck.pop(0)
        self.player.print_cards()
        self.dealing()
        print("Dealer draws cards")
        self.dealer.cards.append(self.deck[0])
        self.deck.pop(0)
        self.dealing()
        self.dealer.print_cards()
        self.player.cards.append(self.deck[0])
        self.deck.pop(0)
        print(f"Drawing Second Card...")
        self.dealing()
        self.player.print_cards()
        self.player.get_total_number()
        self.dealing()
        print("Dealer draws second card")
        self.dealing()
        self.dealer.cards.append(self.deck[0])
        self.deck.pop(0)
        self.dealer.get_total_number()
        if self.dealer.lastnumber not in range (8, 9):
            self.dealer.print_first_with_facedown()
    

    def conclusion(self):
        if len(self.player.cards) == 2:
            if self.player.lastnumber == self.dealer.lastnumber:
                self.tie()
                return
            elif self.player.lastnumber > self.dealer.lastnumber and self.player.check_times_two() == False:
                self.player.player_win()
                CardArt.print_side_by_side(self.dealer.cards, color="red")
                print(f"\033[91mDealer Django's Final Number is {self.dealer.lastnumber}\033[0m")
                print_win_banner()
                return
            elif self.player.lastnumber > self.dealer.lastnumber and self.player.check_times_two() == True:
                self.player.player_win()
                CardArt.print_side_by_side(self.dealer.cards, color="red")
                print(f"\033[91mDealer Django's Final Number is {self.dealer.lastnumber}\033[0m")
                print_win_banner_x2()
                return
            elif self.player.lastnumber < self.dealer.lastnumber:
                self.dealer.dealer_win()
                print(f"Your Final Number is {self.player.lastnumber}")
                print_lose_banner()
                return
        elif len(self.player.cards) == 3 and self.player.check_three_picture() == True and self.dealer.check_three_picture == False:
            self.player.player_win()
            print(''.join((c + ch + '\033[0m') if ch != ' ' else ' ' for i, ch in enumerate("JACKPOT! YOU HAVE 3 PICTURE CARDS") for c in [("\033[91m","\033[93m","\033[92m","\033[96m","\033[94m","\033[95m")[i % 6]]))
            CardArt.print_side_by_side(self.dealer.cards, color="red")
            print(f"\033[91mDealer Django's Final Number is {self.dealer.lastnumber}\033[0m")
            print_win_banner_x3()
        elif len(self.player.cards) == 3 and self.player.check_three_picture() == False and self.dealer.check_three_picture() == True:
            self.dealer.dealer_win()
            print(f"Your Final Number is {self.player.lastnumber}")
            print_lose_banner()
        elif len(self.player.cards) == 3 and self.player.check_three_picture() == False and self.dealer.check_three_picture() == False:
            if self.player.lastnumber == self.dealer.lastnumber:
                self.tie()
                return
            elif self.player.lastnumber > self.dealer.lastnumber and self.player.check_times_three() == True:
                self.player.player_win()
                CardArt.print_side_by_side(self.dealer.cards, color="red")
                print(f"\033[91mDealer Django's Final Number is {self.dealer.lastnumber}\033[0m")
                print_win_banner_x3()
                return
            elif self.player.lastnumber > self.dealer.lastnumber and self.player.check_times_three() == False:
                self.player.player_win()
                CardArt.print_side_by_side(self.dealer.cards, color="red")
                print(f"\033[91mDealer Django's Final Number is {self.dealer.lastnumber}\033[0m")
                print_win_banner()
                return
            elif self.player.lastnumber < self.dealer.lastnumber:
                self.dealer.dealer_win()
                print(f"Your Final Number is {self.player.lastnumber}")
                print_lose_banner()
                return
    

    def draw_card(self):
        while True:
            rubbercard = input(f"Do you want to draw a card? y for yes, n for no: ")
            if rubbercard == "y":
                self.player.total = 0
                print("You draw one card.....")
                self.dealing()
                lastcard = self.deck[0]
                self.deck.pop(0)
                self.player.cards.append(lastcard)
                self.player.print_cards()
                self.player.get_total_number()
                if self.dealer.lastnumber < 5:
                    self.dealer.total = 0
                    print(f"Dealer Drawing one Card...")
                    dealerlastcard = self.deck[0]
                    self.dealing()
                    self.deck.pop(0)
                    self.dealer.cards.append(dealerlastcard)
                    print(f"Dealer is done drawing and now has 3 cards on hand")
                    self.player.get_total_number()
                    self.dealer.get_total_number()
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
                    self.player.get_total_number()
                    self.dealer.get_total_number()
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
        self.shuffle_deck()
        self.dealing()
        self.first_draw()
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
            self.draw_card()

        
            

print_front_page()
deck = Deck()   
p = Player(input("What is your name?"))
d = Dealer("Django")
print(f"Welcome {p.Name}, my name is {d.Name}, get ready for some Bacarrat")
d = Dealer("Django")
game = Engine(deck.cardlist, p, d)
game.play_round()
