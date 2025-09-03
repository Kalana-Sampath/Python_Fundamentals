 
# object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex. phone, cup, book
#          You need a "class" to create many objects
# class  = (blueprint) used to design the structure and layout of an object

from car import Car

class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale              
        
#   *********** With classes, they can take up a lot of space. For better organization, 
#  you can place with a new python file 

        
car1 = Car("Mustang", "2024", "red", False)
car2 = Car("Corvette", "2025", "blue", True)
car3 = Car("Charger", "2026", "yellow", True)

print(car1)

# ----------- if we print the car obejct, we are get the memory address of this car obeject where it is located 
# we are going to access one of the attributes found within this car, we will follow the name within the car with a dot 
# this dot is konwn as the attribute access operator. -----------

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

print()

print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)

print()

print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)

car1.drive()
car1.stop()

print()

car2.drive()
car2.stop()

print()

car1.describe()

