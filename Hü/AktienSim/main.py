"""
A stock simulation with classes
Maximilian && Phillip
❤
29.01.2024
"""


##################################################
#                    Imports                     #
##################################################

import Aktien_GUI
from Aktien_Config import Pl


##################################################
#                     Code                       #
##################################################


def buy_stock(Player, stock, amount):
    if stock.current_value * amount > Player.money:
        print("Hallo stop du hast nicht genug Geld!")
        return
    Player.stocks[stock] = amount + Player.stocks.get(stock, 0)
    Player.money -= stock.current_value * amount
    print(Player.stocks)
    print(Player.money)


Login = Aktien_GUI.Loginwindow()
Login.mainloop()
Pl.name = Login.creds


Aktien_GUI.app = Aktien_GUI.HomeScreen()
Aktien_GUI.app.mainloop()
Aktien_GUI.app = Aktien_GUI.HomeScreen()
Aktien_GUI.app.mainloop()
