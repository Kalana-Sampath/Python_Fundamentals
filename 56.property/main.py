# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
#             Benefit: Add additional logic when read, write, or delete attributes
#             Gives you getter, setter, and deleter method

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    @property
    def width(self):
        pass
    
    @property
    def height(self):
        pass
    
rectangle = Rectangle(3, 4)

print(rectangle.width)   

# when accessing the width and or the height, returned with whatever is within property methods of width and height
# but we want to do one change to the attributes
# we want a set a constructor attribute to private

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height           # using _ (underscore) - we can change these attribute to private 
    
    @property
    def width(self):
        return f"{self._width:.1f}cm"
    
    @property
    def height(self):
        return f"{self._height:.1f}cm"
    
rectangle = Rectangle(3, 4)

print(rectangle._width)   # we should not access the width or height directly out side of the class (Rectangle)  
                            # technically we can, but do not use like that way
                        

print(rectangle.width)      # we will access the height and width using getter method

# that how use getter method, we can add aditional login when read those attributes


# -----------------------------------------------------------------------------------------
# ------------- we can also add setter method ---------------------------------------------

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height           # using _ (underscore) - we can change these attribute to private 
    
    @property
    def width(self):
        return f"{self._width:.1f}cm"
    
    @property
    def height(self):
        return f"{self._height:.1f}cm"
    
    @width.setter 
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")
    
    @height.setter 
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")
    
rectangle = Rectangle(3, 4)

rectangle.width = 5
rectangle.height = -1

print(rectangle.width)
print(rectangle.height)

# when using the setter method, we can add aditional logic when writing or changing the attributes



# -----------------------------------------------------------------------------------------
# ------------- if you need a delete an attribute, there is a delete key word--------------

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height           # using _ (underscore) - we can change these attribute to private 
    
    @property
    def width(self):
        return f"{self._width:.1f}cm"
    
    @property
    def height(self):
        return f"{self._height:.1f}cm"
    
    @width.setter 
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")
    
    @height.setter 
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")
    
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted") 
    
    @height.deleter
    def height(self):
        del self._height
        print("height has been deleted") 
    
rectangle = Rectangle(3, 4)

rectangle.width = 5
rectangle.width = -1
rectangle.height = 6


del rectangle.width
del rectangle.height


