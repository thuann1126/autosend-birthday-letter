##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import random
import smtplib
import datetime as dt

import pandas

MY_EMAIL = "anhthuanzw@gmail.com"
MY_PASSWORD = "lukaku20"

data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict()

now = dt.datetime.now()

date_today = (now.month, now.day)

new_dict = {(row["month"], row["day"]): row for key, row in data.iterrows()}


if date_today in new_dict:
    birthday_person = new_dict[date_today]
    file_path = f"./letter_templates/letter_{random.randint(1,3)}.txt"

    with open(file_path) as file:
        content = file.read()
        content.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday \n\n {content}"
        )
else:
    print('none')


# we can check if a key in the dict even when the key does not have value

# for key, value in data_dict.items():
#
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=today_birthday["email"],
#             msg=f"Subject: Happy birthday!! \n\n I wish you have a nice birthday"
#         )




