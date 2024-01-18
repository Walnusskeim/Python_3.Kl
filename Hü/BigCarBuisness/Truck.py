##################################################
#                    Imports                     #
##################################################

import not_main


##################################################
#                     Code                       #
##################################################

class Truck(not_main.Vehicle):
    def __init__(self, price, brand):
        super().__init__(price, brand)

    def __str__(self):
        return super().__str__() + \
            " and pulling trailers with this car " \
            "is the best thing that can happen in someones life!"

    def pullTrailer(self):
        print("Pulling a trailer with the {} " \
              "is so much fun\n".format(self.brand))


if __name__ == "__main__":
    myGarage = []
    car1 = Truck(10000, "Mercedes")
    car2 = Truck(5000, "Toyota")
    myGarage.append(car1)
    myGarage.append(car2)
    for c in myGarage:
        print(c)
        c.pullTrailer()