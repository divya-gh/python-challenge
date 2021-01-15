import os
import csv

py_bank_path = os.path.join(".", "Resources", "budget_data.csv")

date =[]
profit_loss = []
with open(py_bank_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        # Add title
        date.append(row[0])
        profit_loss.append(row[1])
    print(date)
    print(profit_loss)
    