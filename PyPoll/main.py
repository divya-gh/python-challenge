import os
import csv
os.system("cls")

#Inititalize date and profit/loss as a list
'''--------------------------------------------'''
candidates =[]
average = 0
total_votes = 0

#Get csv file path
'''---------------'''
py_poll_path = os.path.join(".", "Resources", "election_data.csv")

#Open election_data csv file
'''----------------------'''
with open(py_poll_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #seperate header
    header = next(csvreader)
    #read rows
    for row in csvreader:
        #calculating total votes
        total_votes+= 1
        #get unique candidates
        if row[2] not in candidates:
            candidates.append(row[2])
        #Total number of votes per candidates

        
#printing results to terminal:    
print("Election Results \n----------------------------")

print(f"Total Votes: {total_votes}\n----------------------------")

print(f"Winner: {winner}\n----------------------------")




# Open file in "write" mode ('w') .
with open(file_path, 'w') as text_file:

    # write lines into the file
    text_file.write("Financial Analysis \n----------------------------")
    text_file.write(f"\nTotal Months: {total_months}")
    text_file.write(f"\nTotal: ${total_Profit_Losses}")
    text_file.write(f"\nAverage  Change: ${round(average_change,2)}")
    text_file.write(f"\nGreatest Increase in Profits: {profit_date} (${greatest_increase})")
    text_file.write(f"\nGreatest Decrease in Profits: {loss_date} (${greatest_decrease})")