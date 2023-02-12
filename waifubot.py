from tkinter import *

import time
import ctypes
import random
import urllib.request
from datetime import datetime
from PIL import ImageTk, Image

order = 0

def show_message():
    global order
    
    root = Tk()
    root.title("ur waifu")
    # List of image URLs
    image_urls = [
        "https://i.imgur.com/r8QQJMk.jpg",
        "https://i.imgur.com/4rj3rj6.jpg",
        "https://i.imgur.com/Uzwhaj8.jpg",
        "https://i.imgur.com/9qCv7PD.jpg",
        "https://i.imgur.com/QaO1R9k.jpg",
        "https://i.imgur.com/S1NHUvD.jpg",
        "https://i.imgur.com/Xfg0r7T.jpg",
        "https://i.imgur.com/c4O30Gi.jpg",
        "https://i.imgur.com/HLeybmJ.jpg",
        "https://i.imgur.com/JYDppUn.jpg",
        "https://i.imgur.com/u03xedr.jpg",
        "https://i.imgur.com/KRjfYdK.jpg",
        "https://i.imgur.com/blNg1mS.jpg",
        "https://i.imgur.com/fsWCiew.jpg",
        "https://i.imgur.com/JcVM2C0.jpg",
        "https://i.imgur.com/nwGgOiQ.jpg",
        "https://i.imgur.com/2vSau84.jpg",
        "https://i.imgur.com/8FOrw9z.jpg",
        "https://i.imgur.com/6FMikbi.jpg",
        "https://i.imgur.com/r0sj3z0.jpg",
        "https://i.imgur.com/SKJue3G.jpg",
        "https://i.imgur.com/muJLRyX.jpg",
        "https://i.imgur.com/RFYYHm2.jpg",
        "https://i.imgur.com/XHIhd2z.jpg",
        "https://i.imgur.com/QBRg6fJ.jpg"
    ]

    # Select an image
    img = image_urls[order]
    if order == (len(image_urls)-1):
        order = 0
    else:
        order += 1

    # Download the image
    image_filename = "urwaifu.jpg"
    urllib.request.urlretrieve(img, image_filename)
    
    img = ImageTk.PhotoImage(Image.open("urwaifu.jpg"))
    panel = Label(root, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
    
    root.mainloop()

def message_box(text, title):
    ctypes.windll.user32.MessageBoxW(0, text, title, 1)

def main():
    current_date = datetime.now()
    time.sleep(1)
    if current_date.month == 2 and current_date.day == 14:
        message_box("i will be here w u the wholeeeee day UwU lets hang out ❤️", "HAPPY VALENTINES BBYYYYY <333")
        while True:
            show_message()
            time.sleep(1) # wait for yo ass
    else:
        message_box("it is not even valentines day. i am leaving bye", "IMPATIENT BOY >_<")

main()
