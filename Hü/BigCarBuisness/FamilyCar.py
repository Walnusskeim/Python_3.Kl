##################################################
#                    Imports                     #
##################################################

import not_main


##################################################
#                     Code                       #
##################################################

class FamilyCar(not_main.Vehicle):
    def __init__(self, price, brand, doors):
        super().__init__(price, brand)
        self.doors = doors

    def __str__(self):
        return super().__str__() + " and has {} doors.".format(self.doors)


if __name__ == "__main__":
    myGarage = []
    car1 = FamilyCar(10000, "Mercedes", 5)
    car2 = FamilyCar(5000, "Toyota", 4)
    car3 = FamilyCar(30000, "BMW", 5)
    car4 = FamilyCar(55000, "Tesla", 4)
    myGarage.append(car1)
    myGarage.append(car2)
    myGarage.append(car3)
    myGarage.append(car4)

    for c in myGarage:
        print(c)
