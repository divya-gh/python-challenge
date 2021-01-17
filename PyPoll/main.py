import os
import csv
os.system("cls")

#Inititalize candidates as a list and candidate_votes as a dictionary
'''-----------------------------------------------------------------'''
candidates =[]
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



#printing results to terminal:    
print("Election Results \n----------------------------")
print(f"Total Votes: {total_votes}\n----------------------------")
#calculate percentage of votes per candidate and print winner.  
percentage ={}  
max_vote = max(candidate_votes.values())
for key in candidate_votes:
    average = (candidate_votes[key]/total_votes)
    percentage[key] = "{:.3%}".format(average)
    #printing percentage per candidate to terminal
    print(f"{key}: {percentage[key]} ({candidate_votes[key]})")
    #Find winner based on max_value and print it to terminal
    if candidate_votes[key] == max_vote:
        winner = key
print(f"----------------------------\nWinner: {winner}\n----------------------------")



#Set csv file path to write
'''------------------------'''
poll_path = os.path.join(".", "analysis", "Poll_analysis.txt")
# Open file in "write" mode ('w') .
with open(poll_path, 'w') as text_file:

    # write lines to file
    text_file.write("Election Results \n----------------------------")
    text_file.write(f"\nTotal Votes: {total_votes}\n----------------------------")
    for key in candidate_votes:
        text_file.write(f"\n{key}: {percentage[key]} ({candidate_votes[key]})")
    text_file.write(f"\n----------------------------\nWinner: {winner}\n----------------------------")
    