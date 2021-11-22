from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cypher(text, shift, direction):

	result_text = ''

	for letter in text:

		if not letter.isalpha():
			result_text += letter
			continue

		index = alphabet.index(letter)

		if direction == "encode":

			if (index + shift) < len(alphabet):
				result_text += alphabet[index + shift]
			else:

				index_from_start = (index + shift) - len(alphabet)
				result_text += alphabet[index_from_start]

		elif direction == "decode":
			
			if (index - shift) >= 0:
				result_text += alphabet[index - shift]
			else:

				index_from_end = len(alphabet) + (index - shift)
				result_text += alphabet[index_from_end]

		else:
			print("You have to choose between encode or decode")
			break

	print("Your "+ direction + "d text is: " + result_text)


print(logo)

run = True
while(run):
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))

	if shift >= 26:
		shift %= 26

	cypher(text, shift, direction)

	choice = input("Type 'Yes' if you want to go again. Otherwise type 'No'\n").lower()
	if choice != 'yes':
		run = False