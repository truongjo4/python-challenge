# Importing all libraries
import os
import csv

# setting path to data csv file
csvpath = os.path.join('Resources','election_data.csv')

# Open file and allow read only
with open(csvpath, encoding="utf-8") as csvfile:


    #Skip counting headers
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    print(csv_header)