# Typecasting = the process of converting a variable from one data type to another
#               str(), int(), float(), bool()

name = "Kalana"
age = 25
gpa = 3.2
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))


# Typecasting examples
gpa = int(gpa)

print(gpa)

# Converting age to string
age = str(age)
print(age)

age += "1"

print(age)


# Converting name to boolean
name = bool(name)
print(name)