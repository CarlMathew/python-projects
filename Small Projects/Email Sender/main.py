import smtplib
from datetime import datetime as dt
import random
# with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs=receiver2,
#         msg=""""Subject:Qoute of the Daty.\n\nEither you run the day or the day runs you.
#     - Jim Rohn""")
# now = dt.now()
# print(now)
# year = now.year
# print(year)
# month = now.month
# print(month)
# day_of_the_week = now.weekday()
# print(day_of_the_week)
# date_of_birth = dt(year=2000, month=10, day=27)
# print(date_of_birth)

# with open("quotes.txt") as file:
#     f = file.readlines()
#     list_quotes = [quote.split("\n")[0] for quote in f]
#
# random_quotes = random.choice(list_quotes)
# now = dt.now()
# day_of_week = now.weekday()
# password = "maiyfbblacecxwmz"
# my_email = "moradafam2715@gmail.com"
# receiver = "morada.081446@calamba.sti.edu.ph"
# receiver2 = "moradacarl2711@gmail.com"
# if day_of_week == 0:
#     with smtplib.SMTP("smtp.gmail.com",port = 587) as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(from_addr=my_email,
#                             to_addrs=receiver2,
#                             msg= f"""Subject:Quote of the day.\n{random_quotes}""")

list1 = ["Hatdog", "putlong"]
list1.remove(list1[list1.index("Hatdog")])
print(list1)