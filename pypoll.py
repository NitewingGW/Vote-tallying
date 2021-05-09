import csv #allows importing of csv
import os #allows use of file path
import numpy as np #not used only for data testing
import pandas as pd #not used for funtionality only for testing data in dataframes 
file_to_load = os.path.join("Resources", "election_results.csv") #Location of csv
file_to_save = os.path.join("analysis", "election_analysis.txt") #location of analysis file to be written to

total_votes = 0 #accumulator stores total number of votes cast
candidate_options = [] #Create list stores the names of the candidates
candidate_votes = {} #Create Dict stores the votes for each candidate

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]                        #identify the column of interest add to variable
        if candidate_name not in candidate_options:    #easy way to find unique entries in column
            candidate_options.append(candidate_name)   #create list of the unique values
            candidate_votes[candidate_name] = 0        #created Key (candidate name and value set at 0)
        candidate_votes[candidate_name] += 1           #Add a vote for each time candidate recieves vote
    for candidate_name in candidate_votes:             #iterates through candiate names
        votes = candidate_votes[candidate_name]        #assigns votes to each candidate
        vote_percents = (float(votes) / float(total_votes)) * 100       #calculates vote percentage. Floats allow decimal to be calculated
        print(f"{candidate_name}: recieved {votes:,} votes for {vote_percents:.1f}% of the vote.")
        if votes > 0:                                  #ensures no candidate that didn't recieve votes is checked as a winner...saves cycles
            if (votes > winning_count) and (vote_percents > winning_percentage):      #searches for a higher vote and percetage count to find winner
                winning_counts = votes                 #adds the higher vote count until highest vote count reached
                winning_percentage = vote_percents     #add the higher vote percentage until highest vote percentage reached
                winning_candidate = candidate_name     #adds the candidate that got the higher vote count and higher vote percentage
                #print(votes)
                #print(vote_percents)
            else: #Does not work without this else. It stopped the printing of both candidates that had higher than Raymon. Catches the winner
                print(f"\n\nThe WINNER of this election is {winning_candidate}. \n{winning_candidate} won with {winning_counts:,} votes and {winning_percentage:.1f}% of the {total_votes:,} ballots cast")
            
        

#print(candidate_votes)
#print(candidate_votes[candidate_name])
#print(votes)
#print(candidate_votes)