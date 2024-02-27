"""
Inheritance Example 01
Maximilian
❤
15.01.2024
"""

##################################################
#                     Code                       #
##################################################

class Animal:
    def __init__(self, name, rested):
        self.name = name
        self.rested = rested


    def __str__(self):
        return f"This is an animal object with name: " \
               f"{self.name}, rested: {self.rested}!"


    def sleeping(self, hours_slept):
        if hours_slept >= 6:
            self.rested = True


    def running(self, run_time):
        if run_time > 2:
            slef.rested = False


class Mammal(Animal):
    def __init__(self, name, rested, hungry):
        super().__init__(name, rested)
        self.hungry = hungry

    def __str__(self):
        return super().__str__() + \
            f" and it's hunger status is: {self.hungry}!"


if __name__ == "__main__":
    a1 = Animal("Garfield", True)
    a2 = Animal("Dorie", False)
    a2.sleeping(6.5)
    print(a1)
    print(a2)
    m1 = Mammal("Jerry", True, True)
    print(m1)
