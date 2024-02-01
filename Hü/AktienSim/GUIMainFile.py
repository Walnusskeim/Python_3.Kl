##################################################
#                    Imports                     #
##################################################

import tkinter
import time

import customtkinter
import pyautogui

##################################################
#                     Code                       #
##################################################

ctk = customtkinter

root = ctk.CTk()
root.geometry("1920x1080")
ctk.set_appearance_mode("light")


UserLabel = ctk.CTkLabel(root, text = "Username", fg_color = "transparent", bg_color="#EBEBEB", font = ("Futura", 40, "bold"))
UserLabel.place(x = 1700, y = 20)

Title = ctk.CTkLabel(root, text = "Ballin' Aktien Sim!", fg_color = "transparent", bg_color="#EBEBEB", font = ("Futura", 70, "bold"))
Title.place(x = 960, y = 350, anchor = "center")

MoneyLabel = ctk.CTkLabel(root, text = "Available Money", fg_color = "transparent", bg_color="#EBEBEB", font = ("Futura", 40, "bold"))
MoneyLabel.place(x = 60, y = 20)

StartTradinButton = ctk.CTkButton(root, text = "Start Tradin'!", fg_color = "green", bg_color="#EBEBEB", border_width=2, font = ("Futura", 40, "bold"))
StartTradinButton.place(x = 960, y = 700, anchor = "center")

WaitWeekButton = ctk.CTkButton(root, text = "Wait a Week", fg_color = "#860808", bg_color="#EBEBEB", border_width=2, font = ("Futura", 35, "bold"))
WaitWeekButton.place(x = 960, y = 800, anchor = "center")

MyDepotButton = ctk.CTkButton(root, text = "My Depot", fg_color = "#860808", bg_color="#EBEBEB", border_width=2, font = ("Futura", 40, "bold"))
MyDepotButton.place(x = 500, y = 700, anchor = "center")

MarketButton = ctk.CTkButton(root, text = "Market", fg_color = "#860808", bg_color="#EBEBEB", border_width=2, font = ("Futura", 30, "bold"))
MarketButton.place(x = 1400, y = 700, anchor = "center")

LogOutButton = ctk.CTkButton(root, text = "Log Out", fg_color = "#860808", bg_color="#EBEBEB", border_width=2, font = ("Futura", 15, "bold"))
LogOutButton.place(x = 95, y = 1020, anchor = "center")


root.mainloop()