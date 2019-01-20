import csv

class transaction():
	def __init__(self, client, payment, month, date, category, transaction, spending, income, total):
		self.account = client
		self.payment = payment
		self.month = month
		self.date = date
		self.category = category
		self.transaction = transaction
		self.spending = spending
		self.income = income
		self.total = total

def import_data():
	transaction_list = []
	with open('SampleTransactionDataset.csv') as csvdata:
		transaction_reader = csv.reader(csvdata)
		for row in transaction_reader:
			transaction_list.append(transaction(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
		transaction_list.pop(0)
	return transaction_list

def main():
	transaction_list = import_data()
