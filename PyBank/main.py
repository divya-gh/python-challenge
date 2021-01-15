import os
import csv

py_bank_path = os.path.join(".", "Resources", "budget_data.csv")

date =[]
with open(py_bank_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        # Add title
        date.append(row[0])
    print(date)