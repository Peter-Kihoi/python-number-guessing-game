import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

EASY = 10
HARD = 5


def level(difficulty):
    difficulty -= 1
    return difficulty


def game(num):
    the_number = random.randint(1, 100)
    print(f"Pssst, the correct answer is {the_number}")
    game_on = True
    while game_on:
        print(f"You have {num} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        num = level(num)

        if guess > the_number:
            print("Too High")
            print("Guess Again")
        elif guess < the_number:
            print("Too low")
            print("Guess Again")
        if guess == the_number:
            print(f"You got it! The answer was {the_number}")
            game_on = False
        elif num == 0:
            print("You've run out of guesses, you lose")
            game_on = False


if input("Choose a difficulty. Type 'easy' or 'hard': ") == 'hard':
    game(HARD)
else:
    game(EASY)
