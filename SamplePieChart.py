import matplotlib.pyplot as plt
sizes=[100,1,90]
transaction=['Cash','Credit','Debit']
cols=['c','m','r','b']
plt.pie(sizes,labels=transaction, colors=cols,autopct='%1.1f%%',explode=(0,0.1,0))
plt.title('My Transactions')
plt.show()