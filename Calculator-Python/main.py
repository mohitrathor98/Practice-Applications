from art import logo
import os

def cls():
	'''
		Used to clear screen
	'''
	os.system('cls' if os.name=='nt' else 'clear')


def add(first_num, second_num):
	return first_num + second_num

def sub(first_num, second_num):
	return first_num - second_num

def mul(first_num, second_num):
	return first_num * second_num

def div(first_num, second_num):
	if second_num == 0:
		return "Denominator can't be zero"
	return first_num/second_num


def new_calculation():
	'''
		If user starts a new calculation this method
		is called
	'''
	cls()
	print(logo)

	first_num = float(input("What's the first number? "))
	return first_num


operation = {
	'+' : add,
	'-' : sub,
	'*' : mul,
	'/' : div
}

run_calculator = True
choice = 'n'
while run_calculator:
	
	if choice == 'n':
		first_num = new_calculation()
		
	for op in operation:
		print(op)
	
	operator = input("Pick an operation: ")

	second_num = float(input("What's the next number?: "))

	if operator not in operation:
		print("Wrong operator choosed")
		continue

	answer = operation[operator](first_num, second_num)
	if not isinstance(answer, float):
		print(f"ERROR! {answer}")
		break
	
	print(f"{first_num} {operator} {second_num} = {answer}")

	choice = input(f"""Type 'y' to contine calculating with {answer},\
	otherwise type 'n' to start a new calculation and to quit press 'q': \
	""")

	if choice.lower() == 'y':
		first_num = answer
	elif choice.lower() != 'n':
		run_calculator = False