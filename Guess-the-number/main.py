from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100")

# generating a number between 1 and 100
actual = random.randint(1, 100)

# setting difficulty level
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

attempts = 5
if difficulty.lower() == "easy":
	attempts = 10
	print(f"Difficulty is set to Easy. You have {attempts} attempts")
else:
	print(f"Difficulty is set to Hard. You have {attempts} attempts.")

guessed = 0
while (attempts != 0) and (guessed != actual):
	
	guessed = int(input("Guess a number: "))
	if guessed == actual:
		print(f"You got it. Answer was {actual}")
		continue

	elif guessed > actual:
		print("Too high.\nGuess Again")
	
	else:
		print("Too low.\nGuess Again")
	
	attempts -= 1
	if attempts == 0:
		print(f"You'v run out of guesses. Number was {actual}. You lost.")
	else:
		print(f"You have {attempts} attempts remaining to guess the number")