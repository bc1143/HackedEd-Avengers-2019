# import the necessary packages
from PIL import Image
import pytesseract
import cv2
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe" #path to tesseract on computer


# load the example image and convert it to grayscale
image = cv2.imread('receipt2.jpg')
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
#print(text)
f = 'receiptText_test.txt'
with open(f, 'w') as f:
    f.write(text)

cv2.waitKey(0)
