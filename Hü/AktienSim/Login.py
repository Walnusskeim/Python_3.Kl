import asyncio
import customtkinter as ctk

import Aktien_GUI


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
        print(self.creds)
        self.destroy()
        Aktien_GUI.app = Aktien_GUI.HomeScreen(self.creds, 10000, {})
        Aktien_GUI.app.mainloop()
        return self.creds
