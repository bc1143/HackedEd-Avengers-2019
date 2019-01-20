from tkinter import *
from tkinter import Menu
from transactions import import_data
data=import_data()

window = Tk()
window.title("Welcome to LikeGeeks app")
menu = Menu(window)

def clicked():
    print('Hello')
new_item = Menu(menu)
new_item.add_command(label='Retail-Eating Places',command=clicked)

new_item.add_separator()
new_item.add_command(label='Retail-Fast Food')

new_item.add_separator()
new_item.add_command(label='eTransfer- Vacation Property Rental')

new_item.add_separator()
new_item.add_command(label='Services-auto cleaner')

new_item.add_separator()
new_item.add_command(label='Retail-Gas Station')

new_item.add_separator()
new_item.add_command(label='Hotels $ Motels')

new_item.add_separator()
new_item.add_command(label='Retail - Books and Household items')

new_item.add_separator()
new_item.add_command(label='Retail-Auto Glass')

new_item.add_separator()
new_item.add_command(label='Retail-Corner Store')

new_item.add_separator()
new_item.add_command(label='Retail-Grocery Stores')

new_item.add_separator()
new_item.add_command(label='Retail-Boat Supply')

new_item.add_separator()
new_item.add_command(label='Retail-Supplies')


new_item.add_separator()
new_item.add_command(label='Services-Safety')


menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)
window.mainloop()