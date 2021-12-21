import pandas
import datetime as dt
import random
import smtplib

def generate_message(name):
    
    letter = random.choice(['letter_1.txt', 'letter_2.txt', 'letter_3.txt'])
    with open(f"letter_templates/{letter}", 'r') as file:
        message = file.read()
    return message.replace("[NAME]", name)
    
    
def send_mail(record):
    
    message = generate_message(record['name'])
    my_email = "mohitdemo7@gmail.com"
    password = "demopassword"

    with smtplib.SMTP("smtp.gmail.com") as connection:

        connection.starttls() 
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=record['email'], 
            msg=f"Subject:Happy Birthday {record['name']}\n\n{message}"
        )

data = pandas.read_csv("birthdays.csv")
data_list = data.to_dict(orient='records')

now = dt.datetime.now()
for record in data_list:
    if (now.year == int(record['year']) 
        and now.month == int(record['month']) 
        and now.day == int(record['day'])
        ):
        send_mail(record)



