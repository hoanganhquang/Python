import random
from datas import data


def _print(person, a):
    print(f"{a}: {person['name']}, a {person['description']}, from {person['country']}")


compareA = random.choice(data)
_print(compareA, "Compare A")

against = random.choice(data)
_print(against, "Against B")

score = 0
_continue = True
while _continue:
    guess = input("Who has more follower? A or B: ")
    if guess == "A":
        if compareA["follower_count"] > against["follower_count"]:
            score += 1
            print(f"You're right! Current score: {score}")
            _print(compareA, "Compare A")
            against = random.choice(data)
            _print(against, "Against B")
            _continue = True
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            _continue = False
    else:
        if compareA["follower_count"] < against["follower_count"]:
            score += 1
            print(f"You're right! Current score: {score}")
            compareA = against
            _print(compareA, "Compare A")
            against = random.choice(data)
            _print(against, "Against B")
            _continue = True
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            _continue = False
