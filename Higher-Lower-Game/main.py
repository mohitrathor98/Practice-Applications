import random, os

from art import logo, vs
from data import data
 
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

print(logo)

score = 0
while True:

	# picking two instagrammer
	first_pick = random.choice(data)
	second_pick = random.choice(data)

	# making sure two choices are not same
	while second_pick['name'] == first_pick['name']:
		second_pick = random.choice(data)

	print(f"Compare A: {first_pick['name']}, {first_pick['description']}, from {first_pick['country']}")
	print(vs)
	print(f"Against B: {second_pick['name']}, {second_pick['description']}, from {second_pick['country']}")

	choice = input("Who has more followers? Type 'A' or 'B': ").lower()

	# getting correct answer
	if first_pick['follower_count'] > second_pick['follower_count']:
		answer = 'a'
	else:
		answer = 'b'

	cls()
	print(logo)
	# comparing with player's answer
	if choice == answer:
		score += 1
		print(f"You're right! Current score: {score}")
	else:
		print(f"Sorry! That's wrong. Final score: {score}")
		break