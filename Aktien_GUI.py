
import customtkinter as ctk
from Aktien_Config import Pl, Market as M


##################################################
#                     Code                       #
##################################################


class HomeScreen(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Ballin' Aktien Sim!")
        self.geometry("800x600")
        self.name = Pl.name
        self.money = "Money: " + str(Pl.money) + "€"
        self.stocks = Pl.stocks

        self.conf()
        self.create_widgets()


    def create_widgets(self):
        UserLabel = ctk.CTkLabel(self, text=self.name,
                                 fg_color = "transparent", bg_color = "#EBEBEB",
                                 font = ("Futura", 20, "bold"))

        Title = ctk.CTkLabel(self, text = "Ballin' Aktien Sim!",
                             fg_color = "transparent", bg_color = "#EBEBEB",
                             font = ("Futura", 70, "bold"))

        MoneyLabel = ctk.CTkLabel(self, text = self.money,
                                  fg_color = "transparent", bg_color = "#EBEBEB",
                                  font = ("Futura", 20, "bold"))

        StartTradinButton = ctk.CTkButton(self, text = "Start Tradin'!",
                                          fg_color = "green", bg_color = "#EBEBEB",
                                          border_width = 2, font = ("Futura", 40, "bold"),
                                          command = self.start_trading)

        WaitWeekButton = ctk.CTkButton(self, text = "Wait a Week",
                                       fg_color = "#860808", bg_color = "#EBEBEB",
                                       border_width = 2, font = ("Futura", 35, "bold"),
                                       command = self.wait_week)

        MyDepotButton = ctk.CTkButton(self, text = "My Depot",
                                      fg_color = "#860808", bg_color = "#EBEBEB",
                                      border_width = 2, font = ("Futura", 40, "bold"),
                                      command = self.my_depot)

        MarketButton = ctk.CTkButton(self, text = "Market", fg_color = "#860808", bg_color = "#EBEBEB",
                                     border_width = 2, font=("Futura", 40, "bold"),
                                     command = self.market)

        LogOutButton = ctk.CTkButton(self, text = "Log Out",
                                     fg_color = "#860808", bg_color = "#EBEBEB",
                                     border_width = 2, font = ("Futura", 15, "bold"),
                                     command = self.log_out)

        self.WaitedLabel = ctk.CTkLabel(self, text = "You waited a week!",
                                        fg_color = "transparent", bg_color = "#EBEBEB",
                                        font=("Futura", 20, "bold"))

        UserLabel.grid(row = 0, column = 4, sticky = "ne")
        Title.grid(row = 2, column = 2, sticky = "n")
        MoneyLabel.grid(row = 0, column = 0, sticky = "nw")
        StartTradinButton.grid(row = 4, column = 2)
        WaitWeekButton.grid(row = 5, column = 2, sticky = "s")
        MyDepotButton.grid(row = 4, column = 1, sticky = "w")
        MarketButton.grid(row = 4, column = 3, sticky = "e")
        LogOutButton.grid(row = 7, column = 0, sticky = "sw")


    def conf(self):
        for i in range(5):
            self.columnconfigure(i, weight = 1)
            if i == 2:
                self.rowconfigure(i, weight = 1)
        for i in range(8):
            self.rowconfigure(i, weight = 1)


    def start_trading(self):
        self.destroy()
        TradeScreen().mainloop()


    def wait_week(self):
        self.WaitedLabel.grid(row = 6, column = 2, sticky = "s")
        for st in M:
            st.update_current_value()
        self.after(1000, self.WaitedLabel.grid_forget)


    def my_depot(self):
        self.destroy()
        DepotScreen().mainloop()


    def market(self):
        self.destroy()
        MarketScreen().mainloop()


    def log_out(self):
        self.destroy()
        quit()


class MarketScreen(HomeScreen):
    def __init__(self):
        super().__init__()
        self.title("Marketing")

        self.create_widgets()


    def create_widgets(self):
        self.frame1 = ctk.CTkScrollableFrame(self, bg_color = "#EBEBEB")
        self.frame2 = ctk.CTkFrame(self, bg_color = "#EBEBEB")

        Title = ctk.CTkLabel(self, text = "Trade",
                            fg_color = "transparent", bg_color = "#EBEBEB",
                            font = ("Futura", 70, "bold"))

        BackButton = ctk.CTkButton(self, text = "Back",
                                    fg_color = "#860808", bg_color = "#EBEBEB", border_width = 2,
                                    font = ("Futura", 15, "bold"),
                                    command = self.back)

        for stocks in M:
            ctk.CTkButton(self.frame1, text = stocks.name,
                            fg_color = "transparent", bg_color = "#EBEBEB",
                            font = ("Futura", 20, "bold"),
                            command = lambda stock = stocks: self.stock_info(stock)).pack()


        self.frame1.grid(row = 1, column = 0, sticky = "n")
        self.frame2.grid(row = 1, column = 1, sticky = "n")
        Title.grid(row = 0, column = 1, sticky = "n")
        BackButton.grid(row = 2, column = 0, sticky = "sw")


    def stock_info(self, stock):
        self.frame2.destroy()
        self.frame2 = ctk.CTkFrame(self, bg_color = "#EBEBEB")
        self.frame2.grid(row = 1, column = 1, sticky = "n")

        NameLabel = ctk.CTkLabel(self.frame2, text = stock.name,
                                fg_color = "transparent", bg_color = "#EBEBEB",
                                font = ("Futura", 40, "bold"))

        ValueLabel = ctk.CTkLabel(self.frame2, text = "Value: " + str(stock.current_value),
                                fg_color = "transparent", bg_color = "#EBEBEB",
                                font = ("Futura", 20, "bold"))

        DescriptionLabel = ctk.CTkLabel(self.frame2, text = stock.desc,
                                    fg_color = "transparent", bg_color = "#EBEBEB",
                                    font = ("Futura", 20, "bold"))

        NameLabel.grid(row = 0, column = 0, sticky = "n")
        ValueLabel.grid(row = 1, column = 0, sticky = "n")
        DescriptionLabel.grid(row = 2, column = 0, sticky = "n")


    def back(self):
        self.destroy()
        Home = HomeScreen()
        Home.mainloop()


class TradeScreen(MarketScreen):
    def __init__(self):
        super().__init__()
        self.title("Tradin up!")

        self.create_widgets()


    def create_widgets(self):
        super().create_widgets()


    def stock_info(self, stock):
        self.frame2.destroy()
        self.frame2 = ctk.CTkFrame(self, bg_color = "#EBEBEB")
        self.frame2.grid(row = 1, column = 1, sticky = "n")

        NameLabel = ctk.CTkLabel(self.frame2, text = stock.name,
                                fg_color = "transparent", bg_color = "#EBEBEB",
                             font = ("Futura", 40, "bold"))

        ValueLabel = ctk.CTkLabel(self.frame2, text = "Value: " + str(stock.current_value),
                                fg_color = "transparent", bg_color = "#EBEBEB",
                                font = ("Futura", 20, "bold"))

        BuyButton = ctk.CTkButton(self.frame2, text = "Buy",
                                fg_color = "#860808", bg_color = "#EBEBEB",
                                border_width = 2, font = ("Futura", 15, "bold"),
                                command = self.buy_stock(stock))

        NameLabel.grid(row = 0, column = 0, sticky = "n")
        ValueLabel.grid(row = 1, column = 0, sticky = "n")
        BuyButton.grid(row = 2, column = 0, sticky = "n")


    def buy_stock(self, stock):
        def buy():
            amount = int(self.amount_entry.get())
            if stock.current_value * amount > Pl.money:
                print("Dafür hast du nicht genug Geld!")
                return

            Pl.stocks[stock] = amount + Pl.stocks.get(stock, 0)
            Pl.stocks_value[stock] = stock.current_value
            Pl.money -= stock.current_value * amount
            print(Pl.stocks)
            print(Pl.money)
        self.amount_entry = ctk.CTkEntry(self.frame2, width = 200)
        self.amount_entry.grid(row = 3, column = 0, sticky = "n")

        self.buybutton = ctk.CTkButton(self.frame2, text = "Buy",
                                        fg_color = "green", bg_color = "#EBEBEB",
                                        border_width = 2, font=("Futura", 15, "bold"),
                                        command = buy)

        self.buybutton.grid(row = 4, column = 0, sticky = "n")


    def back(self):
        self.destroy()
        Home = HomeScreen()
        Home.mainloop()


class DepotScreen(MarketScreen):
    def __init__(self):
        super().__init__()
        self.title("Marketing")

        self.create_widgets()


    def create_widgets(self):
        self.frame1 = ctk.CTkScrollableFrame(self, bg_color = "#EBEBEB")
        self.frame2 = ctk.CTkFrame(self, bg_color = "#EBEBEB")


        Title = ctk.CTkLabel(self, text = "Trade",
                            fg_color = "transparent", bg_color = "#EBEBEB",
                            font = ("Futura", 70, "bold"))
        BackButton = ctk.CTkButton(self, text = "Back",
                                    fg_color = "#860808", bg_color = "#EBEBEB",
                                    border_width = 2, font = ("Futura", 15, "bold"),
                                    command = self.back)

        for stocks in Pl.stocks:
            ctk.CTkButton(self.frame1, text = stocks.name,
                            fg_color = "blue", bg_color = "#EBEBEB",
                            font = ("Futura", 20, "bold"),
                            command = lambda stock=stocks: self.stock_info(stock)).pack()

        self.frame1.grid(row = 1, column = 0, sticky = "n")
        self.frame2.grid(row = 1, column = 1, sticky = "n")
        Title.grid(row = 0, column = 1, sticky = "n")
        BackButton.grid(row = 2, column = 0, sticky = "sw")


    def stock_info(self, stock):
        self.frame2.destroy()
        self.frame2 = ctk.CTkFrame(self, bg_color = "#EBEBEB")
        self.frame2.grid(row = 1, column = 1, sticky = "n")

        NameLabel = ctk.CTkLabel(self.frame2, text = stock.name,
                                fg_color = "transparent", bg_color = "#EBEBEB",
                                font = ("Futura", 40, "bold"))

        DescriptionLabel = ctk.CTkLabel(self.frame2, text = stock.desc,
                                        fg_color = "transparent", bg_color = "#EBEBEB",
                                        font = ("Futura", 20, "bold"))

        ValueLabel = ctk.CTkLabel(self.frame2, text = "Current Value: " + str(stock.current_value)
                                    + "€\nBought for: " + str(Pl.stocks_value[stock])
                                    + "€\nAmount: " + str(Pl.stocks[stock]) + "\nTotal Value: "
                                    + str(Pl.stocks[stock] * stock.current_value) + "€",
                                    fg_color = "transparent", bg_color = "#EBEBEB",
                                    font = ("Futura", 20, "bold"))

        NameLabel.grid(row = 0, column = 0, sticky = "n")
        DescriptionLabel.grid(row = 1, column = 0, sticky = "n")
        ValueLabel.grid(row = 2, column = 0, sticky = "n")


    def back(self):
        self.destroy()
        Home = HomeScreen()
        Home.mainloop()

class Loginwindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.creds = ""
        self.UsernameVar = ctk.StringVar()
        self.title("Login made easy by M&P!")
        self.geometry("500x250")
        self.create_widgets()

    def create_widgets(self):
        self.label = ctk.CTkLabel(master = self,
                                  text = "Login mit einem Username!",
                                  font = ("Roboto", 20, "bold"))
        self.label.pack(pady = 12, padx = 10)

        self.username_entry = ctk.CTkEntry(master = self,
                                           width = 200,
                                           textvariable = self.UsernameVar)
        self.username_entry.pack(pady = 12, padx = 18)

        self.logbutton = ctk.CTkButton(master = self,
                                       text = "Login", fg_color = "green",
                                       hover_color = "dark green",
                                       command = self.login)
        self.logbutton.pack(pady = 12, padx = 18)

    def login(self):
        self.creds = self.username_entry.get()
        self.destroy()
        self.quit()


app = HomeScreen()
