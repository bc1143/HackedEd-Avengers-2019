import string
import re


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
    print(store_name.lower())
    return store_name.lower()  # Turns it lowercase for easier processing


def find_payment_method(filename):
    # Usually only one instance of one of the target words
    # Doesn't handle case if there is more than of these target words in the file
    suggestive_words = ["CASH", "Cash", "CREDIT", "Credit", "DEBIT", "Debit"]
    total_list, payment_method = universal_finder(filename, suggestive_words)
    print(payment_method[0].lower())
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
    print(real_total_baby)
    return real_total_baby


def numbered_dates_find(target_string):
    # Linny did this magic
    matches = re.findall('(\d{2}[\/ ](\d{2}|January|Jan|February|Feb|March|'
                         'Mar|April|Apr|May|May|June|Jun|July|Jul|August|Aug|September|'
                         'Sep|October|Oct|November|Nov|December|Dec)[\/ ]\d{2,4})', target_string)
    return matches[0][0]


def find_date(filename):
    suggestive_words = ["/", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
                        "Sept", "Oct", "Nov", "Dec", "January", "February", "March", "April",
                        "May", "June", "July", "August", "September", "October", "November", "December",
                        "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST",
                        "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]
    total_list, found_words = universal_finder(filename, suggestive_words)
    target_word = found_words[0].lower()
    numbered_date = numbered_dates_find(total_list[0])
    print(numbered_date)
    return numbered_date

# Testing and debugging
testing_file = "receiptText_test.txt"
print('Total Paid: ')
find_total_number(testing_file)

print('Payment Method: ')
find_payment_method(testing_file)

print('Store Name: ')
find_store_name(testing_file)

print('Transaction Date: ')
find_date(testing_file)

def safe_print(name):
    print(name + " is a poop")

safe_print("Ibrahim")