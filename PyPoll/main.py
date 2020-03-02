import os
import csv

csvpath = os.path.join('..', 'PyPoll', 'election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')

    csvheader = next(csvreader)
    print(f"CSV Header: {csvheader}")

    total_votes = 0
    candidate_list = []
    each_candidate = set()
    li_votes = 0
    li_percent = 0
    khan_votes = 0
    khan_percent = 0
    correy_votes = 0
    correy_percent = 0
    otooley_votes = 0
    otooley_percent = 0
    

    for row in csvreader:
        
        total_votes += 1 
        print(total_votes)
        
        each_candidate.add(row[2])
        new_candidate_list = list(each_candidate)
        print(new_candidate_list)

        if row[2] == "Li":
            li_votes += 1
        elif row[2] == "Khan":
            khan_votes += 1   
        elif row[2] == "Correy":
            correy_votes += 1
        elif row[2] == "O'Tooley":
            otooley_votes += 1
            
        #li_percent = (li_votes / total_votes) * 100
        #khan_percent = (khan_votes / total_votes) * 100
        #correy_percent = (correy_votes / total_votes) * 100
        #otooley_percent = (otooley_votes/ total_votes) * 100

    votes_bycandidates = []
    votes_bycandidates.append(li_votes)
    votes_bycandidates.append(khan_votes)
    votes_bycandidates.append(correy_votes)
    votes_bycandidates.append(otooley_votes)

    votes_bycandidates.sort()
    print(votes_bycandidates)
    #print(f"Winner is: ", votes_bycandidates[-1])
    
    
    


    #print(f" Number of Li's votes: {li_votes}")
    #print(f" Number of Khans's votes: {khan_votes}")
    #print(f" Number of Correy's votes: {correy_votes}")
    #print(f" Number of O'Tooley's votes: {otooley_votes}")
    #print(votes_bycandidates)
    #print(li_percent)


 