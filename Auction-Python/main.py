import os
from art import logo

# to clear console for next user
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()

auction_record = []

print(logo)
print("Welcome to auction")

run_auction = True
while run_auction:

	bidder = input("What is your name? ")
	bid = int(input("What is your bid? Rs."))

	auction_record.append({'bidder': bidder, 'bid': bid})
	
	choice = input("Are there any other bidder? Type 'Yes' or 'No'.\n")
	if choice.lower() != 'yes':
		run_auction = False
	else:
		cls()

max_bid = 0
winner = ''
for rec in auction_record:

	if rec['bid'] > max_bid:
		max_bid = rec['bid']
		winner = rec['bidder']

cls()
if max_bid == 0:
	print("No bidder found")
else:	
	print(f"The winner is {winner} with a bid of Rs. {max_bid}")
