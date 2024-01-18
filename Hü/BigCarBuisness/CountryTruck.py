##################################################
#                    Imports                     #
##################################################

import FourWheelDrive


##################################################
#                     Code                       #
##################################################

class CountryTruck(FourWheelDrive.FourWheelDrive):
    def __int__(self, price, brand):
        super().__init__(price, brand)

    def __str__(self):
        return super().__str__() + \
            f"\n4x4 Trucks are the only thing" \
            f" you will ever need in your life"

    def pullTrailer(self):
        print("Pulling a trailer with the {} " \
              "is so much fun!\n".format(self.brand))

if __name__ == "__main__":
    myGarage = []
    car1 = CountryTruck(52000, "Dodge RAM")
    car2 = CountryTruck(16800, "Nissan Navara")
    myGarage.append(car1)
    myGarage.append(car2)
    for c in myGarage:
        print(c)
        c.pullTrailer()
        c.offRoad()
