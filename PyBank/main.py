import os
import csv
os.system("cls")

#Function to create a dictionary of date and amount change
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
                #remove previous value avoid re-assignment
                p_l_change.remove(value) 
                break
    return date_and_amount

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
    #seperate header
    header = next(csvreader)
    #read rows
    for row in csvreader:
        #creating a list of dates and profit/losses
        dates.append(row[0])
        profit_loss.append(row[1])
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
average_change , monthly_change= calc_avg_change(profit_loss)
print(f"Average  Change: ${round(average_change,2)}")

#4. The greatest increase in profits (date and amount) over the entire period
'''------------------------------------------------------------------------'''
#Find max diff in profit/losses
greatest_increase = max(monthly_change)

#Call the function to create a dictionary of Months and profit/losses change
month_amount_dict = profit_date_amount(dates , monthly_change)

#Find date and max_change amount
for key in month_amount_dict:
    if month_amount_dict[key] == greatest_increase:
        profit_date = key
        break
print(f"Greatest Increase in Profits: {profit_date} (${greatest_increase})")

#4. The greatest decrease in losses (date and amount) over the entire period
'''------------------------------------------------------------------------'''
#montly_change has been deleted while creating a dictionary of date and change amount ; to get it back, call function again
average_change , monthly_change = calc_avg_change(profit_loss)
#Find min diff in profit/losses
greatest_decrease = min(monthly_change)
#Find date and max change amount using month_amount_dict dictionary
for key  in month_amount_dict:
    if month_amount_dict[key] == greatest_decrease:
        loss_date = key
        break
print(f"Greatest Decrease in Profits: {loss_date} (${greatest_decrease})")

#5 print the analysis in a text file with the results.
'''------------------------------------------------'''
#set file path
file_path = os.path.join(".", "analysis", "Py_Bank_analysis.txt")

# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(file_path, 'w') as text_file:

    # Store all of the text inside a variable called "lines"
    text_file.write("Financial Analysis \n----------------------------")
    text_file.write(f"\nTotal Months: {total_months}")
    text_file.write(f"\nTotal: ${total_Profit_Losses}")
    text_file.write(f"\nAverage  Change: ${round(average_change,2)}")
    text_file.write(f"\nGreatest Increase in Profits: {profit_date} (${greatest_increase})")
    text_file.write(f"\nGreatest Decrease in Profits: {loss_date} (${greatest_decrease})")
   


