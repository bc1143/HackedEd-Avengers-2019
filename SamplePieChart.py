from transactions import import_data
import matplotlib.pyplot as plt

def category_chart(client):
    transactions = import_data()
    trans_type = {}
    total = 0
    for i in transactions:
        if i.account == client:
            if '(' in i.total:
                amount = i.total.strip('(')
                amount = amount.strip(')')
                amount = float(amount)
                total += amount
            if not i.category in trans_type:
                trans_type[i.category] = amount
            else:
                trans_type[i.category] += amount
    return trans_type, total

def piechart(data):
    plt.pie([float(v) for v in data.values()], labels=[k for k in data],
           autopct=None)
    plt.title('My Transactions')
    plt.show()

def barchart(data):
    names = list(data.keys())
    values = list(data.values())
    plt.bar(range(len(data)),values,tick_label=names)
    plt.show()

def main():
    transaction_data, total = category_chart('Jerry Maguire')
    print(transaction_data)
    piechart(transaction_data)
    barchart(transaction_data)

main()