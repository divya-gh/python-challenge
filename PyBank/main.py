import os
import csv
os.system("cls")
py_bank_path = os.path.join(".", "Resources", "budget_data.csv")

date =[]
profit_loss = []
total =0
with open(py_bank_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        # Add title
        date.append(row[0])
        profit_loss.append(row[1])
        total+=int(row[1])
        
   
    

#total  number of months
total_months = len(date)
print(total_months)
print(total)
#net total amount of 

#net_total_amount = sum(profit_loss)
#print(net_total_amount)

#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
changes= []
for i in range(len(profit_loss)):
    if i == len(profit_loss) :
        break
    else:
        changes.append(int(profit_loss[i+1]) - int(profit_loss[i]))
    

print(changes)