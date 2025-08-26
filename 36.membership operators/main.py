# Membership operators = used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set, or dictionary)
#                        1. in
#                        2. not in

word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")


# we can use - not in - also

if letter not in word:
    print(f"{letter} was not found")
else:
    print(f"There is a {letter}")
    

# --------------------------------------------
# --- another example -----------------------

students = {"Kalana", "Sampath", "Nimal"}

student = input("Enter the name of a student: ")

if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} was not found")



# -----------------------------------------------------------
# --- another example for dictionaries-----------------------

grades = {"Kalana": "A", 
          "Sampath": "B", 
          "Nimal": "C"}

student = input("Enter the name of a student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")      # {grade[student]} - this will return a value, given key / index operator
else:
    print(f"{student} was not found")



# -----------------------------------------------------------
# --- another example ---------------------------------------

email = "Kalana@gmail.com"
email = "Kalana@gmailcom"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")







