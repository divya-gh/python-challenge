import os
import csv
os.system("cls")

#function to map greatest increase in profits date and amount by creating a dictionary
'''----------------------------------------------------------------------------------'''
def profit_date_amount(dates , p_l_change):
    #initialize the dictionary
    date_and_amount={}
    for key in dates:
        #Assign value "0" to the first date
        if key == 'Jan-2010':
            date_and_amount[key] = 0
        else:
            for value in p_l_change:
                #Assign difference values to each date
                date_and_amount[key] = value
                #remove previous so that if doesnt get re-assignedsure 
                p_l_change.remove(value) 
                break
    return date_and_amount

#Function to calculate changes in "Profit/Losses" over the entire period and thier average
def calc_avg_change(profit_losses)
    monthly_diff = []
    for i in range(1,len(profit_losses)):
        change = int(profit_losses[i]) - int(profit_losses[i-1])
        monthly_diff.append(change)
    average_change  = sum(monthly_diff)/len(monthly_diff)  
    return average_change , monthly_diff


#Inititalize date and profit/loss as a list
'''--------------------------------------------'''
dates =[]
profit_loss = []

#Initialize total amount of "Profit/Losses" over the entire period
'''---------------------------------------------------------------'''
total_Profit_Losses = 0


#Get csv file path
'''---------------'''
py_bank_path = os.path.join(".", "Resources", "budget_data.csv")

#Open csv budget_data file
'''----------------------'''
with open(py_bank_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #sepearte header
    header = next(csvreader)
    #read rest of the rows 
    for row in csvreader:
        #creating a list of dates and profit/losses
        dates.append(row[0])
        profit_loss.append(row[1])
        #calculating total profit/losses
        total_Profit_Losses+=int(row[1])  
    

#1. The total number of months included in the dataset
'''-------------------------------------------------'''
total_months = len(dates)
print(f"Total Months: {total_months}")

#2. The net total amount of "Profit/Losses" over the entire period
'''-------------------------------------------------------------'''
print(f"Total: {total_Profit_Losses}")

#3. Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
'''----------------------------------------------------------------------------------------------------'''
#Call the function calc_avg_change(profit_loss) that calculates the average change 
average_change , monthly_change= calc_avg_change(profit_loss)
print(f"Average  Change: $ {round(average_change,2)}")

#4. The greatest increase in profits (date and amount) over the entire period
'''------------------------------------------------------------------------'''
#Find max diff in profit/losses
greatest_increase = max(P_L_Change_list)
#Call the function to create a dictionary of Months and profit/losses change
month_amount_dict = profit_date_amount(dates , monthly_change)
#Find date and max change amount
for key,value in month_amount_dict:
    if value == greatest_increase:
        profit_date = key
print(f"Greatest Increase in Profits: $ {profit_date} (${greatest_increase})")

#4. The greatest decrease in losses (date and amount) over the entire period
'''------------------------------------------------------------------------'''
#Find min diff in profit/losses
greatest_decrease =min(P_L_Change_list)
#Find date and max change amount using month_amount_dict dictionary
for key,value in month_amount_dict:
    if value == greatest_decrease:
        loss_date = key
print(f"Greatest Decrease in Profits: $ {loss_date} (${greatest_decrease})")

