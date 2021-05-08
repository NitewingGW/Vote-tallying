import csv
import os
import numpy as np
import pandas as pd
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0 
candidate_options = [] #Create list
candidate_votes = {} #Create Dict

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]#identify the column of interest add to variable
        if candidate_name not in candidate_options:#easy way to find unique entries in column
            candidate_options.append(candidate_name)#create list of the unique values
            candidate_votes[candidate_name] = 0 #created Key (candidate name and value set at 0)
        candidate_votes[candidate_name] += 1 #Add a vote for each time candidaTE REVIEVES VOTE
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percents = float(votes) / float(total_votes) * 100
        print(f"{candidate_name}: recieved {vote_percents:.1f}% of the vote.")