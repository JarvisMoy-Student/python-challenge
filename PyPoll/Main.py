import os
import csv

ElectionData_csv = os.path.join("Resources", "election_data.csv" )

with open(ElectionData_csv) as csvfile:
    # setup variable for csvReader 
    csvReader = csv.reader(csvfile, delimiter = ",")

    #setup variable to skip header
    csvHeader = next(csvReader)

    Number_voters = 0
    List_of_Candidates = []
    Vote_count_Dict ={}
    Per_Vote_Dict = {}
    Highest_count = 0
    Winner = ''
    body = []

    out_file = open("./Analysis/PyPoll.txt", "w")
    for row in csvReader:
        Number_voters = Number_voters + 1

        if row[2] not in List_of_Candidates: 
            List_of_Candidates.append(row[2])

            Vote_count_Dict[row[2]] = 1

        else:
            Vote_count_Dict[row[2]] += 1

    for x, y in Vote_count_Dict.items():


        Per_Vote_Dict = (y*100/Number_voters) 
        body.append((f"{x}: {round(Per_Vote_Dict, 3)}% ({y})"))  

        if y > Highest_count:
            Highest_count = y
            Winner = x


    
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



