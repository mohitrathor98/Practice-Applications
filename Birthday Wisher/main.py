##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] 
# with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import pandas
import datetime as dt
import random

def generate_message(name):
    
    letter = random.choice(['letter_1.txt', 'letter_2.txt', 'letter_3.txt'])
    with open(f"letter_templates/{letter}", 'r') as file:
        message = file.read()
    return message.replace("[NAME]", name)
    
    
def send_mail(record):
    message = generate_message(record['name'])
    print(message)

data = pandas.read_csv("birthdays.csv")
data_list = data.to_dict(orient='records')

now = dt.datetime.now()
for record in data_list:
    if (now.year == int(record['year']) 
        and now.month == int(record['month']) 
        and now.day == int(record['day'])
        ):
        send_mail(record)



