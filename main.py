import smtplib
import datetime as dt
import pandas

my_email = "tabpython0105@gmail.com"
password = "Quangpython123456"

now = dt.datetime.now()
year = now.year
month = now.month
date = now.day
data = pandas.read_csv("birthdays.csv")
data1 = data.to_dict(orient="records")

for row in data1:
    if row["year"] == year and row["month"] == month and row['day'] == date:
        with open("let1.txt", "r") as text:
            text1 = text.read()
            text1 = text1.replace("[NAME]", row["name"])

        with smtplib.SMTP("smtp.gmail.com") as mail:
            mail.starttls()
            mail.login(my_email, password)
            mail.sendmail(from_addr=my_email, to_addrs=my_email,
                          msg=f"Subject: HPBD!\n\n {text1}")
