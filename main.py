import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

failsafe = False
goodgood = {"good"}
nono = {"bad"}
santa = {"hohoho"}
sweetheart = {"ohohoh"}
window = tk.Tk()
window.title("chrome.exe")
window.geometry("300x300")
def click():
    print("uwu")
    failsafe = True
    while failsafe == True:
        wow = input("is heelo good or bad?\n>> ")
        if wow in goodgood:
            print("kerchoo")
            Image.open("kerchoo.png")
            failsafe = False
        elif wow in nono:
            print("sobbing crying throwing up\nkathew")
            failsafe = False
        elif wow in santa:
            print("woah santa...\nnow answer my question")
            failsafe = True
        elif wow in sweetheart:
            print("GO BACK TO CAPTAIN SPACE BOYFRIEND")
            failsafe = True
        else:
            print("that not what I asked doofus")
            failsafe = True

hello = tk.Label(text="peepeepoopoo")
hello.pack()
button = tk.Button(text="smash me",
                  command=click)

button.pack()

tk.mainloop()
