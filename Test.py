import tkinter as tk
from PIL import ImageTk, Image


def next(panel):
    path = "bar.png"
    img = ImageTk.PhotoImage(Image.open(path))
    panel.configure(image=img)
    panel.image = img # keep a reference!

def prev(panel):
    path = "pie.png" #alternate
    img = ImageTk.PhotoImage(Image.open(path))
    panel.configure(image=img)
    panel.image = img # keep a reference!


window = tk.Tk()
window.title("Welcome to Financial Fitness")
lbl = tk.Label(window, text="Here is your spending history!",font=("Garamond", 40))


top = tk.Frame(window)
top.pack(side="top")
bottom = tk.Frame(window)
bottom.pack(side="bottom")

path = 'finfit.png' #this is the image displayed first
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(window, image = img)
panel.image = img # keep a reference!
panel.pack(side = "top", fill = "both", expand = "yes")

prev_button = tk.Button(window, text="Previous", width=10, height=2, command=lambda: prev(panel))
prev_button.pack(in_=bottom, side="left")
next_button = tk.Button(window, text="Next", width=10, height=2, command=lambda: next(panel))
next_button.pack(in_=bottom, side="right")

window.mainloop()