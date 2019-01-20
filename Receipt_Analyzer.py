import string
import re
from PIL import Image
import pytesseract
import cv2
import os
from yelpapi import YelpAPI
import sys
#TODO:
# Add option for user to reassign classifications

def takePicture(): #Takes a picture of receipt
    cv2.namedWindow("ReceiptCamera")
    vc = cv2.VideoCapture(0)
    
    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False
    
    while rval:
        cv2.imshow("preview", frame) #show stream
        rval, frame = vc.read()
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            break
        if cv2.waitKey(1) & 0xFF == ord('r'): #save on pressing 'r' 
            cv2.imwrite('Receipt.png',frame)
            cv2.destroyAllWindows()
            break    
        
    cv2.destroyWindow("ReceiptCamera") 
    
    return 'Receipt.png'


def tesseract(imageFile): #Optical character recognition
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
    

def universal_finder(filename, find_list): #Extract facts from the receipt
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


def find_store_name(filename): #Find name of store
    # Just looks at the first line of the receipt txt
    # Pray that it's there
    file = open(filename, 'r')
    store_name = file.readline()
    file.close()
    # print(store_name.lower())
    return store_name.lower()  # Turns it lowercase for easier processing


def find_payment_method(filename): #Find their payment method
    # Usually only one instance of one of the target words
    # Doesn't handle case if there is more than of these target words in the file
    suggestive_words = ["CASH", "Cash", "CREDIT", "Credit", "DEBIT", "Debit"]
    total_list, payment_method = universal_finder(filename, suggestive_words)
    # print(payment_method[0].lower())
    if len(payment_method) == 0:
        payment_method.append('')
    return payment_method[0].lower()


def find_total_number(filename): # Finds instances of target word
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
    try:
        real_total_baby = max(confusion_matrix)  # Picks highest total as the real total
    except ValueError:
        real_total_baby = '???'
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


def find_date(filename): #Find date of transaction
    #possible names of dates
    suggestive_words = ["/", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
                        "Sept", "Oct", "Nov", "Dec", "January", "February", "March", "April",
                        "May", "June", "July", "August", "September", "October", "November", "December",
                        "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST",
                        "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"] 
    #try to find it in the receipt
    total_list, found_words = universal_finder(filename, suggestive_words)
    target_word = found_words[0].lower()
    numbered_date = numbered_dates_find(total_list[0])
    # print(numbered_date)
    return numbered_date


def yelpSearch(store, city="Edmonton"): #Search the store name on Yelp to find its classifications
    #my specific key
    yelp_api = YelpAPI("BkeVvBepP5xWd8hfOi_Pud4wx3d1NWAx7XV_oopCygqKDNuJyE1MBr5TqGhNlBf1KM-cVcz05YsyTGkAkeVq73yTbwbER51fVxc9Qq4vGBhwtCQkjZvPP9LBkvNDXHYx")
    #search yelp for the resturant
    op = yelp_api.search_query(term=store, location=city, sort_by='rating', limit = 5)
    title1 = ''
    title2 = ''
    title = []
    #find the descriptors of the buisness
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


def date_input(): #Allows user to enter a data of transaction
    month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
    date = input('Please enter transaction date (DD/MM/YY): ').split('/')
    month = date[1] + '.' + month_list[int(date[1]) - 1] #Correcting format of month
    formatted_date = date[0] + '/' + month_list[int(date[1]) - 1] + '/' + date[2] #Correcting format of date
    return month + ',' + formatted_date

def main():
    #Allow use of command line
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = takePicture()
    testing_file = tesseract(filename)
    paid = find_total_number(testing_file).rstrip() #find money paid
    method = find_payment_method(testing_file).rstrip() #find method of payment
    store = find_store_name(testing_file).rstrip() #find store
    # date = find_date(testing_file)
    tags = yelpSearch(store) #find tags of the store
    client = 'Robin' #placeholder client
    # date = date_input() 
    date = 'XX.XXX,XX/XX/XX'
    #Get the most relevant tag, which is usually the second one
    if len(tags)>1:
        classification = tags[1].rstrip()
    else:
        classification = tags[0].rstrip()

    filename = 'SampleTransactionDataset.csv' #Database (spreadsheet) of all transactions, including Servus database
    string = client + ',' + method + ',' + date + ',' + classification + ',' \
    + store + ',(' + paid + '),0.00 ,(' + paid +'),\n' #Proper formatting to put it into the database
    with open(filename, 'a') as f: 
        f.write(string)

main()