"""from tkinter import *
from PIL import Image,ImageTk

window = Tk()

window.title("Welcome to Financial Fitness")
lbl = Label(window, text="Here is your spending history!",font=("Garamond", 16))
lbl.grid(column=0, row=0)
btn = Button(window, image="picture.png")
window.geometry('1600x900')
window.mainloop()
"""

"""""
from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.title("Welcome to Financial Fitness")
root.title("Welcome to Financial Fitness")
lbl = Label(root, text="Here is your spending history!",font=("Garamond", 16))

def Click():

    image = Image.open("picture.png")
    photo = ImageTk.PhotoImage(image)

    label = Label(root,image=photo)
    label.image = photo # keep a reference!
    label.pack()

image = Image.open("pepe.jpeg")
photo = ImageTk.PhotoImage(image)
label = Label(root,image=photo)

label.image = photo # keep a reference!
label.pack()


labelframe = LabelFrame(root)
labelframe.pack(fill="both", expand="yes")


left = Label(labelframe)

button=Button(labelframe, padx = 5, pady = 5, text="Next",command = Click)
button.pack(side = RIGHT)


R1 = Radiobutton(labelframe, text="Pie Graph", value=1)
R1.pack(side = LEFT)

R2 = Radiobutton(labelframe, text="Bar Graph",  value=2)
R2.pack(side = LEFT)


left.pack()
root.mainloop()
"""

import tkinter as tk
from PIL import ImageTk, Image


def next(panel):
    path = "Han.jpeg"
    img = ImageTk.PhotoImage(Image.open(path))
    panel.configure(image=img)
    panel.image = img # keep a reference!

def prev(panel):
    path = "picture.png"
    img = ImageTk.PhotoImage(Image.open(path))
    panel.configure(image=img)
    panel.image = img # keep a reference!


window = tk.Tk()
window.title("Welcome to Financial Fitness")


top = tk.Frame(window)
top.pack(side="top")
bottom = tk.Frame(window)
bottom.pack(side="bottom")

path = "finfit.png"
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(window, image = img)
panel.image = img # keep a reference!
panel.pack(side = "top", fill = "both", expand = "yes")

prev_button = tk.Button(window, text="Previous", width=10, height=2, command=lambda: prev(panel))
prev_button.pack(in_=bottom, side="left")
next_button = tk.Button(window, text="Next", width=10, height=2, command=lambda: next(panel))
next_button.pack(in_=bottom, side="right")

window.mainloop()
