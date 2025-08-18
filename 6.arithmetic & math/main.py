# friends = 5

# Addition
friends = friends + 1
# augmeted assignment operator
friends += 1
# Subtraction
friends = friends - 2
# augmeted assignment operator
friends -= 2
# Multiplication
friends = friends * 3
# augmeted assignment operator
friends *= 3
# Division
friends = friends / 2
# augmeted assignment operator
friends /= 2
# exponentiation
friends = friends ** 2
# augmeted assignment operator
friends **= 2
# modulus
friends = friends % 3
# augmeted assignment operator
friends %= 3


print(friends)


#--------------------------------------------------
# build in math functions

x = 3.14
y = 4
z = 5

result = round(x)  # rounds to the nearest integer
result = abs(y)  # returns the absolute value
result = pow(z, 2)  # raises z to the power of 2
result = max(x, y, z)  # returns the maximum value
result = min(x, y, z)  # returns the minimum value

print(result)  

#--------------------------------------------------
# math class
# math module provides access to mathematical functions

import math

x 9.9 

print(math.pi) # prints the value of pi
print(math.e)  # prints the value of e
result = math.sqrt(x)  # calculates the square root of x
result = math.ceil(x)  # rounds x up to the nearest integer
result = math.floor(x)  # rounds x down to the nearest integer

print(result)  


#--------------------------------------------------
# Exercise 1: Circumference of a Circle

import math

radius = float(input("Enter the radius of a circle: "))

circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference, 2)}cm")  # rounding to 2 decimal places


#--------------------------------------------------
# Exercise 2: Area of a Circle

import math

radius = float(input("Enter the radius of a circle: "))

area = math.pi * pow(radius, 2)

print(f"The area of the circle is: {round(area, 2)}cm²")  # rounding to 2 decimal places


#--------------------------------------------------
# Exercise 3: hypotenuse of a Right Triangle

import math

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))

hypotenuse = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"The length of the hypotenuse is: {round(hypotenuse, 2)}")  # rounding to 2 decimal places




