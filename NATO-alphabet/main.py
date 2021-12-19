
import pandas

nato_dict = {}
data = pandas.read_csv("nato_phonetic_alphabet.csv")

for (index, row) in data.iterrows():
    nato_dict[row['letter']] = row['code']

while(True):
    try:
        user_name = input("What's the word? ").upper()
        nato_code = [nato_dict[l] for l in user_name]
    except:
        print("Sorry, only alphabets please")
    else:
        break
    
print(nato_code)