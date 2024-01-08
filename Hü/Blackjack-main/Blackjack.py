"""
A simple Blackjack game with a GUI from CustomTKinter which is not quite finished.
Maximilian
❤
08.01.2024
"""


##################################################
#                    Imports                     #
##################################################

import os
import re
import time
import random

import pyautogui
import customtkinter as ctk
from PIL import Image, ImageTk
import mysql.connector as mariadb


##################################################
#                     Code                       #
##################################################

logwindow = ctk.CTk()
logwindow.geometry("500x250")

creds = ("")


def login():
    global creds
    creds = username.get()
    print(creds)
    logwindow.destroy()


def highscoreshow():
    hiscrwindow = ctk.CTk()
    hiscrwindow.geometry("727x250")
    
    frame = ctk.CTkFrame(master = hiscrwindow)
    frame.pack(pady = 20, padx = 60, fill = "both", expand = True)
    
    header = ctk.CTkLabel(master = frame,
                          text = "Wer ist zu Zeit auf der Spitze?",
                          font = ("Roboto", 20, "bold"))
    header.pack(pady = 12, padx = 10)
    
    text = ctk.CTkLabel(master = frame,
                        text = "Keine Ahung wie bzw. keine Zeit mehr zu implementieren.\n"
                        "Entschuldigung.",
                        font = ("Roboto", 15, "bold"))
    text.pack(pady = 14, padx = 12)


def database_setup():  # Connecting to the Database
    global mydb
    global mycursor
    mydb = mariadb.connect(
        host = "localhost", user = "maxi", password = "mako")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS BlackjackData;")
    mycursor.execute("USE BlackjackData;")
    mycursor.execute("CREATE TABLE IF NOT EXISTS Users (Username VARCHAR(20) PRIMARY KEY, Wins INT, Losses INT);")
    

frame = ctk.CTkFrame(master = logwindow)
frame.pack(pady = 20, padx = 60, fill = "both", expand = True)

label = ctk.CTkLabel(master = frame, text = "Login mit einem Username!",
                    font = ("Roboto", 20, "bold"))
label.pack(pady = 12, padx = 10)

UsernameVar = ctk.StringVar()
username = ctk.CTkEntry(master = frame, textvariable = UsernameVar)
username.pack(pady = 12, padx = 10)

logbutton = ctk.CTkButton(master = frame, text = "Login", fg_color = "green",
                          hover_color = "dark green", command = login)
logbutton.pack(pady = 12, padx = 10)

hiscrbutton = ctk.CTkButton(master = frame, text = "Hiscores",
                            fg_color = "green", hover_color = "dark green",
                            command = highscoreshow)
hiscrbutton.pack(pady = 12, padx = 10)

database_setup()

logwindow.mainloop()


class cards:
    def function(self):
        # Erstellt eine Liste mit allen Karten
        path = "cards"
        self.filelist = []
        for root, dirs, files in os.walk(path):         # Geht durch alle Dateien im Ordner
            for file in files:              # Wenn die Datei CardBack.png ist, wird sie übersprungen
                if file == "CardBack.png":
                    continue
                self.filelist.append(os.path.join(root, file))              # Fügt den Pfad der Datei und das Bild zur Liste hinzu
        return self.filelist


class BlackjackGame(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.width, self.height = pyautogui.size()            # Speichert die Bildschirmgröße in Variablen
        print(self.width, self.height)
        self.delet()

    def delet(self):
        """
        Bei Aufruf dieser Funktion werden alle Variablen auf den Ursprungswert zurückgesetzt
        """
        self.attributes("-fullscreen", True)
        self.bg = ImageTk.PhotoImage(Image.open("design/design1.png").resize(size=(self.width, self.height)))
        self.canvas1 = ctk.CTkCanvas(self)
        self.canvas1.pack(fill="both", expand=True)
        self.canvas1.create_image(0, 0, image=self.bg, anchor="nw")
        self.second_card = None
        self.second_card_counter = 0
        self.player_cards_x = self.width / 2
        self.player_cards_y = 730
        self.coupier_cards_x = self.width / 2
        self.coupier_cards_y = 235
        self.x_change = 20
        self.y_change = 20
        self.value_player = 0
        self.value_coupier = 0
        self.lst = []
        self.filelist = cards().function()
        self.create_widgets()

    def create_widgets(self):
        """
        Erstellen der Texte/Buttons/Karten auf dem Canvas
        """
        self.coupier_text = self.canvas1.create_text(self.width / 2, self.height / 21.6,
                                                     text=f"coupier value: {self.value_coupier}",
                                                     font=('Times New Roman', 20, 'bold'), fill="white")
        self.player_text = self.canvas1.create_text(self.width / 2, self.height / 2,
                                                    text=f"coupier value: {self.value_coupier}",
                                                    font=('Times New Roman', 20, 'bold'), fill="white")
        
        if creds == "":
            self.name_text = self.canvas1.create_text(self.width / 5.45, self.height / 40,
                                                        text="Gast Account | Es werden keine Wins/Losses aufgezeichnet!",
                                                        font=('Times New Roman', 20, 'bold'), fill="white")
        else:
            self.name_text = self.canvas1.create_text(self.width / 20, self.height / 40,
                                                        text=f"{creds}",
                                                        font=('Times New Roman', 20, 'bold'), fill="white")

        self.create_cards("Coupier")
        self.create_cards("Player")
        self.create_cards("Coupier")
        self.create_cards("Player")

        self.Hit = ctk.CTkButton(self.canvas1, text="Hit", height=self.height / 21.6, width=self.width / 9.6,
                                 command=lambda: self.create_cards("Player"), fg_color="#202020", corner_radius=0)

        self.Hit.place(x=self.width / 2 - self.width / 4.8, y=self.height - self.height / 10.8)
        self.Stand = ctk.CTkButton(self.canvas1, text="Stand", height=self.height / 21.6, width=self.width / 9.6,
                                   command=self.stand, fg_color="#202020", corner_radius=0)

        self.Stand.place(x=self.width / 2 - 100, y=self.height - self.height / 10.8)
        self.leave = ctk.CTkButton(self.canvas1, text="Hit and run", height=self.height / 21.6, width=self.width / 9.6,
                                   command=exit, fg_color="#202020", corner_radius=0)

        self.leave.place(x=self.width / 2 + self.width / 4.8 - 200, y=self.height - self.height / 10.8)

    def create_cards(self, player):
        """
        Wenn der Spieler auf Stand drückt, wird diese Funktion aufgerufen
        """
        # Wenn die Liste der Karten leer sein sollte, wird sie hier neu erstellt
        if len(self.filelist) == 0:
            self.filelist = cards().function()
        # Es wird eine zufällige Karte gewählt und aus der Liste entfernt
        self.card = random.choice(self.filelist)
        self.filelist.remove(self.card)
        self.value = int(re.search(r'\d+', self.card).group())  # Mit der "re" Library, kann man einen Integer aus einem String extrahieren

        # Nachdem eine neue Karte gezogen wurde, wird die alte um vorgegebene Koordinaten verschoben
        if player == "Player":
            self.player_cards_x += self.x_change
            self.player_cards_y += self.y_change
            self.x = self.player_cards_x - self.x_change
            self.y = self.player_cards_y - self.y_change
            self.value_player += self.value
            print(f"player value:{self.value_player}")
        # Wenn die Karte für den Croupier gezogen wird, wird sie erstmal verdeckt
        else:
            self.second_card_counter += 1
            if self.second_card_counter == 2:
                self.card = "cards//CardBack.png"
            else:
                self.value_coupier += self.value

            self.coupier_cards_x += self.x_change
            self.coupier_cards_y += self.y_change
            self.x = self.coupier_cards_x - self.x_change
            self.y = self.coupier_cards_y - self.y_change

        self.canvas1.itemconfig(self.coupier_text, text=f"coupier value: {self.value_coupier}")
        self.canvas1.itemconfig(self.player_text, text=f"player value: {self.value_player}")
        self.card = ImageTk.PhotoImage(Image.open(self.card).resize((int(self.width / 9.6), int(self.height / 3.6))))
        self.image = self.canvas1.create_image(self.x, self.y, image=self.card)

        if self.second_card_counter == 2 and player == "Coupier":
            self.hidden_card = self.image   # Speichert das Bild der verdeckten Karte
        self.lst.append(self.card)          # Fixt Error, bei dem das letzte Bild gelöscht wird, wenn neue Karte gezogen wurde

        # Überprüft, ob jemand einen gesamtwert von über 21 hat
        if self.value_player > 21:
            winner = "coupier"
            self.end(winner)
        elif self.value_coupier > 21:
            winner = "player"
            self.end(winner)

        if self.value_player == 21:
            self.stand()

    def stand(self):
        self.coupier_cards_x = self.coupier_cards_x - self.x_change
        self.coupier_cards_y = self.coupier_cards_y - self.y_change
        self.canvas1.delete(self.hidden_card)

        while self.value_coupier < 17:
            self.create_cards("Coupier")

        # Gewinner ermitteln
        if self.value_coupier < self.value_player:
            winner = "player"

        if self.value_coupier > self.value_player:
            winner = "coupier"

        if self.value_coupier == self.value_player:
            winner = "draw"

        if self.value_coupier > 21 or self.value_player > 21:
            return

        self.end(winner)

    def end(self, winner):
        """
        Endbildschirm
        """
        print(f"winner is {winner}")
        
        mycursor.execute("INSERT IGNORE INTO Users(Username,Wins,Losses)VALUE(%s,0,0);",(creds,))
        
        if winner == "draw":
            self.text = "draw"
            x = 625
        else:
            self.text = f"{winner} won!"

        if winner == "player":
            if creds == "":
                pass
            else:
                mycursor.execute("UPDATE Users SET Wins=Wins+1 WHERE Username=%s",(creds,))
                mydb.commit()
            x = 200

        if winner == "coupier":
            if creds == "":
                pass
            else:
                mycursor.execute("UPDATE Users SET Losses=Losses+1 WHERE Username=%s",(creds,))
                mydb.commit()
            x = 125

        self.Hit.configure(command=None)
        self.Stand.configure(command=None)
        self.frame_end = ctk.CTkFrame(self, width=500, height=500)
        self.frame_end.place(x=x, y=300)
        self.label_end = ctk.CTkLabel(self.frame_end, text=self.text, font=('Times New Roman', 300, 'bold'))
        self.label_end.pack()
        self.button_end_restart = ctk.CTkButton(self.frame_end, text="Again?", command=self.close, height=50)
        self.button_end_restart.pack(fill="x")
        self.button_end_end = ctk.CTkButton(self.frame_end, text="End the game", command=exit, height=50)
        self.button_end_end.pack(fill="x")

    def close(self):
        """
        Wenn "Again?" gedrückt wird
        """
        self.canvas1.destroy()
        self.delet()


########################################################################################################################


# Startet das Spiel
game = BlackjackGame()
game.mainloop()
