# Polymorphism = Greek word that means to "have many forms or faces"
#                Poly = Many 
#                Morphe = Form 

#                TWO WAYS TO ACHIEVE POLYMORPHISM
#                1. Inheritance    =  An object could be treated of the same type as a parent class
#                2. "Duck typing"  =  Object must have necessary attributes/methods


from abc import ABC, abstractmethod

class Shape:
    
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return self.base * self.height * 0.5


shapes = [Circle(4), Square(5), Triangle(6, 7)]   # each object is a it's own class and also shape, mean have many forms or faces

for shape in shapes:
    print(f"{shape.area()}cm²")
    
 
# -----------------------------------------------------------------------------
# ---- what if we were to create a class that is completely unrelated to shapes

from abc import ABC, abstractmethod

class Shape:
    
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return self.base * self.height * 0.5

unrelated class
class Pizza:
    def __init__(self, topping, radius):
        self.topping = topping
        self.radius = radius
    
    
shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("pepperoni", 15)]   
  
for shape in shapes:
    print(f"{shape.area()}cm²")
    
# -----------------     
# Exception has occurred: AttributeError
# 'Pizza' object has no attribute 'area - then get error
# but we can iherit pizza from circle class

class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping
        
# our pizza is considered a pizza. It inherits from the circle class So, it also considered a circle, and our
# circle class inherits from the shape class.
# Our pizza has a three forms. Or pizza is considered a pizza. It's also considered a circle and it's also 
# considered a shape 

