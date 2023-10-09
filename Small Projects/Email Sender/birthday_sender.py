from datetime import date
import mysql.connector
from mysql.connector import Error
import smtplib
import os
import random

host = "localhost"
user = "root"
password = "mypass"
database = "birthdays"
password_email = "email_pass"
my_email = "moradafam2715@gmail.com"
receiver = None


def connection(host_name, user_name, password, dbase):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=password,
            db=dbase
        )
        print("Successful")
    except Error as err:
        print(f"Error:{err}")
    return connection


connection = connection(host, user, password, database)


def read_query(connection, query):
    cursor = connection.cursor()
    results = None
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except Error as err:
        print(f"Error:{err}")


random_letters = []
letters = os.listdir("letter_templates")

for letter in letters:
    with open(f"letter_templates/{letter}") as f:
        file = f.read()
        random_letters.append(file)

now = date.today()
name = read_query(connection, f"""SELECT Name, email FROM Friends_Info WHERE birthdate = "{now}" """)
for birthdate in name:
    person_name, email = birthdate[0], birthdate[1]
    letter = random.choice(random_letters)
    true_letter = letter.replace("[NAME]", person_name)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password_email)
        connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"Subject:Birthday Wisher.\n\n{true_letter}")
