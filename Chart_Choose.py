from transactions import import_data
import matplotlib.pyplot as plt
import pprint
from tkinter import *
import sys

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
                trans_type[i.category] = round(trans_type[i.category], 2)
    total = round(total, 2)
    return trans_type, total

def piechart():
    plt.clf()
    data, total = category_chart('Bat Man')
    plt.rcParams["figure.figsize"] = [24, 12]
    labels = [k for k in data]

    colors = ['#00FFFF','#0000FF','#8A2BE2','#7FFF00','#FF7F50','#6495ED','#DC143C','#FF8C00','#FF1493',
              '#FF00FF','#C71585','#FFC0CB','#708090','#FFFF00','#000080','#B0C4DE']

    plt.pie([float(v) for v in data.values()], autopct=None, colors=colors)
    plt.title('My Transactions\nYou sure you want to spend that much?')
    plt.legend(labels, loc='best',bbox_to_anchor=(-0.08,1.),fontsize=10)
    plt.show()
    #plt.savefig('pie.png')

def barchart():
    plt.clf()
    data, total = category_chart('Bat Man')
    plt.rcParams["figure.figsize"] = [24, 12]
    names = list(data.keys())
    values = list(data.values())
    from matplotlib import rcParams
    rcParams.update({'figure.autolayout': True})
    plt.barh(range(len(data)), values, tick_label=names)
    plt.xlabel('Types of Transactions')
    plt.ylabel('Amount Spent')
    plt.title('Your Transaction Breakdown')
    plt.show()
    #plt.savefig('bar.png')


def print_amounts(client):
    transactions, total = category_chart(client)
    print("Your Total Expenses were " + str(total))
    print("Breakdown By Category: ")
    pprint.pprint(transactions)
    while input("Press Enter to Continue to View Graph Breakdown") != '':
        pass


def callback(number):
    if number == 1:
        barchart()
    elif number == 2:
        piechart()


def main():
    print_amounts(sys.argv[1])
    window = Tk()
    window.title('Pick a Chart!')
    window.geometry('150x75')
    Button(text="Bar Chart", command=lambda: callback(1)).pack()
    Button(text="Pie Chart", command=lambda: callback(2)).pack()
    window.mainloop()

main()