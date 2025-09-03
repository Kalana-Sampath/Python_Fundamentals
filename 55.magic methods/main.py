# Magic methods = Dunder methods (double underescore) __init__, __str__, __eq__
#                 They are automatically called by many of Python's built-in operations.
#                 They allow developers to define or customize the behavior of objects

class Book:
    
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author 
        self.num_pages = num_pages
    
    # ------------------------------------------------------
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    # we can return the string representation of the object

    # ------------------------------------------------------
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    # we are using dunder equals to compare if two objects are equal 

    # ------------------------------------------------------
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    # we use dunder less than(lt) and greater than(gt) to compare two obeject attributes like (eg:- num_pagess) 

    # ------------------------------------------------------
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"
    # we use dunder add method to add two object attributes

    # ------------------------------------------------------
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    # we use dunder contains method to searching for a keyword in an object 

    # ------------------------------------------------------
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' was not found"
    # we use dunder getitem method to get the attribute value according their key 

# ------------------------------------------------------

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter and The Philosopher's Stone", "J.K. Rowling", 223)
book3 = Book("The Lion, the witch and the Wardrobe", "C.S. Lewis", 172)

print(book1)

# ------------------------------------------------------

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("The Hobbit", "J.R.R. Tolkien", 223)

print(book1 == book2)

# ------------------------------------------------------

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("The Hobbit", "J.R.R. Tolkien", 223)

print(book1 > book2)
print(book1 < book2)

# ------------------------------------------------------

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("The Hobbit", "J.R.R. Tolkien", 223)

print(book1 + book2)

# ------------------------------------------------------

book3 = Book("The Lion, the witch and the Wardrobe", "C.S. Lewis", 17)

print("Lion" in book3)

# ------------------------------------------------------

book3 = Book("The Lion, the witch and the Wardrobe", "C.S. Lewis", 17)

print(book3['title'])
print(book3['author'])
print(book3['num_pages'])
print(book3['audio'])