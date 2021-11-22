import random
from hangman_art import stages, logo
from hangman_words import word_list

print()
print(logo)

# choose word randomly
word = random.choice(word_list)
user_word = []

# user_word is word which user will keep on guessing
for i in word:
    user_word.append('_')

strikes = 0
hit = 0
choosed_letters = []

while strikes != 6 and hit != len(word):
    
    user_choice = input("Guess a letter: ").lower()
    if user_choice in choosed_letters:
        print("You have already choosen "+ user_choice + " . Please choose again.")
        continue
    choosed_letters.append(user_choice)
    
    # wrong guess
    if user_choice not in word: 
    
        strikes+=1
        print("Letter "+ user_choice + " is a wrong choice. You have received a strike.")
        if hit != 0:
            print(' '.join(user_word))
        # print stages pattern
        print(stages[len(stages) - strikes - 1])
        continue
    
    # right guess
    hit+=1
    for i in range(len(word)):
        # replacing blanks in user_word with correcly guessed letter
        if word[i] == user_choice:
            user_word[i] = word[i]

    print("You got this letter right!")
    print(' '.join(user_word))

    # print stages pattern
    print(stages[len(stages) - strikes - 1])


if ''.join(user_word) == word:
    print("You Won!")
else:
    print("You used up all the strikes. You are dead!")
