from tkinter import *
import urllib.request
import cv2
import numpy as np
import sys
url = 'http://172.31.21.206:8080/shot.jpg'

window = Tk()
window.title("Welcome to IPCamera App")
window.geometry('350x200')

def callback(img):

    print ("clicked!")
    cv2.imwrite('receiptImage.png', img)
    sys.exit(0)


while True:
    imgResp = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img = cv2.imdecode(imgNp, -1)
    cv2.imshow('test',img)
    b = Button(text="click me", command=callback)
    b.pack()
    window.mainloop()
    if ord('q')==cv2.waitKey(10):
        exit(0)

