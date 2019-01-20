import string


def find_total_line(filename):
    total_line_list = []
    suggestive_words = ["Total", "Paid", "total", "TOTAL"]
    file = open(filename, 'r')
    lines = file.readlines()
    for i in range(0, len(lines)):
        for word in suggestive_words:
            if word in lines[i]:
                total_line_list.append(lines[i])
    print(total_line_list)
    return total_line_list


def find_total_number(total_line_list):
    confusion_matrix = []
    for i in range(0, len(total_line_list)):
        construct_total = []
        for characters in total_line_list[i]:
            if characters in string.digits or characters == ".":
                construct_total.append(characters)
        total_amount = ''.join(construct_total)
        confusion_matrix.append(total_amount)
    real_total_baby = max(confusion_matrix)
    print(real_total_baby)
    return real_total_baby


interesting_line = find_total_line('receiptText_test.txt')

find_total_number(interesting_line)