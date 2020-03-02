import os
import csv

csvpath = os.path.join('..', 'PyPoll', 'election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')

    csvheader = next(csvreader)
    
    total_votes = 0
    #candidate_list = []
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
        
        #total number of votes cast
        total_votes += 1  
  
        #complete list of candidates who received votes
        each_candidate.add(row[2])
        new_candidate_list = list(each_candidate)
        

        if row[2] == "Li":
            li_votes += 1
        elif row[2] == "Khan":
            khan_votes += 1   
        elif row[2] == "Correy":
            correy_votes += 1
        elif row[2] == "O'Tooley":
            otooley_votes += 1
            
        li_percent = round((li_votes / total_votes) * 100, 2)
        khan_percent = round((khan_votes / total_votes) * 100, 2)
        correy_percent = round((correy_votes / total_votes) * 100, 2)
        otooley_percent = round((otooley_votes/ total_votes) * 100, 2)

    

    candidates = {
        "Name" : ["Li", "Khan", "Correy", "O'Tooley"],
        "Percentage of Votes" : [li_percent, khan_percent, correy_percent, otooley_percent],
        "Total Number of Votes" : [li_votes, khan_votes, correy_votes, otooley_votes]
    }
    

    #adding number of votes for each candidate into a list
    votes_bycandidates = []
    votes_bycandidates.append(li_votes)
    votes_bycandidates.append(khan_votes)
    votes_bycandidates.append(correy_votes)
    votes_bycandidates.append(otooley_votes)

    #sorting the list in ascending order to find out the highest number of votes
    votes_bycandidates.sort()
    print(votes_bycandidates)
    print(f"Winner is: ", votes_bycandidates[-1])
    
    
    ############ A N A L Y S I S #################
    print("Election Results \n--------------------------")
    print(f"Total votes: {total_votes} \n--------------------------")
    #print(f"Khan: {candidates["Percentage of Votes"][2]} ({candidates["Total Number of Votes"][2]})") 
    print("Khan: {}% ({})".format(candidates["Percentage of Votes"][1], candidates["Total Number of Votes"][1])) 
    print("Correy: {}% ({})".format(candidates["Percentage of Votes"][2], candidates["Total Number of Votes"][2])) 
    print("Li: {}% ({})".format(candidates["Percentage of Votes"][0], candidates["Total Number of Votes"][0])) 
    print("O'Tooley: {}% ({})".format(candidates["Percentage of Votes"][3], candidates["Total Number of Votes"][3]))
    print("--------------------------") 

    
    
   


 