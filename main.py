import random

print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard: ")
result = random.randint(1, 100)


def guess(attempt):
    while attempt > 0:
        print(f"You have {attempt} remaining to guess the number")
        me_guess = int(input("Make a guess: "))
        if me_guess > result:
            print("Too high\n"
                  "Guess again")
            attempt -= 1
        elif me_guess < result:
            print("Too low\n"
                  "Guess again")
            attempt -= 1
        else:
            print("You win")
            break


if level == "easy":
    guess(10)
else:
    guess(5)
