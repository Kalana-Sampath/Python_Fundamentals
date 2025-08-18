# input() = A function that prompts the user to enter data 
#           Returns the entered data as a string

# ------------------------------------------------------------
# Example of using input() to get user input
input("What is your name?: ")

name = input("What is your name?: ")
age = input("How old are you?: ")

print(f"Hello, {name}!")
print(f"You are {age} years old")


#-----------------------------------------------------------
# Example of using input() to get user input and convert it to an integer
name = input("What is your name?: ")
age = input("How old are you?: ")

age = int(age)
age = age + 1 


print(f"Hello, {name}!")
print("HAPPY BIRTHDAY!")
print(f"You are {age} years old")


# ----------------------------------------------------------
# Get the user input as a int (default it is a string)
name = input("What is your name?: ")
age = int(input("How old are you?: "))

age = age + 1 


print(f"Hello, {name}!")
print("HAPPY BIRTHDAY!")
print(f"You are {age} years old")


# ----------------------------------------------------------
# Exercise 1 Rectangle Area Calc

length = float(input("Enter the length: "))
width = float(input("Enter the width:"))

area = length * width 

print(f"The area is: {area}cm²")     # type a superscript 2 after the cm to get the square symbol
                                     # Numlock on and type 0178 + alt


# ----------------------------------------------------------
# Exercise 2 Shopping Cart Program 

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(total)
s
# f-string to format the output
# add the item, quantity and total to the print statement
print(f"You have bought {quantity} x {item}/s")
print(f"Your total is ${total}")


