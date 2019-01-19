def findtotal(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    for line in lines:
        if "TOTAL" or "Total" in line:
            print(line)
        else:
            print('No total found')

findtotal('receiptText_test.txt')