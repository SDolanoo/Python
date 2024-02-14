import smtplib
import random
import datetime as dt
import pandas

my_email = "malytrolll@gmail.com"
password = "password"

data = pandas.read_csv("birthdays.csv")
person_list = data.to_dict(orient='records')

now = dt.datetime.now()
today_month = now.month
today_day = now.day


def send_email(address, month, day, text):
    # function to send email if conditions are met
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        if today_month == month and today_day == day:
            connection.sendmail(from_addr=my_email, to_addrs=f"{address}",
                                msg=f"Subject:Twoje urodziny!!!\n\n{text}")


def read_and_replace_name_in_txt(name):
    number = random.randint(1, 3)
    with open(f'letter_templates/letter_{number}.txt', 'r') as f:
        text_before = f.read()
        text_edited = text_before.replace('[NAME]', f'{name}')

    return text_edited


for person in range(len(person_list)):
    bday_name = person_list[person]['name']
    bday_address = person_list[person]['email']
    bday_month = person_list[person]['month']
    bday_day = person_list[person]['day']
    if bday_month == today_month and bday_day == today_day:
        text_edited = read_and_replace_name_in_txt(bday_name)
        send_email(bday_address, bday_month, bday_day, text_edited)