from data import resources, MENU

def genearte_report( money : float ) -> None:
	'''
		Generates report of resources
	'''
	print()
	for resource, quantity in resources.items():
		if resource == 'coffee':
			print(f"{resource.title()}: {quantity} gm")
		else:
			print(f"{resource}: {quantity} ml")

	print(f"Money: ${money}\n")


def check_resource_availability( coffee : str ) -> str:
	'''
		check if resources are enough for required coffee
	'''
	
	for ingredient, quantity in MENU[coffee]['ingredients'].items():
		if quantity > resources[ingredient]:
			return ingredient
	return 'yes'


def deduct_resources( coffee : str ) -> None:
	'''
		deduct resources as per coffee made
	'''
	for ingredient, quantity in MENU[coffee]['ingredients'].items():
		resources[ingredient] -= quantity


# main
money = 0.0
print("\nEnter below 'Report' to generate report and 'off' to switch off the machine\n")
while(True):

	choice = input("What would you like? espresso/ latte/ cappuccino: ").lower()

	if choice == 'report':
		genearte_report(money)
		continue

	elif choice == 'off':
		print("Bye :)")
		break
	
	elif choice not in MENU:
		print("Valid choice not entered")
		continue 

	available = check_resource_availability(choice)
	if available != 'yes' :
		# resources for the demanded coffee are not available
		print(f"\nSorry, there is not enough {available} in the machine\n")
		continue

	print("\nPlease insert coins.")
	quarters = int(input("how many quarters? "))
	dimes = int(input("how many dimes? "))
	nickels = int(input("how many nickels? "))
	pennies = int(input("how many pennies? "))

	# converting coin values to dollars
	cash = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
	
	# check if given cash is enough
	if MENU[choice]['cost'] > cash:
		# cash is not enough to purchase
		# refund amount
		print(f"\nSorry, that's not enough money. {choice} will cost you ${float(MENU[choice]['cost'])}")
		print("Here is your ${0:.2f} refund.\n".format(cash))
		continue

	deduct_resources(choice)
	money += MENU[choice]['cost']
	print("\nHere is ${0:.2f} in change.".format(cash - MENU[choice]['cost']))
	print(f"Here is your {choice} ☕. Enjoy!\n")	
