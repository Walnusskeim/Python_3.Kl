##################################################
#                    Imports                     #
##################################################

import not_main


##################################################
#                     Code                       #
##################################################

class FourWheelDrive(not_main.Vehicle):
    def __init__(self, price, brand):
        super().__init__(price, brand)

    def __str__(self):
        return super().__str__() + \
            " and has the incredible capabilities of a 4x4 vehicle!"

    def offRoad(self):
        print("WOW! Off Road driving is so cool! "
              "It literally changed my life for the better! \n"
              "I can now pay my bills!\n")


if __name__ == "__main__":
    myGarage = []
    car1 = FourWheelDrive(100000, "Jeep")
    car2 = FourWheelDrive(250000, "Mercedes G-Class")
    myGarage.append(car1)
    myGarage.append(car2)
    for car in myGarage:
        print(car)
        car.offRoad()