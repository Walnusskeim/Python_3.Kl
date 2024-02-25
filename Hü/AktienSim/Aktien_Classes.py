"""
A stock simulation with classes
Maximilian && Phillip
❤
29.01.2024
"""

import random


##################################################
#                     Classes                    #
##################################################

class Player:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.stocks = {}
        self.stocks_value = {}

class Stock:
    def __init__(self, name, current_value, desc = None):
        self.name = name
        self.current_value = current_value
        self.desc = desc


    def update_current_value(self):
        pass

class LowRiskStock(Stock):
    def update_current_value(self):
        self.current_value = round(self.current_value + random.uniform(-10, 10), 2)
        if self.current_value < 0:
            self.current_value = 0


class MedRiskStock(Stock):
    def update_current_value(self):
        self.current_value = round(self.current_value + random.uniform(-33, 33), 2)
        if self.current_value < 0:
            self.current_value = 0


class HighRiskStock(Stock):
    def update_current_value(self):
        self.current_value = round(self.current_value + random.uniform(-50, 50), 2)
        if self.current_value < 0:
            self.current_value = 0
