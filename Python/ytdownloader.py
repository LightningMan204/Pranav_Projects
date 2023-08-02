from pytube import YouTube
import os
from sys import argv

# For pytube `pip install pytube` in your cmd line.

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)

print("Views: ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download('/Applications/Games/Recordings/YT downloads')