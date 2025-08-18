# if = Do some code only IF some condition is True
#      Else do something else 

# --------------------------------------------------
age = int(input("Enter your age: "))

if age >= 18:
    print("You are now signed up!")
else:
    print("You must be 18+ to sign up!")


# --------------------------------------------------
# if statements can be used to check multiple conditions

age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to sign up!")   # you would be careful with the order of your conditions
elif age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't been born yet!")
# elif age >= 100:
#     print("You are too old to sign up!")      # after the check the age > 18 then not checked age > 100 therefore 
                                                #  you would be careful with the order of your conditions
else:
    print("You must be 18+ to sign up")


# --------------------------------------------------
# another example of if statements 

response = input("Would you like food? (Y/N): ")

if response == "Y":
    print("Have some food!")
else: 
    print("No food for you!")


# --------------------------------------------------
# another example of if statements 

name = input("Enter your name: ")

if name == "":
    print("You did not type in your name!")
else:
    print(f"Hello {name}")


# --------------------------------------------------
# boolean with if statements

online = True

if online: 
    print("The user is online!")
else:
    print("The user is offline!")


    

