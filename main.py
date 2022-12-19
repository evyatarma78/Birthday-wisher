from datetime import datetime
import smtplib
import pandas
import random

today = datetime.now()
today_tuple = (today.month, today.day)
MY_EMAIL = "your email"
MY_PASSWORD = "your password"

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    #RANDOMLY CHOOSEN A LETTER

    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )


        #EVERY YEAR THE PERSON WILL GET AN EMAIL WITH A LETTER
        #YOU NEED TO RUN THE CODE ON ANY SERVR FO THAT TO HAPPEND



