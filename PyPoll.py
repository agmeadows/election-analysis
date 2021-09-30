import csv
import os

file_to_load = os.path.join('Resources', 'election_results.csv')
file_to_save = os.path.join('Analysis', 'election_analysis.txt')

with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
    # Print each row in the CSV file.
    #for row in file_reader:
    #    print(row)

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