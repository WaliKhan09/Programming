# Python code to run a loop for the number of files in a folder.

# Importing required libraries
import os

# Initializing loop for the files in the defined folder
for filename in os.listdir("/Users/walikhan/Work/Python_YouTube_Auto/vid"):

    # Applying condition to check for a particular file type
    if filename.endswith(".mp4"):

        # Printing the file name
        print("File name with extension", filename)

        # Complete file path
        print("File path - ",os.path.join("/Users/walikhan/Work/Python_YouTube_Auto/vid", filename))

        # to remove last characters(or file extension)
        print("File name without extension", filename[:-4])

    else:
        continue
