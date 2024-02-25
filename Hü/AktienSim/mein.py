"""
A stock simulation with classes
Maximilian
❤
29.01.20
"""


##################################################
#                    Imports                     #
##################################################

import random


##################################################
#                     Code                       #
##################################################

class Player:
    def __init__(self):
        self.money = 3000
        self.depot = {}

    def buy_stock(self, market, stock_name, amount):
        stock = market.get_stock(stock_name)
        if stock and self.money >= amount * stock.current_value:
            self.money -= amount * stock.current_value
            self.depot[stock_name] = self.depot.get(stock_name, 0) + amount
            return True
        return False

    def sell_stock(self, market, stock_name, amount):
        stock = market.get_stock(stock_name)
        if stock and self.depot.get(stock_name, 0) >= amount:
            self.money += amount * stock.current_value
            self.depot[stock_name] -= amount
            return True
        return False

    def view_portfolio(self):
        return self.depot

    def view_stocks(self):
        if self.depot:
            for stock_name, quantity in self.depot.items():
                print(f"You have {quantity} Stocks of {stock_name}.\n")
        else:
            print("You have no stocks.")

    def game_menu(self, market):
        while True:
            print("1. View current values of all stocks")
            print("2. Buy stocks / View current money")
            print("3. Sell stocks")
            print("4. View all stocks you currently have")
            print("5. Wait for a week")
            print("6. Exit game")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                print("\nLRS: Low Risk Stock\nMRS: Medium Risk Stock\nHRS: High Risk Stock\n")
                market.display_stock_values()
                print("\n")
            elif choice == 2:
                print(f"You currently have ${self.money}")
                stock_name = input('Enter the name of the stock you want to buy (type "back" to return back: ')
                if stock_name == "back":
                    continue
                amount = int(input("Enter the amount you want to buy: "))
                print("\n")
                if not self.buy_stock(market, stock_name, amount):
                    print("You do not have enough money to buy this amount of stock.\n")
            elif choice == 3:
                stock_name = input('Enter the name of the stock you want to sell (type "back" to return back): ')
                amount = int(input('Enter the amount you want to sell (type "back" to return back): '))
                if amount == "back":
                    continue
                print("\n")
                if not self.sell_stock(market, stock_name, amount):
                    print("You do not have this amount of stock to sell.\n")
            elif choice == 4:
                self.view_stocks()
                print("\n")
            elif choice == 5:
                market.update_all_stock_values()
            elif choice == 6:
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.\n")

class Stock:
    def __init__(self, name, current_value):
        self.name = name
        self.current_value = current_value

    def update_current_value(self):
        pass

class Low_Risk_Stock(Stock):
    def update_current_value(self):
        self.current_value = round(self.current_value + random.uniform(-10, 10), 2)

class Med_Risk_Stock(Stock):
    def update_current_value(self):
        self.current_value = round(self.current_value + random.uniform(-33, 33), 2)

class High_Risk_Stock(Stock):
    def update_current_value(self):
        self.current_value = round(self.current_value + random.uniform(-50, 50), 2)

class Market:
    def __init__(self, stocks):
        self.stocks = {stock.name: stock for stock in stocks}

    def get_stock(self, stock_name):
        return self.stocks.get(stock_name)

    def display_stock_values(self):
        for stock in self.stocks.values():
            print(f"{stock.name}: {stock.current_value}")

    def update_all_stock_values(self):
        for stock in self.stocks.values():
            stock.update_current_value()
        print("The stock values have been updated for the week.\n")


if __name__ == "__main__":
    stocks = [Low_Risk_Stock("PhillipsFischereiAG (LRS)", 230), Low_Risk_Stock("StableBankingAG (LRS)", 230), Low_Risk_Stock("ReliableUtilitiesAG (LRS)", 230),
              Med_Risk_Stock("MaximalGerüstbauAG (MRS)", 500), Med_Risk_Stock("DynamicTechAG (MRS)", 500), Med_Risk_Stock("ProgressiveAutoAG (MRS)", 500),
              High_Risk_Stock("R&B RechtskanzleiAG (HRS)", 727), High_Risk_Stock("VolatileCryptoAG (HRS)", 727), High_Risk_Stock("RiskyStartUpAG (HRS)", 727)]
    market = Market(stocks)
    player = Player()
    player.game_menu(market)