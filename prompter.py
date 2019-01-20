import csv

client = 'Robin' #merge
date = 'XX.XXX,XX/XXX/XX' #merge


newClass = input('Name a new class: ')
numberOfOld = int(input('How many classes to replace: '))
oldClasses = []
for i in range(0, numberOfOld):
    replace = input('Enter the classes one by one: ')
    oldClasses.append(replace)

prices=[]    

filename = 'SampleTransactionDataset.csv'
newFilename = 'SampleTransactionDataset_client.csv'

with open(filename) as csvdata:
    transaction_reader = csv.reader(csvdata)
    transaction_writer = csv.writer(csvdata)
    for row in transaction_reader:
        for oldClass in oldClasses:
            if oldClass == transaction(row[4]):
                prices.append(transaction(row[6]))
                transaction_writer.whiterow(row)

with open(newFilename, 'a') as f:
    for price in prices:
        string = client + ',' + 'various methods' + ',' + date + ',' + newClass + ',' + 'various stores' + ',(' + price + '),0.00 ,(' + price +'),\n'
        f.write(string)
                