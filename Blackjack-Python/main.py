import os, random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def cls():
	'''
		Clears console
	'''
	os.system('cls' if os.name=='nt' else 'clear')


def pick_card() -> int:
	'''
		Pick card randomly from deck and return its value
	'''
	return random.choice(cards)


def get_dealer_cards(dealer_cards : list, dealer_sum : int) -> list:
	'''
		check if dealer cards adds up to 17
		if not it adds until sum reaches 17
		returns dealer's deck of cards
	'''
	# check if dealer's card add up to 17
	while dealer_sum < 17:
		# choose card for dealer
		dealer_cards.append(pick_card())
		dealer_sum = sum(dealer_cards)

	return dealer_cards


def display_results(player_cards : list, dealer_cards : list, player_sum : int ,dealer_sum : int ) -> None:
	'''
		processes the final deck and displays final results
	'''
	print()
	print(f"Your final hand: {player_cards}, final score: {player_sum}")
	print(f"\tComputer's final hand: {dealer_cards}, final score: {dealer_sum}")

	# limit exceed check for player
	if player_sum > 21:
		print("You went over. You lose 😭")
	
	elif player_sum == dealer_sum:
		print("Draw 🙃")
	
	# blackjack for player
	elif player_sum == 0:
		print("It's a BlackJack. You win 😁")
	
	# blackjack for opponent
	elif dealer_sum == 0:
		print("Opponent got a blackjack. You lose 😭")

	# player greater than dealer
	elif player_sum > dealer_sum:
		print("You win 😁")
	
	# player less than dealer
	else:
		
		# limit exceed check for dealer
		if dealer_sum <= 21:
			print("You lose 😭")
		else:
			print("Opponent went over. You win 😁")
		

def game_status(player_cards : list, dealer_cards : list, player_sum : int, dealer_sum : int) -> None:
	'''
		displays current status of the game
	'''
	print()
	print(f"Your cards: {player_cards}, current score = {player_sum}")
	print(f"\tComputer's first card: {dealer_cards[0]}")


def end_game(player_cards : list, dealer_cards : list, player_sum : int, dealer_sum : int) -> None:
	'''
		gets dealer card, calculates sum and calls display_results
	'''
	# dealer_sum == 0 is blackjack condition
	if dealer_sum != 0:
		dealer_cards = get_dealer_cards(dealer_cards, dealer_sum)
		dealer_sum = sum(dealer_cards)

	# it is being done in cases where dealer_cards are having ace when
	# we are generating dealer cards above
	while dealer_sum > 21  and (11 in dealer_cards):
		dealer_cards[dealer_cards.index(11)] = 1
		dealer_sum = sum(dealer_cards)

	display_results(player_cards, dealer_cards, player_sum, dealer_sum)


def run_game() -> None:
	'''
		Runs the whole game
	'''

	cls()
	print(logo)

	player_cards = []
	dealer_cards = []

	# pick two cards for player and dealer
	player_cards.append(pick_card())
	player_cards.append(pick_card())
	dealer_cards.append(pick_card())
	dealer_cards.append(pick_card())

	while(True):

		player_sum = sum(player_cards)
		dealer_sum = sum(dealer_cards)
		
		# if ace is present and if sum > 21 replace ace value of 11 with 1
		while player_sum > 21 and (11 in player_cards):
			player_cards[player_cards.index(11)] = 1
			player_sum = sum(player_cards)

		while dealer_sum > 21  and (11 in dealer_cards):
			dealer_cards[dealer_cards.index(11)] = 1
			dealer_sum = sum(dealer_cards)

		# display status
		game_status(player_cards, dealer_cards, player_sum, dealer_sum)
		
		# check for blackjack condition
		if len(player_cards) == 2:
			if player_sum == 21:
				player_sum = 0
			if dealer_sum == 21:
				dealer_sum = 0

		# check for limits and blackjack (sum becomes 0)
		if player_sum >= 21 or dealer_sum > 21 or player_sum == 0 or dealer_sum == 0:
			end_game(player_cards, dealer_cards, player_sum, dealer_sum)
			break

		# ask for another card
		choice = input("Type 'y' to get another card, type 'n' to pass: ")
		if choice.lower() == 'n':
			end_game(player_cards, dealer_cards, player_sum, dealer_sum)
			break

		# pick card for player
		player_cards.append(pick_card())
		

while(True):
	
	print()
	choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
	if choice.lower() == 'n':
		break

	run_game()