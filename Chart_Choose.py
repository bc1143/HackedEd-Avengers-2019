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
    plt.rcParams["figure.figsize"] = [16, 9]
    labels = [k for k in data]
    apple = plt.pie([float(v) for v in data.values()], labels=[k for k in data],
           autopct=None)
    plt.title('My Transactions\nYou sure you want to spend that much?')
    # plt.legend(labels, loc='left center',bbox_to_anchor=(-0.08,1.),fontsize=10)
    plt.show(apple)

def barchart(data):
    names = list(data.keys())
    values = list(data.values())
    from matplotlib import rcParams
    rcParams.update({'figure.autolayout': True})
    plt.barh(range(len(data)),values,tick_label=names)
    plt.xlabel('Types of Transactions')
    plt.ylabel('Amount Spent')
    plt.title('Your Transaction Breakdown')
    plt.show()

def main():
    transaction_data, total = category_chart('Jerry Maguire')
    print(transaction_data)
    piechart(transaction_data)
    barchart(transaction_data)

main()
