# "Duck typing" = Another way to achive polymorphism besides Inheritance 
#                 Object must have the minimum necessary attributes/methods
#                 "If it look like a duck and quacks like a duck, it must be a duck."     


class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Car:
    
    def horn(self):
        print("HONK!")
        
#     # Exception has occurred: AttributeError
#     #'Car' object has no attribute 'speak' - it get the error because, Object must have the 
#     #                                        minimum necessary attributes/methods 
#     # In this case minium method is speak() 

    def speak(self):
        print("HONK!")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()


# --------------------------------------------------
# ---- animals inherit this alive attribute --------

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Car:
    
    def horn(self):
        print("HONK!")
        
    # Exception has occurred: AttributeError
    #'Car' object has no attribute 'speak' - it get the error because, Object must have the 
    #                                        minimum necessary attributes/methods 
    # In this case minium method is speak() 

    def speak(self):
        print("HONK!")
        
    # Exception has occurred: AttributeError
    # 'Car' object has no attribute 'alive'  - it get the error because, car obeject has no alive attribute
   
    alive = False      # add the alive attribute

    animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)