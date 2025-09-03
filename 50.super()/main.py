# super() = Function used in a child class to call methods from a parent class (superclass).
#           Allows you to extend the functionality of the inherited methods

class Circle():
    def __init__(self, color, filled, radius)
        self.color = color
        self.filled = filled
        self.radius = radius

class Square:
    def __init__(self, color, filled, width)
        self.color = color
        self.filled = filled
        self.width = width

class Triangle:
    def __init__(self, color, filled, width, height)
        self.color = color
        self.filled = filled
        self.width = width
        self.height = height


# ---------------------------------------------------------------------------------------
# If we have to changes to one of these attributes, we would have to do so manually.
# for example if we want to replace, filled with is_filled then want to change all one manually, it is lot of work
# and might make mistake also, 
# --- * It is better to write your code once and try and reuse it.
# --- that why we use inheritance and the super function

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

# within the constructor of children classes, we have to call the constructor for the parent, also known as
# the super class of shape

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

circle = Circle(color="red", is_filled=True, radius=5)
square = Square(color="blue", is_filled=False, width=6 )
triangle = Triangle(color="yellow", is_filled=False, width=5, height=6 )

print(circle.color)
print(circle.is_filled)
print(f"{circle.radius}cm")

print()

print(square.color)
print(square.is_filled)
print(f"{square.width}cm")

print()

print(triangle.color)
print(triangle.is_filled)
print(f"{triangle.width}cm")
print(f"{triangle.height}cm")



# ------------ and also you colud, extend the functinality as well ---------------------------------

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

circle = Circle(color="red", is_filled=True, radius=5)
square = Square(color="blue", is_filled=False, width=6 )
triangle = Triangle(color="yellow", is_filled=False, width=5, height=6 )

circle.describe()
square.describe()
triangle.describe()

print()

print(circle.color)
print(circle.is_filled)
print(f"{circle.radius}cm")

print()

print(square.color)
print(square.is_filled)
print(f"{square.width}cm")

print()

print(triangle.color)
print(triangle.is_filled)
print(f"{triangle.width}cm")
print(f"{triangle.height}cm")



# --------------- we also have method overwriting ----------------------------------------------------

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"It is circle with an area of {3.14 * self.radius * self.radius}cm")

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

circle = Circle(color="red", is_filled=True, radius=5)
square = Square(color="blue", is_filled=False, width=6 )
triangle = Triangle(color="yellow", is_filled=False, width=5, height=6 )

circle.describe()

# This is called a method overwriting. If a child shares a similar method with a parent, you will use the child 
# version and not the parent 

# we can also extend the functionalitu using the super method, in the descibe method 
# eg:-

    # def describe(self):
    #     print(f"It is circle with an area of {3.14 * self.radius * self.radius}cm")
    #     super().describe       # *** like this ********* 

