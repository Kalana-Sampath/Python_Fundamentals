# Python reading files (.txt, .json, .csv)

file_path = "61.reading files/employees.txt"

with open(file_path, "r") as file:
    content = file.read()
    print(content)
  


# ------ if the file extension was not added(forget to add) then it will interrupt our program --
# -- we can use excaption handling ----------

file_path = "61.reading files/employees"

try: 
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found")



# ---- if the file use the permission dinied ----------------------------------------------
# -- we can use excaption handling ----------

file_path = "61.reading files/employees.txt"

try: 
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")



# ------ read a JSON file ----------------------------------------------------

import json 

file_path = "61.reading files/employees.json"

try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content)
        print(content["name"])         # with the daya of json you could a value using a key 
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file") 



# ------ read a CSV file ----------------------------------------------------

import csv 

file_path = "61.reading files/employees.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        # with the csv file all the data in collection way, we want to iterate over line by line
        for line in content:
            print(line)
            print(line[0])          # to get the specified column
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")  


