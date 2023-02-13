import os
import csv

ElectionData_csv = os.path.join("Resources", "election_data.csv" )

with open(ElectionData_csv) as csvfile:
    # setup variable for csvReader 
    csvReader = csv.reader(csvfile, delimiter = ",")

    #setup variable to skip header
    csvHeader = next(csvReader)
    
    #variable that will start intitial count of voters
    Number_voters = 0
    # variable that will hold the list of candidates
    List_of_Candidates = []
    # variable that will hold dictionary of vote_count_dict
    Vote_count_Dict ={}
    # variable that will hold dictionary of per_vote_dict
    Per_Vote_Dict = {}
    #Setting variable for intial max and starting point for highest count
    Highest_count = 0
    # setting variable to count the highest count to that willl hold the winner
    Winner = ''
    # setting up body empty list to hold body text to show o seperate lines
    body = []

    # variable that will write to different text file
    out_file = open("./Analysis/PyPoll.txt", "w")

    for row in csvReader:
        # Number_voters = Number_voters + 1
        Number_voters += 1
        # if statement to append names that are not in List_of_Candidates[] list
        if row[2] not in List_of_Candidates: 
            List_of_Candidates.append(row[2])
        # setting eacch unique value in list to a numeric value
            Vote_count_Dict[row[2]] = 1

        else:
            Vote_count_Dict[row[2]] += 1

    # setting x,y values to items in Vote_count_Dict Dictionary
    for x, y in Vote_count_Dict.items():

        #creating value to hold per_vote_count solution 
        Per_Vote_Dict = (y*100/Number_voters) 
        # appending the rounded solution to body[] list
        body.append((f"{x}: {round(Per_Vote_Dict, 3)}% ({y})"))  
        # setting up if statment to identify winner
        if y > Highest_count:
            Highest_count = y
            Winner = x


    # output to text file
    out_file.write(f"\n\n")
    out_file.write(f"Election Results")
    out_file.write(f"\n\n")
    out_file.write(f"--------------------")
    out_file.write(f"\n\n")
    out_file.write(f"Total Votes: {Number_voters}")
    out_file.write(f"\n\n")
    out_file.write(f"--------------------")
    out_file.write(f"\n\n")
    out_file.write(f"{body[0]}")
    out_file.write(f"\n\n")
    out_file.write(f"{body[1]}")
    out_file.write(f"\n\n")
    out_file.write(f"{body[2]}")
    out_file.write(f"\n\n")
    out_file.write(f"--------------------")
    out_file.write(f"\n\n")
    out_file.write(f"Winner: {Winner}")
    out_file.write(f"\n\n")
    out_file.write(f"--------------------")



