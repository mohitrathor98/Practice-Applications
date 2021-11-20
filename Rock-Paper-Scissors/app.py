import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choice = {'rock': rock, 'paper': paper, 'scissors': scissors}

play = True
while(play):

	player_choice = input("Choose Rock or Paper or Scissors: ").lower()
	if(player_choice not in choice.keys()):
		break
	print(choice[player_choice])

	computer_choice = random.choice(list(choice.keys()))
	print("Computer chooses\n" + choice[computer_choice])

	if player_choice == 'rock':
		if computer_choice == 'scissors':
			print("You win")
		elif computer_choice == 'paper':
			print("You loose")
		else:
			print("It's a draw")

	elif player_choice == 'paper':
		if computer_choice == 'rock':
			print("You win")
		elif computer_choice == 'scissors':
			print("You loose")
		else:
			print("It's a draw")

	else:
		if computer_choice == 'paper':
			print("You win")
		elif computer_choice == 'rock':
			print("You loose")
		else:
			print("It's a draw")

	choose = input("Play again? Y or N ")
	if choose != 'Y':
		play = False

print("Bye :)")
		