
# multiple inheritance = inherit from more than one parent class
#                        C(A, B)

# multilevel inheritance = inherit from a parent which inherits from another parent 
#                          C(B) <- B(A) <- A 


class Prey:
    def flee(self):
        print("This animal is fleeing")

class Predator:
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):       # children class can inherit from more than one parent
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()

fish.flee()
fish.hunt()   # fish has both 



# ---------------------------------------------------------------------------------------
# ------------- multilevel inheritance, parent can inherit from another parent ----------

# create a animal class 

class Animal:
    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Prey(Animal):
    def flee(self):
        print("This animal is fleeing")

class Predator(Animal):
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):                    # rabbit inhetits parent's parent 
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):       # children class can inherit from more than one parent
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.eat()
rabbit.sleep()


# -------------------------------------------------------------------
# ---------- more expand --------------------------------------------

class Animal:
    
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):                    # rabbit inhetits parent's parent 
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):       # children class can inherit from more than one parent
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")


# ---------- * With these other classes, if you are not assigning any attributes or if you do not need any other 
# ------ initialization logic, you do not need a constructor. We'll implicitly use the constructor we inherit from
# -- the parent 

rabbit.eat()
rabbit.sleep()
rabbit.flee()

print()

hawk.eat()
hawk.sleep()
hawk.hunt()

print()

fish.eat()
fish.sleep()
fish.flee()
fish.hunt()

