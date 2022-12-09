# Importing all libraries
import os
import csv

# setting path to data csv file
csvpath = os.path.join('Resources','election_data.csv')

# Open file and allow read only
with open(csvpath, encoding="utf-8") as csvfile:


    # Skip counting headers
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)

    # Defining variables that need tracking
    candidate = []

    # Count total votes - simple counting + note all the candidates into list
    total_votes = 0
    for row in csvreader:
        candidate.append(row[2])
        total_votes += 1
    
    # Determine all the unique candidates and put into list
    unique_candidates = []
    for i in candidate:
        if not i in unique_candidates:
            unique_candidates.append(i)

    # Create a dictionary where key = candidate, value = votes
    candidate_vote = {}
    for name in unique_candidates:
        unique_candidate_votes = candidate.count(name)
        candidate_vote[name] = unique_candidate_votes
    
    # Create variables that allow indexing for the dictionary
    # Allow referencing for the summary table
    candidate_keys = list(candidate_vote.keys())
    candidate_values = list(candidate_vote.values())
 
    # Determining percentages of votes, rounded to 3 decimals
    percent_votes = []
    for name in candidate_vote:
        percent_votes.append(round(candidate_vote[name]/total_votes * 100, 3))

    # Determining winner's name automatically 
    # List added in 'candidate_keys' to avoid 'type error' 
    winner_percent = max(percent_votes)
    winner_index = percent_votes.index(winner_percent)
    winner_name = candidate_keys[winner_index]

    # Print to console summary results
    def summary():
        return f'Election Results\n--------------------\n'\
        f'Total Votes {total_votes}\n--------------------\n'\
        f'{candidate_keys [0]}: {percent_votes[0]}% ({candidate_values[0]}) \n'\
        f'{candidate_keys [1]}: {percent_votes[1]}% ({candidate_values[1]}) \n'\
        f'{candidate_keys [2]}: {percent_votes[2]}% ({candidate_values[2]}) \n--------------------\n'\
        f'Winner: {winner_name}\n--------------------'

print (summary())

# Set path for output file - calling text file financial_summary
output_file = os.path.join("Analysis","vote_summary.txt")

# Insert in the financial analysis
with open(output_file, "w") as txtfile:
    txtfile.write(summary())  
