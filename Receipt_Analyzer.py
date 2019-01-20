import string
import re
from PIL import Image
import pytesseract
import cv2
import os
from yelpapi import YelpAPI
import sys

def tesseract(imageFile):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
    # load the example image and convert it to grayscale
    image = cv2.imread(imageFile)
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
    
    f = 'receiptText_test.txt' #file to be written to
    with open(f, 'w') as f:
        f.write(text)
    
    cv2.waitKey(0)    
    
    return 'receiptText_test.txt'
    

def universal_finder(filename, find_list):
    # filename is name of receipt txt file from receipt image
    # find_list is list of target words
    marked_list = []  # List of lines that contains target words
    found_words = []  # List of target words that were triggered
    # Open file, read line by line and look for target words
    # Add entire line to marked_list if line contains target word
    file = open(filename, 'r')
    lines = file.readlines()
    for i in range(0, len(lines)):
        for word in find_list:
            if word in lines[i]:
                marked_list.append(lines[i])
                found_words.append(word)
    file.close()
    return marked_list, found_words


def find_store_name(filename):
    # Just looks at the first line of the receipt txt
    # Pray that it's there
    file = open(filename, 'r')
    store_name = file.readline()
    file.close()
    # print(store_name.lower())
    return store_name.lower()  # Turns it lowercase for easier processing


def find_payment_method(filename):
    # Usually only one instance of one of the target words
    # Doesn't handle case if there is more than of these target words in the file
    suggestive_words = ["CASH", "Cash", "CREDIT", "Credit", "DEBIT", "Debit"]
    total_list, payment_method = universal_finder(filename, suggestive_words)
    # print(payment_method[0].lower())
    return payment_method[0].lower()


def find_total_number(filename):
    # Finds instances of target word
    # Total usually shows up multiple times ie subtotal and total
    # Stores these possible totals and then picks the higher one
    # Doesn't work for Tesco receipts
    suggestive_words = ["Total", "Paid", "total", "TOTAL"]
    total_list, found_words = universal_finder(filename, suggestive_words)
    confusion_matrix = []  # Stores the potential totals
    # Go through the line, only keep the numbers and decimal points
    for i in range(0, len(total_list)):
        construct_total = []
        for characters in total_list[i]:
            if characters in string.digits or characters == ".":
                construct_total.append(characters)
        total_amount = ''.join(construct_total)
        confusion_matrix.append(total_amount)
    real_total_baby = max(confusion_matrix)  # Picks highest total as the real total
    # print(real_total_baby)
    return real_total_baby

'''
def numbered_dates_find(target_string):
    # Linny did this magic
    matches = re.findall('(\d{2}[\/ ](\d{2}|January|Jan|February|Feb|March|'
                         'Mar|April|Apr|May|May|June|Jun|July|Jul|August|Aug|September|'
                         'Sep|October|Oct|November|Nov|December|Dec)[\/ ]\d{2,4})', target_string)
    return matches[0][0]
'''

def find_date(filename):
    suggestive_words = ["/", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
                        "Sept", "Oct", "Nov", "Dec", "January", "February", "March", "April",
                        "May", "June", "July", "August", "September", "October", "November", "December",
                        "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST",
                        "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]
    total_list, found_words = universal_finder(filename, suggestive_words)
    target_word = found_words[0].lower()
    numbered_date = numbered_dates_find(total_list[0])
    # print(numbered_date)
    return numbered_date

def yelpSearch(store, city="Edmonton"):
    yelp_api = YelpAPI("BkeVvBepP5xWd8hfOi_Pud4wx3d1NWAx7XV_oopCygqKDNuJyE1MBr5TqGhNlBf1KM-cVcz05YsyTGkAkeVq73yTbwbER51fVxc9Qq4vGBhwtCQkjZvPP9LBkvNDXHYx")
    op = yelp_api.search_query(term=store, location=city, sort_by='rating', limit = 5)
    title1 = ''
    title2 = ''
    title = []
    try:
        title1=op['businesses'][0]['categories'][0]['title']
    except IndexError:
        print('Retailer not Recognized')
    try:
        title2=op['businesses'][0]['categories'][1]['title']
    except IndexError:
        pass
    title.append(title1)
    title.append(title2)
    
    return title

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = 'receipt2.JPG'
    testing_file = tesseract(filename)
    paid = find_total_number(testing_file).rstrip()
    method = find_payment_method(testing_file).rstrip()
    store = find_store_name(testing_file).rstrip()
    # date = find_date(testing_file)
    tags = yelpSearch(store)
    client = 'Robin'
    date = 'XX.XXX,XX/XXX/XX'
    if len(tags)>1:
        classification = tags[1].rstrip()
    else:
        classification = tags[0].rstrip()

    filename = 'SampleTransactionDataset.csv' 
    string = client + ',' + method + ',' + date + ',' + classification + ',' \
    + store + ',(' + paid + '),0.00 ,(' + paid +'),\n'
    with open(filename, 'a') as f: 
        f.write(string)

main()