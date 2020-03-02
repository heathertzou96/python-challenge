import os
import csv

csvpath = os.path.join('..', 'PyPoll', 'election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')

    csvheader = next(csvreader)
    
    total_votes = 0
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
        #using set to get the unique values from the Candidate column and then converting back to a list
        #https://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python
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
    

    #trying to get the ultimate winner's name based on most number of total votes (although you can tell based on above results... just wanted to experiment)
    #I used the sorted method to sort list according to second element in sublist 
    #https://www.geeksforgeeks.org/python-sort-list-according-second-element-sublist/ 
    winner_list = []
    winner_list.append(("Li", li_votes))
    winner_list.append(("Khan", khan_votes))
    winner_list.append(("Correy", correy_votes))
    winner_list.append(("O'Tooley", otooley_votes))
    find_winner = sorted(winner_list, key = lambda x: x[1])
    #print(find_winner)
    ultimate_winner = find_winner[-1]
    #print(find_winner[-1])
    ultimate_person = ultimate_winner[0]
    #print(ultimate_person)
    

    ################# A N A L Y S I S ####################
    #print(new_candidate_list)
    print("Election Results \n--------------------------")
    print(f"Total votes: {total_votes} \n--------------------------")
    print("Khan: {}% ({})".format(candidates["Percentage of Votes"][1], candidates["Total Number of Votes"][1])) 
    print("Correy: {}% ({})".format(candidates["Percentage of Votes"][2], candidates["Total Number of Votes"][2])) 
    print("Li: {}% ({})".format(candidates["Percentage of Votes"][0], candidates["Total Number of Votes"][0])) 
    print("O'Tooley: {}% ({})".format(candidates["Percentage of Votes"][3], candidates["Total Number of Votes"][3]))
    print("--------------------------") 
    print(f"Winner: {ultimate_person}")
    print("--------------------------") 

    
    textfile = open("results.txt", "w")
    textfile.write("Election Results \n--------------------------\n")
    textfile.write(f"Total votes: {total_votes} \n--------------------------\n")
    textfile.write("Khan: {}% ({}) \n".format(candidates["Percentage of Votes"][1], candidates["Total Number of Votes"][1])) 
    textfile.write("Correy: {}% ({}) \n".format(candidates["Percentage of Votes"][2], candidates["Total Number of Votes"][2]))
    textfile.write("Li: {}% ({}) \n".format(candidates["Percentage of Votes"][0], candidates["Total Number of Votes"][0])) 
    textfile.write("O'Tooley: {}% ({}) \n".format(candidates["Percentage of Votes"][3], candidates["Total Number of Votes"][3]))
    textfile.write("--------------------------\n") 
    textfile.write(f"Winner: {ultimate_person} \n")
    textfile.write("--------------------------\n") 

   


 