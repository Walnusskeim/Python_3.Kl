"""
Big Car Business - A inheritance example
Maximilian
❤
15.01.2024
"""


##################################################
#                     Code                       #
##################################################

class Vehicle:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

    def __str__(self):
        return "This {} costs {}€".format(self.brand, self.price)

    def drive(self):
        print("Driving {}".format(self.brand))

    def price(self):
        return self.price


if __name__ == "__main__":
    myGarage = []
    car1 = Vehicle(10000, "Mercedes")
    car2 = Vehicle(5000, "Toyota")
    myGarage.append(car1)
    myGarage.append(car2)
    for c in myGarage:
        print(c)
        c.drive()
