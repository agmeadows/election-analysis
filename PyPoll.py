# load dependancies
import csv
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
file_to_load = os.path.join('Resources', 'election_results.csv')
file_to_save = os.path.join('Analysis', 'election_analysis.txt')

# declare variables
total_votes = 0
candidate_options = []
candidate_name = ""
candidate_results = ""
candidate_votes = {}
county_name = ""
county_results = ""
counties = []
county_votes = {}
votes = 0

candidate_dict = {}
county_dict = {}

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

        county_name = row[1]
        if county_name not in counties:
            counties.append(county_name)
            county_votes[county_name] = 0
        # tally votes for each county
        county_votes[county_name] += 1 

    # put candidates in single dictionary with percentage won rounded to 2 decimals
    for key in candidate_votes:
        candidate_dict[key] = {"votes" : candidate_votes[key], "percentage_won" : round(candidate_votes[key]/total_votes * 100, 1)}
    
    # put counties in single dictionary with votes
    for key in county_votes:
        county_dict[key] = {"votes" : county_votes[key], "percentage_won" : round(county_votes[key]/total_votes * 100, 1)}
    
    # calculate candidate winner from dictionary
    for candidate in candidate_dict.keys():
        for value in candidate_dict.values():
            if (candidate_dict[candidate]['percentage_won'] > value['percentage_won']):
                winner = candidate

    # calculate county with highest turnout
    for county in county_dict.keys():
        for value in county_dict.values():
            if (county_dict[county]['percentage_won'] > value['percentage_won']):
                county_highest = county

    # print candadate stats
    for key in candidate_dict.keys():
        candidate_results = candidate_results + f"{key}: {candidate_dict[key]['percentage_won']}% ({candidate_dict[key]['votes']:,})\n"
    
    # print county stats
    for key in county_dict.keys():
        county_results = county_results + f"{key}: {county_dict[key]['percentage_won']}% ({county_dict[key]['votes']:,})\n"

    #print(candidate_results)

    county_summary = (
        f"\n-------------------------\n"
        f"Largest county turnout: {county_highest}\n"
        f"-------------------------\n\n"
    )

    winning_candidate_summary = (
        f"\n-------------------------\n"
        f"Winner: {winner}\n"
        f"Winning Vote Count: {candidate_dict[winner]['votes']:,}\n"
        f"Winning Percentage: {candidate_dict[winner]['percentage_won']}%\n"
        f"-------------------------\n")
    
with open(file_to_save, 'w') as text_file:

    election_results = (
        f"\nCounty Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\nCounty Votes:\n")
    
    print(county_results)
    print(county_summary)
    print(election_results, end="")
    print(candidate_results)
    print(winning_candidate_summary)
    
    # Save the final vote count to the text file.
    text_file.write(election_results)
    text_file.write(county_results)
    text_file.write(county_summary)
    text_file.write(candidate_results)
    text_file.write(winning_candidate_summary)

# close the file.
election_data.close()
text_file.close()

# import data file
# get list of candidates
# create a vote count
# tally votes for each candidate
# get total votes for election
# determine election winner