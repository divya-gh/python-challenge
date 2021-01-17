import os
import csv
os.system("cls")

#Inititalize date and profit/loss as a list
'''--------------------------------------------'''
candidates =[]
average = 0
total_votes = 0
candidate_votes = {}
vote_count = 0

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
            #calculate total votes per candidates and add them to a dictionary.
            candidate_votes[row[2]] = vote_count +1
        else:
            candidate_votes[row[2]] = candidate_votes[row[2]] + 1      

#candidates list and candidates per vote dictionary
#print(candidates) 
#print(candidate_votes)  

##printing results to terminal:    
print("Election Results \n----------------------------")
print(f"Total Votes: {total_votes}\n----------------------------")
#calculate percentage of votes per candidate and print winner.  
percentage ={}  
max_vote = max(candidate_votes.values())
for key in candidate_votes:
    percentage[key] = (candidate_votes[key]/total_votes) * 100
    #printing percentage
    print(f"{key}: {round(percentage[key], 2)} ({candidate_votes[key]})")
    #Find winner based on max_value and print winner
    if candidate_votes[key] == max_vote:
        winner = key
print(f"Winner: {winner}\n----------------------------")



#Set csv file path to write
'''------------------------'''
poll_path = os.path.join(".", "analysis", "Poll_analysis.txt")
# Open file in "write" mode ('w') .
with open(poll_path, 'w') as text_file:

    # write lines into the file
    text_file.write("Election Results \n----------------------------")
    text_file.write(f"\nTotal Votes: {total_votes}\n----------------------------")
    for key in candidate_votes:
        text_file.write(f"\n{key}: {round(percentage[key], 2)} ({candidate_votes[key]})")
    text_file.write(f"Winner: {winner}\n----------------------------")
    