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

def piechart():
    plt.clf()
    data, total = category_chart('Jerry Maguire')
    plt.rcParams["figure.figsize"] = [24, 12]
    labels = [k for k in data]
    plt.pie([float(v) for v in data.values()], labels=[k for k in data],
           autopct=None)
    plt.title('My Transactions\nYou sure you want to spend that much?')
    # plt.legend(labels, loc='left center',bbox_to_anchor=(-0.08,1.),fontsize=10)
    #plt.show()
    plt.savefig('pie.png')

def barchart():
    plt.clf()
    data, total = category_chart('Jerry Maguire')
    plt.rcParams["figure.figsize"] = [24, 12]
    names = list(data.keys())
    values = list(data.values())
    from matplotlib import rcParams
    rcParams.update({'figure.autolayout': True})
    plt.barh(range(len(data)),values,tick_label=names)
    plt.xlabel('Types of Transactions')
    plt.ylabel('Amount Spent')
    plt.title('Your Transaction Breakdown')
    #plt.show()
    plt.savefig('bar.png')
