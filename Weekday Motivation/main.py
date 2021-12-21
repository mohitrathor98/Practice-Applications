import datetime as dt
import smtplib
import random

def send_mail(message):
    my_email = "mohitdemo7@gmail.com"
    password = "demopassword"

    with smtplib.SMTP("smtp.gmail.com") as connection:

        connection.starttls() 
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="mohitdemo7@yahoo.com", 
            msg=f"Subject:Weekday Motivation\n\n{message}"
        )



with open("quotes.txt", "r") as file:
    quotes = file.readlines()

current_day = dt.datetime.now().weekday()
if current_day < 5:
    send_mail(random.choice(quotes))