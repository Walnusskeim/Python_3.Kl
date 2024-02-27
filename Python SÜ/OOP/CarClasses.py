"""
First interactions with object-oriented programming in Python.
Maximilian
❤
08.01.2024
"""


##################################################
#                     Code                       #
##################################################

class Car:
    def __init__(self,manu,m,price,y,c,p,d,fuel,usage):
        self.year = y
        self.doors = d
        self.power = p
        self.color = c
        self.manufacturer = manu
        self.model = m
        self.price = price
        self.fuel = fuel
        self.fuelusage = usage


    def drive(self):
        if self.power < 100:
            print("Boring :(")
        elif self.power < 200:
            print("Nice :)")
        else:
            print("Vroooom!")


my_garage = []
car_1 = Car("Mercedes", "C63", 100000, 2022, "frog green", 350, 5)
car_2 = Car("Toyota", "Corolla", 10000, 2010, "family mango", 65, 4)
my_garage.append(car_1)
my_garage.append(car_2)

total_value = 0

for c in my_garage:
    total_value += c.price
    print(f"{c.model}, PS: {c.power}",end=": ")
    c.drive()

print(f"{total_value= }")