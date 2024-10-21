from art import logo
import random


number = random.randint(1,100)
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.\n")
choice_level = input("Choose a difficulty. Type 'easy' or 'hard':\n").lower()


def game (attempts):
    index_attempt = 1
    game_status = True
    print(f"You have {attempts} attempts remaining to guees the number.")
    guess_number = int(input("Make a guess: "))
    while game_status:
        if guess_number == number:
            print("You win!")
            game_status = False
        elif index_attempt == attempts:
            if guess_number > number:
                print("Too high.")
            else:
                print("Too low.")
            print("You've run out of guesses, You lose!")
            game_status = False
        elif guess_number > number:
            print("Too high.")
            print("Guess again.")
            print(f"You have {attempts - index_attempt} attempts remaining to guess the number.")
            guess_number = int(input("Make a guess: "))
        elif guess_number < number:
            print("Too low.")
            print("Guess again.")
            print(f"You have {attempts - index_attempt} attempts remaining to guess the number.")
            guess_number = int(input("Make a guess: "))
        index_attempt += 1

while choice_level != 'easy' and choice_level != 'hard':
    print("You didn't type the choice correctly.")
    choice_level = input("Choose a difficulty. Type 'easy' or 'hard':\n").lower()

if choice_level == "easy":
    game(10)
elif choice_level == "hard":
    game(5)