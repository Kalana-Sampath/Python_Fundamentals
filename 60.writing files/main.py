# Python writing files (.txt, .json, .csv)


txt_data = "I like pizza!"

file_path = "60.writing files/output.txt"

with open(file_path, "w") as file:
    file.write(txt_data)
    print(f"txt file '{file_path}' was created")



# ------- there are different mode exists -- like x for,we will write a file if that file doesn't already
#  -- exist -

txt_data = "I like pizza!"

file_path = "60.writing files/output.txt"

try:                                       # if the file already exist then we can handle using, try catch block
    with open(file_path, "x") as file:
        file.write(txt_data)
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")



# ------ there is a mode, 'a' for to append. Any new data will be appended to that file 


txt_data = "I like pizza!"

file_path = "60.writing files/output.txt"

try:                                       
    with open(file_path, "a") as file:
        file.write("\n" + txt_data)                     # new line with update data
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")



# --------- Let's work with the collection. ------------------------------------

employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]

file_path = "60.writing files/emplayees.txt"

try:
    with open(file_path, "w") as file:
# In order for us to write each item within a list, we will need to iterate over it using some sort of loop
        for employee in employees:
            file.write(employee + "\n")
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")



# --------------------------------------------------------------------------
# ------ Outputting a JSON file, JSON file is made of key value pairs

import json

employee = {
    "name": "Spongebob",
    "age": 30,
    "job": "cook"
}

file_path = "60.writing files/employees.json"

try:
    with open(file_path, "w") as file:
# # we can use indent keyword how many spaces you want through each key value pairs 
        json.dump(employee, file, indent=4)      # dump method will convert our dictionary to a JSON string 
        print(f"json file '{file_path} was created")
except FileExistsError:
    print("That file already exists!")



# --------------------------------------------------------------------------
# ------ Work with csv file, (CSV mean comma separeted values) 

import json 
import csv

employees = [["Name", "Age", "Job"],
             ["Spongebob", 30, "Cook"],
             ["Patrick", 97, "Unemployed"],
             ["Sandy", 27, "Scientist"]]

file_path = "60.writing files/employees.csv"

try:
    with open(file_path, "w", newline="") as file:  # writer method do the new line automatically, to avoid that we use (newline = " " )
        writer = csv.writer(file)           # writer is a object. It provides methods for writing data to a csv
                                            # file  
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")


