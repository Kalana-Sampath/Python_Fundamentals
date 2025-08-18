# Variable = A container for a value (string, integer, float, boolean)
#            A variable behaves as if it was the value it contains 

first_name = "Kalana"

print(first_name)


f-string - To use formatted string literals, begin a string with f or F before the opening quotation mark or 
triple quotation mark. Inside this string, you can write a Python expression between { and } characters that 
can refer to variables or literal values.


# Strings
first_name = "Kalana"
food = "pizza"

print(f"Hello {first_name}")     # f mean format
print(f"You like {food}")


# Integers
age = 25
quantity = 10
num_of_students = 30

print(f"You are {age} years old")
print(f"You have {quantity} apples")
print(f"There are {num_of_students} students in the class")


# Floats
price = 19.99
gpa = 3.2
distance = 5.5

print(f"The price of the item is ${price}")
print(f"Your GPA is: {gpa}")
print(f"You ran {distance}km")


# Booleans
is_student = True

print(f"Is the person a student? {is_student}")

if is_student:
    print("The person is a student.")
else:
    print("The person is not a student.")


fore_sale = False

if fore_sale:
    print("That item id for sale")
else:
    print("That item is NOT available")



