"""
A simple programm to download YouTube videos in the highest resolution
Maximilian
❤
27.04.2024
"""


##################################################
#                    Imports                     #
##################################################

from pytube import YouTube
import customtkinter as ctk
from tkinter import StringVar


##################################################
#                     Code                       #
##################################################

def download_video(url, path):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    if path == "":
        stream.download("C:\\YTDownloader")
    else:
        stream.download(path)
    finished_window = ctk.CTk()
    finished_window.title("Download abgeschlossen!")
    finished_window.geometry("200x100")
    finished = ctk.CTkLabel(finished_window, text="Download abgeschlossen!")
    finished.pack()
    finished_window.mainloop()


# Create a window
window = ctk.CTk()
window.title("YouTube Downloader")
window.geometry("500x250")

# Create a StringVar for the URL
url_var = StringVar()
# Create a StringVar for the path
path_var = StringVar()

# Create a label
label = ctk.CTkLabel(window, text="YouTube Downloader", font=("Arial", 20, "bold"))
label.pack(pady=10)

# Create a label for the URL
url_label = ctk.CTkLabel(window, text="URL:", font=("Arial", 12))
url_label.pack(pady=1)

# Create an entry for the URL
url_entry = ctk.CTkEntry(window, placeholder_text="url", width =200, textvariable=url_var)
url_entry.pack(pady=5, padx=10)

# Create a label for the path
path_label = ctk.CTkLabel(window, text='Pfad mit "\\" \n("C:\\YTDownloader" wenn keiner definiert) :', font=("Arial", 12))
path_label.pack(pady=1)

# Create an entry for the path
path_entry = ctk.CTkEntry(window, width=200, placeholder_text="path", textvariable=path_var)
path_entry.pack(pady=5, padx=10)

# Create a button that calls the download_video function when clicked
download_button = ctk.CTkButton(window, text="Download", fg_color="green" , hover_color="#35682b", command=lambda: download_video(url_var.get(), path_var.get()))
download_button.pack(pady=10)

# Start the GUI
window.mainloop()