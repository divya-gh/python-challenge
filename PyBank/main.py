import os
import csv


#Function to calculate changes in "Profit/Losses" over the entire period and thier average change
'''------------------------------------------------------------------------------------------'''
def calc_avg_change(profit_losses):
    monthly_diff = []
    for i in range(1,len(profit_losses)):
        change = int(profit_losses[i]) - int(profit_losses[i-1])
        monthly_diff.append(change)
    average_change  = sum(monthly_diff)/len(monthly_diff)  
    return average_change , monthly_diff


#Inititalize date and profit/loss as a list
'''--------------------------------------------'''
dates =[]
profit_losses = []
total_Profit_Losses = 0

#Get csv file path
'''---------------'''
py_bank_path = os.path.join(".", "Resources", "budget_data.csv")

#Open budget_data csv file
'''----------------------'''
with open(py_bank_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #seperate header
    header = next(csvreader)
    #read rows
    for row in csvreader:
        #creating a list of dates and profit/losses
        dates.append(row[0])
        profit_losses.append(row[1])
        #calculating total profit/losses
        total_Profit_Losses+=int(row[1])  

        
    
print("Financial Analysis \n----------------------------")
#1. The total number of months included in the dataset
'''-------------------------------------------------'''
total_months = len(dates)
print(f"Total Months: {total_months}")


#2. The net total amount of "Profit/Losses" over the entire period
'''-------------------------------------------------------------'''
print(f"Total: ${total_Profit_Losses}")


#3. Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
'''----------------------------------------------------------------------------------------------------'''
#Call the function calc_avg_change(profit_loss) that calculates the average change 
average_change , monthly_change = calc_avg_change(profit_losses)
print(f"Average  Change: ${round(average_change,2)}")


#4. The greatest increase in profits (date and amount) over the entire period
'''------------------------------------------------------------------------'''
#Exclude first month
dates.pop(0)

#Find max diff in profit/losses
greatest_increase = max(monthly_change)
profit_date = dates[monthly_change.index(greatest_increase)]
print(f"Greatest Increase in Profits: {profit_date} (${greatest_increase})")


#4. The greatest decrease in losses (date and amount) over the entire period
'''------------------------------------------------------------------------'''
#Find min diff in profit/losses
greatest_decrease = min(monthly_change)
loss_date = dates[monthly_change.index(greatest_decrease)]
print(f"Greatest Decrease in Profits: {loss_date} (${greatest_decrease})")


#5 print the analysis in a text file with the results.
'''------------------------------------------------'''
#set file path
file_path = os.path.join("analysis", "Py_Bank_analysis.txt")

# Open file in "write" mode ('w') .
with open(file_path, 'w') as text_file:

    # write lines into the file
    text_file.write("Financial Analysis \n----------------------------")
    text_file.write(f"\nTotal Months: {total_months}")
    text_file.write(f"\nTotal: ${total_Profit_Losses}")
    text_file.write(f"\nAverage  Change: ${round(average_change,2)}")
    text_file.write(f"\nGreatest Increase in Profits: {profit_date} (${greatest_increase})")
    text_file.write(f"\nGreatest Decrease in Profits: {loss_date} (${greatest_decrease})")
   


