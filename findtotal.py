import string


def find_total_line(filename):
    suggestive_words = ["Total", "Paid"]
    file = open(filename, 'r')
    lines = file.readlines()
    for i in range(0, len(lines)):
        for word in suggestive_words:
            if word in lines[i]:
                total_line = lines[i]
                return total_line
            else:
                pass


def find_total_number(total_line):
    total_list = []
    for characters in total_line:
        if characters in string.digits or characters == ".":
            total_list.append(characters)
    total_amount = ''.join(total_list)
    print(total_amount)


interesting_line = find_total_line('receiptText_test.txt')

find_total_number(interesting_line)