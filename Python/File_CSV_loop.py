# Python code to check if a file exist in a folder
# whose name is equal to the row data of csv file.

# Importing required libraries
import os
import csv

# Opening CSV file in a variable.
with open("Book.csv", newline='') as f:

    # Reading CSV file
    ereader = csv.DictReader(f)

    # Initializing loop to get CSV file data in a variable.
    for row in ereader:
        b = row['color']

        # Initializing loop for the files in the defined folder
        for filename in os.listdir("/Users/walikhan/Work/Python_YouTube_Auto/vid"):

            # Applying condition to check if file name is equal to CSV row data or not.
            if ((filename.endswith(".mp4")) & (filename[:-4] == b)): # here "(filename.endswith(".mp4"))" is used for checking for a particular file type.
                print(filename)
            else:
                continue
