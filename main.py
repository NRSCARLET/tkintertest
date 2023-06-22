import tkinter as tk
"""from PIL import ImageTk, Image

#This creates the main window of an application
window = tk.Tk()
window.title("Join")
window.geometry("300x300")
window.configure(background='grey')

path = "kerchoo.png"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "bottom", fill = "both", expand = "yes")

#Start the GUI
window.mainloop()"""
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

# Create a photoimage object of the image in the path
image1 = Image.open("kerchoo.png")
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test

# Position image
label1.place(x=300, y=300)
root.mainloop()

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
print("image no worky")