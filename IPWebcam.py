import urllib.request
import cv2
import numpy as np 
url='http://172.31.21.206:8080/shot.jpg'

from tkinter import *
window = Tk()
window.title("Welcome to IPCamera App")
window.geometry('350x200')

btn = Button(window, text="Click Me")
btn.grid(column=1, row=0)

class button:
   def __init__(self):
       self.clicked = False
   def click(self):
       self.clicked = True

window.mainloop()

btn=button
prev_button = tk.Button(window, text="Take Photo", width=10, height=2, command=lambda: prev(panel))
prev_button.pack(in_=bottom, side="left")
while self.clicked == True:
   imgResp = urllib.request.urlopen(url)
   imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
   img = cv2.imdecode(imgNp,-1)
   cv2.imshow('test',img)
   cv2.imwrite('receiptImage.png',img)
   if ord('q')==cv2.waitKey(10):
       exit(0)
