from random import randint


##################################################
#                     Classes                    #
##################################################

class Player:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.stocks = {}

class Stock:
    def __init__(self, name, current_value,change):
        self.name = name
        self.current_value = current_value
        self.change = change

    def update_current_value(self):
        cf = randint(0, self.change)
        if randint(0, self.risk) <= (self.risk-1):
            self.current_value = self.current_value + (cf*self.current_value/100)
        else:
            self.current_value = self.current_value - (cf*self.current_value/100)


class HighRiskStock(Stock):
    def __init__(self, name, current_value, change):
        super().__init__(name, current_value, change)
        self.risk = 1
    # if randint(0, self.risk) == 0:
        # self.current_value = self.current_value * 1.5
    # else:
        # self.current_value = self.current_value * -1.5


class MedRiskStock(Stock):
    def __init__(self, name, current_value, change):
        super().__init__(name, current_value, change)
        self.risk = 10
    # if randint(0, 10) <= 4:
        # self.current_value = self.current_value * self.risk * 1.2
    # else:
        # self.current_value = self.current_value * -1.2



class LowRiskStock(Stock):
    def __init__(self, name, current_value, change):
        super().__init__(name, current_value, change)
        self.risk = 50
    # if randint(0, 50) <= 49:
        # self.current_value = self.current_value * self.risk
    # else:
        # self.current_value = self.current_value * -1.1