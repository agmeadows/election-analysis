import csv
import os

file_to_load = os.path.join('Resources', 'election_results.csv')
file_to_save = os.path.join('Analysis', 'election_analysis.txt')

# declare variables
total_votes = 0
candidate_options = []
candidate_name = ""
candidate_votes = {}
votes = 0

candidate_dict = {}
#candidate_dict['candidate'] = {}

with open(file_to_load) as election_data:

    # declare variables for use in loop
    

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # add votes
        total_votes += 1
        # get candidate names
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        # tally votes
        candidate_votes[candidate_name] += 1 
    
    # put candidates in single dictionary with percentage won rounded to 2 decimals
    for key in candidate_votes:
        #print(key)
        candidate_dict[key] = {"votes" : candidate_votes[key], "percentage_won" : round(candidate_votes[key]/total_votes * 100, 1)}
    
    # calculate winner from dictionary
    for key in candidate_dict.keys():
        for value in candidate_dict.values():
            if (candidate_dict[key]['percentage_won'] > value['percentage_won']):
                #print(key, value['percentage_won'], candidate_dict[key]['percentage_won'])
                winner = key

    # print statistics
    for key in candidate_dict.keys():
        print(f"{key}: {candidate_dict[key]['percentage_won']}% ({candidate_dict[key]['votes']:,})\n")

    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"Winning Vote Count: {candidate_dict[winner]['votes']:,}\n"
    f"Winning Percentage: {candidate_dict[winner]['percentage_won']}%\n"
    f"-------------------------\n")
    
    print(winning_candidate_summary)


with open(file_to_save, 'w') as text_file:

    # write three counties to the file.
    text_file.write("Counties in the Election\n")
    text_file.write("________________________\n")
    text_file.write("Arapahoe\n")
    text_file.write("Denver\n")
    text_file.write("Jefferson")

# close the file.
election_data.close()
text_file.close()

# import data file
# get list of candidates
# create a vote count
# tally votes for each candidate
# get total votes for election
# determine election winner