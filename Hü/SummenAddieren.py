"""
Programm zum Addieren von Zahlen mit einer MySQL-Datenbank
Maximilian
11.12.2023
"""

##################################################
#                    Imports                     #
##################################################

import mysql.connector as mariadb

##################################################
#                     Code                       #
##################################################

# Variables
mydb = None
mycursor = None
numbers = []
username = input("Wie lautet dein Vorname?\n")


# Functions
def database_setup():  # Connecting to the Database
    global mydb
    mydb = mariadb.connect(host="localhost", user="maxi", password="mako")
    global mycursor
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS Zahlensummierer;USE Zahlensummierer")
    mycursor.execute("CREATE TABLE IF NOT EXISTS Users (Name varchar(20), Nummern INT, Summe INT)")


database_setup()

while True:
    try:
        print("Gib eine Zahl ein oder 'end' um rauszugehen.")
        zahl = input()

        if zahl == "end":
            break
        else:
            zahl = int(zahl)
            numbers.append(zahl)

    except ValueError:
        print("Das ist keine Zahl.")


amount = len(numbers)
value = sum(numbers)


data = "INSERT INTO Users (Name, Nummern, Summe) VALUES (%s, %s, %s)"
values = (username, amount, value)

mycursor.execute(data, values)
mydb.commit()

print("Du hast " + str(amount) + " Zahlen eingegeben. Die Summe ist " + str(sum) + ".")
print("Deine Daten wurden in der Datenbank gespeichert.")

mycursor.execute("SELECT * FROM Users")

for x in mycursor:
    print(x)
