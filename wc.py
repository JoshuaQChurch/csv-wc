# Author: Joshua Church
# Purpose: Count the number of rows, columns, and cells of a csv file. 

import os
import sys
from pandas import read_csv


def parse_args():
    argv = sys.argv 
    argc = len(argv)
    csv_files = []

    # Verify that the user passes at least one argument
    if argc < 2: 
        error()

    # Store arguments (ignoring this file)
    args = argv[1:]

    for arg in args:

        # Check if user passes contents of 
        # current working directory
        if arg == '.':
            path = os.getcwd() 
            files = os.listdir(path) 

            # Check to see if there are 
            # any .csv files in the current directory
            for file in files:
                if file.endswith(".csv"):
                    fullpath = os.path.join(path, file)
                    csv_files.append(fullpath) 
        
        # Check if user passes contents of 
        # a different working directory
        elif arg.endswith('.'):
            # Make sure we pull the contents of the 
            # directory. 
            if arg[-2] == "\\" or arg[-2] == "/":
                path = arg[:-1]
                files = os.listdir(path)
                for file in files:
                    if file.endswith(".csv"):
                        fullpath = os.path.join(path, file)
                        csv_files.append(fullpath)
        
        # If the file is a .csv file, append it
        elif arg.endswith(".csv"):
            csv_files.append(arg)   

    # Verify that a csv file has been provided 
    if not len(csv_files):
        error()
    
    else:
        return csv_files

# Print the information about the csv file. 
def csv_info(files):
    for f in files: 
        csv = read_csv(f) 
        rows = len(csv.count(axis=1))
        columns = len(csv.count(axis=0))
        cells = rows*columns 

        print("\nFilename: " + os.path.basename(f))
        print("--> Rows: " + str(rows))
        print("--> Columns: " + str(columns))
        print("--> Cell Count: " + str(cells))    
    print("\n")


def error():
    print("\nPlease provide at least (1) csv file.\n")
    exit()  
    
    
csv_files = parse_args()
csv_info(csv_files)  



