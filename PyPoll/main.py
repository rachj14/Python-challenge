import os
import csv
election_data = os.path.join('Resources', 'election_data.csv')

# Set variables
total_votes = 0
total_candidates = 0
candidate_1_votes = 0
candidate_2_votes = 0
candidate_3_votes = 0
candidate = []
candidate_index = [0, 1, 2]

# Read CSV file
with open(election_data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        # Count number of total votes
        total_votes += 1

        # Capture different candidates names
        if row[2] not in candidate:
            candidate.append(row[2])

        # Count the number of votes
        if row[2] == candidate[0]:
            candidate_1_votes += 1

        elif row[2] == candidate[1]:
            candidate_2_votes += 1

        elif row[2] == candidate[2]:
            candidate_3_votes += 1

        candidate1count = round(candidate_1_votes / total_votes * 100, 3)
        candidate2count = round(candidate_2_votes / total_votes * 100, 3)
        candidate3count = round(candidate_3_votes / total_votes * 100, 3)

        # Winning candidate
        Poll = {"Charles Casper Stockham":candidate1count, "Diana DeGette":candidate2count, "Raymon Anthony Doane":candidate3count}
        winner = max(Poll, key=Poll.get)

    print("Election Results")
    print("-----------------------------")
    print("Total Votes: " + str(total_votes))
    print("-----------------------------")
    print(str(candidate[0]) + ": " + str(candidate1count) + "% (" + str(candidate_1_votes) + ")")
    print(str(candidate[1]) + ": " + str(candidate2count) + "% (" + str(candidate_2_votes) + ")")
    print(str(candidate[2]) + ": " + str(candidate3count) + "% (" + str(candidate_3_votes) + ")")
    print("-----------------------------")
    print("Winner: " + str(winner))
    print("-----------------------------")