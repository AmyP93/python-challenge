##Main script to run for each analysis

import csv

election_data_csv = "C:\\1-SMU DATA VISUA\\1-Github\\Repos\\python-challenge\\PyPoll\\Resources\\election_data.csv"

file_to_output = "PyPoll/Analysis/PyPoll_analysis.txt"

#Variables to track
total_votes = 0
vote_percent = []       #lower, I have vote_percent in {} not []
candidate_options = []  #list of candidate names
candidate_total = {}    #Each candidates totals
winner = " "            #winner's name
winner_count =999999         #amount of votes for the winner


#read csv and create dictionary
with open(election_data_csv) as Poll_data:
    csvreader = csv.DictReader(Poll_data)

    for row in csvreader:       


        #Add to total vote count
        total_votes = total_votes + 1  

        #Save the candidate's name
        candidate_name = row["Candidate"]

        #Is this the first time Candidate name appears?
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_total[candidate_name] = 1
        else:
            candidate_total[candidate_name] = candidate_total[candidate_name] + 1

with open(file_to_output, "w") as txt_file:
    
    #print final vote count
    election_results = (
        f"\n\nElection Results\n"
        f"--------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"--------------------------\n"
    )

    print(election_results, end="")

    txt_file.write(election_results)

   # determine winning candidate
    for candidate in candidate_total:

        votes = candidate_total.get(candidate)
        vote_percent = float(votes) / float(total_votes) * 100

        if (votes > winner_count):
            winner_count = votes
            winner_candidate = candidate

        voter_output = f"{candidate}: {vote_percent:.3f}% ({votes})\n"
        print(voter_output, end="")

        txt_file.write(voter_output)

    winning_candidate_summary = (
        f"------------------------\n"
        f"Winner: {winner_candidate}\n"
        f"------------------------\n"
        
    )

    print(winning_candidate_summary)

txt_file.write(winning_candidate_summary)