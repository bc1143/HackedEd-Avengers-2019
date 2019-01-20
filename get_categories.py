from transactions import import_data

transaction_list = import_data()
list = []

for i in transaction_list:
    if i.category not in list:
        list.append(i.category)

for i in list:
    print(i)
