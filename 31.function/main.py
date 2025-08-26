# function = A block of reusable code
#            place () after the function name to invoke it

def happy_birthday():
    print("Happy birthday to you!")
    print("You are old!")
    print("Happy birthday to you!")
    print()

happy_birthday()

 
# -----------------------------------------------

def happy_birthday(name):
    print(f"Happy birthday to {name}!")
    print("You are old!")
    print(f"Happy birthday to you!")
    print()
     
happy_birthday("Bro")            # With functions, you are able to send data directly to a function
happy_birthday("Steve")
happy_birthday("Joe")            


# -----------------------------------------------
# when you invoke a function, you can send more than one argument.

 
def happy_birthday(name, age):                 # you need a matching set of parameters
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print("Happy birthday to you!")
    print()
     
happy_birthday("Bro", 20)           
happy_birthday("Steve", 30)
happy_birthday("Joe", 40) 


# -----------------------------------------------
# ------- another example ----------------------

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("Kalana", 42.50, "01/01")



# -----------------------------------------------
# ------- another example ----------------------

# retrun = statement used to end a function 
#          and send a result back to the caller

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))



# -----------------------------------------------
# ------- another example ----------------------

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last     # Using the return statement, you can some data back to the place 
                                  # in which you can call a function

full_name = create_name("Kalana", "Sampath")

print(full_name)
    

