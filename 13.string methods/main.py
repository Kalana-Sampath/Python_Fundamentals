
name = input("Enter your full name: ")
phone_number = input("Enter your phone #: ")

result = len(name)              # it will give the length of the string
result = name.find(" ")         # first occrence of given character
result = name.find("K")           
result = name.rfind("a")         # last occrence of given characterm,  if the no sedult then return the -1
name = name.capitalize()         # capitalize the first letter of the string, and also return as a string
name = name.upper()              # uppercase the all character
name = name.lower()              # lowercase the all character 
result = name.isdigit()          # return either true or false,  all the character digit then return the true
result = name.isalpha()          # return true or false if the string have only alperbertical character
result = phone_number.count("-")                # count the amount of characters
phone_number = phone_number.replace("-", " ")   # replace one character using another 

print(help(str))      # get the all the string methods

print(phone_number)


#-------------------------------------------------------------
# ------- Exercise ----------------------------------------------

# Validate user input exercise
# 1. username is no more than 12 character
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")


if len(username) > 12:
    print("Your username can not be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}")


