# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import urllib.request
import numpy as np
import os

url='http://172.31.21.206:8080/shot.jpg' #url to be used to connect to phone camera
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe" #path to tesseract on computer


def live_camera(output_filename):
    while True: # stream from Android phone and take an image
        imgResp = urllib.request.urlopen(url)
        imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
        img = cv2.imdecode(imgNp,-1)
        cv2.imshow('test', img)
        cv2.imwrite(output_filename + ".png", img)
        if ord('q') == cv2.waitKey(10):
            exit(0)


def ocr(open_filename):
    # load the example image and convert it to grayscale
    image = cv2.imread(open_filename)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # apply thresholding to preprocess image
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # write the grayscale image to disk as a temporary file so we can
    # apply OCR to it
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)

    # load the image as a PIL/Pillow image, apply OCR, and then delete
    # the temporary file
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    # print(text)
    f = 'receiptText_test.txt'
    with open(f, 'w') as f:
        f.write(text)

    cv2.waitKey(0)
