import random

suits = ["Diamond", "Clubs", "Hearts", "Spade"]
ranks = []
for x in range (1, 11, 1):
   if x == 1:
      x = "Ace"
      ranks += [x]
   else:
      ranks += [x]
ranks += ["Jack", "Queen", "King"]

def random_card ():
   cardlist = []
   for x in ranks:
      for y in suits:
         card = f"{x}-{y}"
         cardlist += [card]
   randomcard = random.choice(cardlist)
   print(randomcard)



def random_range():
   cardlist = []
   for x in ranks:
      for y in suits:
         card = f"{x}-{y}"
         cardlist += [card]
   randomrange = random.sample(cardlist, count)
   print(", ".join(randomrange))

while True:
    count = input("How many cards would you like baby?")
    try:
       count = int(count)
       if count == 1:
          random_card()
          break
       if count > 1 and count <= 52:
          random_range()
          break
       else:
          print("Please enter a valid number of cards in a deck: 1 - 52")
    except ValueError:
       print("Please input a number not alphabets")