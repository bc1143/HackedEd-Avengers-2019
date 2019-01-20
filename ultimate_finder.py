import string


def universal_finder(filename, find_list):
    marked_list = []
    found_words = []
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
    file = open(filename, 'r')
    store_name = file.readline()
    file.close()
    print(store_name.lower())
    return store_name.lower()


def find_payment_method(filename):
    suggestive_words = ["CASH", "Cash", "CREDIT", "Credit", "DEBIT", "Debit"]
    total_list, payment_method = universal_finder(filename, suggestive_words)
    print(payment_method[0].lower())
    return payment_method[0].lower()


def find_total_number(filename):
    suggestive_words = ["Total", "Paid", "total", "TOTAL"]
    total_list, found_words = universal_finder(filename, suggestive_words)
    confusion_matrix = []
    for i in range(0, len(total_list)):
        construct_total = []
        for characters in total_list[i]:
            if characters in string.digits or characters == ".":
                construct_total.append(characters)
        total_amount = ''.join(construct_total)
        confusion_matrix.append(total_amount)
    real_total_baby = max(confusion_matrix)
    print(real_total_baby)
    return real_total_baby


testing_file = "receiptText_test.txt"
print('Total Paid: ')
find_total_number(testing_file)

print('Payment Method: ')
find_payment_method(testing_file)

print('Store Name: ')
find_store_name(testing_file)