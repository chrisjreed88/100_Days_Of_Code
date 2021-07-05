## Sending Email with Python
import smtplib
import datetime as dt
from random import choice

now = dt.datetime.now()
weekday = now.weekday()

my_email = "myemail@gmail.com"
password = "mypassword"

with open("quotes.txt") as f:
    quotes = f.readlines()

if weekday == 5:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Quote Of The Day\n\n{choice(quotes)}"
    )


## Working with date and time in Python
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
# print(date_of_birth)