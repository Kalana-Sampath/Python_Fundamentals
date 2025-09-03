# class variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class

# ------------ * instance variables are defined inside of the constructor -------------
# ---------------------- instance variables each object has their own version. --------

class Student:

    class_year = 2024         # class variable
    num_students = 0
    
    def __init__(self, name, age):        
        self.name = name              
        self.age = age     
        
# this code always be executed when we instantiate an object. take the number of studentss and increment it
# by one each time we construct a new student object, if we are modifying a class variable, in place of self, 
# we will use the name of the class 
            
        Student.num_students += 1


student1 = Student("Spongebob", 30)                    
student2 = Student("Patrick", 35)

print(student1.name)
print(student1.age)
print(student1.class_year)
print()
print(student2.name)
print(student2.age)
print(student2.class_year)
# # ------- is good practice to access a class variable by the name of the class, rather than any object created from
# # the class
print()
print(Student.class_year)

print(Student.num_students)     # we are constructing two student objects. then the output is 2

# -------- print all class variables ------------------------------------
print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
