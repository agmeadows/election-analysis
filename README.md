# Election-Analysis

## Project Overview
Calculate the candidate winner for the local congress election from data provided from the Colorodo Board of Elections

1. Calculate the total votes cast.
2. Get a complete list of counties participating in polling.
3. Calculate the total number of votes placed in each county.
4. Calculate the percentage of votes placed in each county.
5. Determine the county with the highest voter turnout.
6. Get a complete list of candidates who received votes.
7. Calculate the total number of votes for each candidate.
8. Calculate the percentage of votes for each candidate.
9. Determine the winner based on popular vote

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Election Audit Results
### The analysis of the election show:
#### - There were 369,711 votes cast
#### - The counties were:
    - Jefferson
    - Denver
    - Arapahoe
#### - The polling results for the counties were:
    - Jefferson received 10.5% of the votes and 38,855 total votes
    - Denver received 82.8% of the votes and 306,055 total votes
    - Arapahoe received 6.7% of the votes and 24,801 total votes
    - Denver had the largest voter turnout
#### - The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
#### - The candidate results were:
    - Charles Casper Stockham received 23.0% of the votes and 85,213 total votes
    - Diana DeGette received 73.8% of the votes and 272,892 total votes
    - Raymon Anthony Doane received 3.1% of the votes and 11,606 total votes
#### - The winner of the election was Diana DeGette who received 73.8% of the vote and 272,892 total votes

## Election Audit Summary
By using the provided data set to perform an election analysis, we are able to determine the winner of the local congress election. Additionally, we can determine the county with the largest voter turn out. While the data set was limited, the analysis could be modified to work for any election. These are as follows:

### - Proposed modifications
    - Automate column discovery
    --  Currently, column headers are not used to discover the data beneath them. These are hard coded. If the column order were to change the script would not work. Instead, the program can look at the data file headers to determine the data beneath is. For instance, ballot_id or candidate_name