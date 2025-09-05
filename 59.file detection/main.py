# Python file detection

import os

# Change current directory to the script's folder
os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_path = "test.txt"
file_path = "test.pdf"

file_path = "stuff/test.txt"

# use the absoulute file path
file_path = "C:/example/example/test.txt"


if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
else:
    print("That location doesn't exist")
    

# -----------------------------------------------------------------------------------------------------
# There is a built-in method of 'is file' check to see if that file is in fact a file and not a directory

import os

# Change current directory to the script's folder
os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_path = "stuff/test.txt"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
    
    if os.path.isfile(file_path):
        print("That is a file")
else:
    print("That location doesn't exist")


# -----------------------------------------------------------------------------------------------------
# There is a built-in method of 'is dir' check to see if that file is in fact a directory and not a file

import os

# Change current directory to the script's folder
os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_path = "stuff/test1"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
    
    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print("That location doesn't exist")