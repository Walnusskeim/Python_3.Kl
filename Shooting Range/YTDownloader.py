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
import customtktinter as tk


##################################################
#                     Code                       #
##################################################

def download_video(url, path):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download(path)


print("### YouTube Downloader ###")
url = input("Gib den Link des Videos ein: ")
path = "C:/YTDownloader/"
download_video(url, path)
