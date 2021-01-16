import os
import csv
os.system("cls")

#getting the path for the csv file
py_bank_path = os.path.join(".", "Resources", "budget_data.csv")

#Inititalize date and profit/loss as a list
date =[]
profit_loss = []

#Initialize total amount of "Profit/Losses" over the entire period
total_Profit_Losses = 0

#Open csv budget_data file
with open(py_bank_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #sepearting header
    header = next(csvreader)
    #read rest of the rows 
    for row in csvreader:
        #creating a list of dates and profit/losses
        date.append(row[0])
        profit_loss.append(row[1])
        #calculating total profit/losses
        total_Profit_Losses+=int(row[1])
        
   
    

#total  number of months
total_months = len(date)
print(total_months)
print(total_Profit_Losses)
#net total amount of 

#net_total_amount = sum(profit_loss)
#print(net_total_amount)

#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
P_L_Change_list = []
for i in range(1,len(profit_loss)):
    profit_loss_change = int(profit_loss[i]) - int(profit_loss[i-1])
    P_L_Change_list.append(profit_loss_change)
    

#print(changes)
#percentage 
average_change  = sum(P_L_Change_list)/len(P_L_Change_list)
print(f"Average Change: $ {round(average_change,2)} ")
greatest_increase = max(P_L_Change_list)
greatest_decrease =min(P_L_Change_list)

print(greatest_increase)
print(greatest_decrease)
print("change list")
#print(P_L_Change_list)
print("Date: ")
#print(date)

pair={}
for key in date:
    if key == 'Jan-2010':
        pair[key] = 0
    else:
        for value in P_L_Change_list:
            pair[key] = value
            P_L_Change_list.remove(value) 
            break

print(pair)