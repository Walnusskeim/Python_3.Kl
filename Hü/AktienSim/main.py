"""
A stock simulation with classes
Maximilian && Phillip
❤
29.01.2024
"""


##################################################
#                    Imports                     #
##################################################

import customtkinter

from classes import Player, Stock, LowRiskStock, MedRiskStock, HighRiskStock


##################################################
#                   Functions                    #
##################################################

def buy_stock(Player,stock,amount):
    if stock.current_value * amount > Player.money:
        print("Hallo stop du hast nicht genug Geld!")
        return
    Player.stocks[stock] = amount
    print(Player.stocks)





##################################################
#                     Code                       #
##################################################

#name= input("What is your name? ")
name= "Testor"
Pl=Player(name,10000)


PhillipsFischereiAG = LowRiskStock("PhillipsFischereiAG", 230, 2)
MGAG = MedRiskStock("MaximalGerüstbauAG", 500, 10)
RuBRechtskanzleiAG = HighRiskStock("R&B RechtskanzleiAG", 727, 50)
print(Pl.money)
buy_stock(Pl,PhillipsFischereiAG,4)
RuBRechtskanzleiAG.update_current_value()
print(RuBRechtskanzleiAG.current_value)