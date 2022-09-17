# Python code to check if a file exist in a folder
# whose name is equal to the row data of csv file.

# Importing required libraries
import os
import csv

# Opening CSV file in a variable.
with open("Python\\Colors.csv", newline='') as f:

    # Reading CSV file
    ereader = csv.DictReader(f)

    # Initializing loop to get CSV file data in a variable.
    for row in ereader:

        # Getting values in variables
        a = row['name']
        b = row['hex']

        # Initializing loop for the files in the defined folder
        for filename in os.listdir("Python\\Sample_videos"):

            # Applying condition to check if file name is equal to CSV row data or not.
            if ((filename.endswith(".mp4")) & (filename[:-4] == b[1:])): # here "(filename.endswith(".mp4"))" is used for checking for a particular file type.
                print("File named",filename,"found in dir.")
            else:
                continue
