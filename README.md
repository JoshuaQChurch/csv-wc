# CSV Word Count
*Convenient way to count the columns, rows, and cells of a csv file.*

## Setup 
1. Download and install [Python 3.](https://www.python.org/downloads/)
    * Uncheck the box *Install launcher for all users* (unless you have administrator privileges on your device) 
    * Check the box *Add Python 3.X.X to PATH (X denotes whatever version of Python you download at this time)*
    
2. Install additional dependencies
    * Open Terminal 
    * Enter the following command:
      * pip install pandas
      
 ## How to use
 Open up a Terminal shell
 

#### Single csv file
    $ python wc.py file.csv

#### Multiple csv files
    $ python wc.py file1.csv file2.csv

#### All csv files in current directory
    $ python wc.py . 
 
#### File not in same directory as script
    $ python wc.py path/to/file/file.csv
    
#### All csv files in different directory
    $ python wc.py path/to/file/. 


## Alias suggestion
In order to eliminate the need to type *python wc.py file.csv* each time,
I would suggest using an alias. 
#### 1. Place *wc.py* in a constant directory (a directory from which it won't move)
#### 2. Open *bash_profile* and enter the following:
     alias csv="python ~/path/to/script/wc.py "
#### 3. Now you can do the following:
      $ csv file.csv 


 
