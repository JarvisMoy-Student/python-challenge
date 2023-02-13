import os
import csv

budgetdata_csv = os.path.join("Resources", "budget_data.csv")
# use open command to read file
with open(budgetdata_csv) as CSVFile:
    #setup reader for the CSV file
    csvReader = csv.reader(CSVFile, delimiter=',')
    # read the row of headers
    csvHeader = next(csvReader)
    # setting variable for totalmonths
    totalmonths = 0 

    # setting variable for maximum
    mostprofit = 0
    monthprofitmost = ""

    # setting variable for minimum
    mostlosses = 777777777777
    monthlossmost = ""

    # seting variable for total
    total = 0
    
    #setting variable for change
    change = 0

    # creating index that apppend data will go for variable
    change_profit_loss = []

    # setting initial varibale for average
    average = 0
    
    # setting for loop to look at each row
    for row in csvReader:
        
        # Setting variable within loop for net_change
        net_change = float(row[1]) - float(change)
        # appending net_change solution to change_profit_loss list
        change_profit_loss.append(net_change)
        #change_profit_loss_Dict[row[0]] = net_change
        totalmonths = totalmonths + 1
        change = float(row[1])
        # total += row[1]
        total = total + float(row[1])

    #for x, y in change_profit_loss_Dict.items():
       
        if float(net_change) > mostprofit:
            mostprofit = float(net_change)
            monthprofitmost = row[0]

        if float(net_change) < mostlosses:
            mostlosses = float(net_change)
            monthlossmost = row[0]

# variable that will hold average change solution    
avg_change = (sum((change_profit_loss[1:])))/(len(change_profit_loss[1:]))

# writing to new text file in different folder      
out_file = open("./Analysis/Pybank.txt", 'w')

#output that will show on txt file
out_file.write(f"Financial Analysis\n\n-------------------------------\n\nTotal Months: {totalmonths}\n\nTotal: ${round(total)}\n\nAverage Change : ${round(avg_change, 2)}\n\nGreatest Increase in Profits: {monthprofitmost} (${round(mostprofit)})\n\nGreatest Decrease in Profits: {monthlossmost} (${round(mostlosses)})")

#close file
out_file.close()

