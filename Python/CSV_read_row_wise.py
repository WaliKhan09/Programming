# Python code to read a CSV file row wise

# Importing required module
import csv

# Opening CSV file in a variable.
with open("Python\\Sample.csv", newline='') as f:

    # Reading CSV file
    ereader = csv.DictReader(f)

    # Initializing loop to get CSV file data in variable.
    for row in ereader:
        a = row['Title']
        b = row['Author']
        c = row['Pages']

        # Printing the values
        print("Title = " + a)
        print("Author = " + b)
        print("Pages = " + c)
