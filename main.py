import random

cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
cards_ten = ["J", "K", "Q"]
cards_A = ["A"]
cards_A1 = [1, 10]
me = []
bot = []


def deal(arr):
    card = random.choice(cards)
    arr.append(card)
    return arr


def blackjack(arr):
    if ("A" in arr and 10 in arr) or ("A" in arr and "J" in arr) or ("A" in arr and "Q" in arr) or ("A" in arr and "K" in arr):
        print("BlackJack!")


for i in range(1, 3):
    deal(me)
    deal(bot)


bot[1] = "*"
print(f"Your cards: {me}")
print(f"Bot's cards: {bot}")

if blackjack(me):
    _continue = False
else:
    _continue = True

total = 0
for a in me:
    if a in cards_ten:
        a = 10
    elif a in cards_A:
        a = int(input("1 or 10: "))
    total += a


while _continue:
    choice = input("Hit or stand: ").lower()
    if choice == "hit":
        total = 0
        deal(me)
        print(me)
        for a in me:
            if a in cards_ten:
                a = 10
            elif a in cards_A:
                a = int(input("1 or 10: "))
            total += a
        if total > 21:
            print("You lose")
            _continue = False
        else:
            _continue = True
    elif choice == "stand":
        total_bot = 0
        bot[1] = random.choice(cards)
        print(bot)
        for i in bot:
            if i in cards_ten:
                i = 10
            elif i in cards_A:
                i = random.choice(cards_A1)
            total_bot += i

        while total_bot < 17:
            deal(bot)
            total_bot = 0
            for i in bot:
                if i in cards_ten:
                    i = 10
                elif i in cards_A:
                    i = random.choice(cards_A1)
                total_bot += i

        if total_bot > 21:
            print(total_bot)
            print("You win")
            _continue = False
        else:
            print(total)
            print(total_bot)
            if total > total_bot:
                print("You win")
            elif total == total_bot:
                print("Draw")
            else:
                print("Dealer win")
            _continue = False
