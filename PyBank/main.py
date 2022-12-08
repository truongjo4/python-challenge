# Importing all libraries
import os
import csv

# setting path to data csv file
csvpath = os.path.join('Resources','budget_data.csv')

# Open file and allow read only
with open(csvpath, encoding="utf-8") as csvfile:


    # Skip counting headers
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
        

    # Getting total number of months in dataset + net total amount
    ## Empty lists allow tracking for later
    net_amount = []
    date = []
    # Each row = new month - so simply counting
    total_months = 0
    for row in csvreader:
        date.append(row[0])
        # Have opportunity to get all the profits here and store in list for summing
        net_amount.append(int(row[1]))
        total_months += 1
    
    total_amount = sum(net_amount)

    # Getting changes in profit/losses + average
    ## Average changes of profit over whole period = (next month - previous month/total number of months)
    change_profit = []
    # -1 in range so code doesn't break as we have i+1
    for i in range(0, len(net_amount)-1):
        change_profit.append(net_amount[i+1]-net_amount[i])
    average_profit = round(sum(change_profit)/len(change_profit),2)
    

    # Getting greatest increase in profits
    ## + 1 on date to sync up the list as change_profit does not include the first month
    largest_profit = max(change_profit)
    largest_profit_index = change_profit.index(largest_profit)
    largest_profit_date = date[largest_profit_index + 1]

    # Getting greatest decrease in profits
    largest_loss = min(change_profit)
    largest_loss_index = change_profit.index(largest_loss)
    largest_loss_date = date[largest_loss_index + 1]

#Use function to avoid reptition
def summary():
    return f'Financial Analysis\n--------------------\n'\
    f'Total Months: {total_months}\n'\
    f'Total: ${total_amount}\n'\
    f'Average Change: ${total_amount}\n'\
    f'Greatest Increase in Profits: {largest_profit_date} (${largest_profit})\n'\
    f'Greatest Decrease in Profits: {largest_loss_date} (${largest_loss})\n'\


print(summary())

# Set path for output file - calling text file financial_summary
output_file = os.path.join("Analysis","financial_summary.txt")

# Insert in the financial analysis
with open(output_file, "w") as txtfile:
    txtfile.write(summary())