# Decorator = A function that extends the behavior of another function
#             w/o modifying the base function 
#             Pass the base function as an argument to the decorator

# eg : add some sprinkles to the ice_cream
            # @add_sprinkles
            # get_ice_cream("Vanilla")
# adding something to the base function without changing it

# def add_sprinkles(func):
#     def wrapper():
#         print("*You add sprinkles 🍉*")
#         func()
#     return wrapper

# # necessary to add wrapper function, because we want execute the wrapper function when call the base function, at
# # that time only 

# @add_sprinkles
# def get_ice_cream():
#     print("Here is your ice cream 🍨")


# get_ice_cream()


# --------------------------------------------------------------------------
# -------------- add more than one decorator -------------------------------

# def add_sprinkles(func):
#     def wrapper():
#         print("*You add sprinkles 🍉*")
#         func()
#     return wrapper

# def add_fudge(func):
#     def wrapper():
#         print("*You add fudge 🍫*")
#         func()
#     return wrapper

# @add_sprinkles
# @add_fudge
# def get_ice_cream():
#     print("Here is your ice cream 🍨")


# get_ice_cream()



# ------------------- what if your base function accepts arguments ----------------------------------

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("*You add sprinkles 🍉*")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("*You add fudge 🍫*")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream 🍨")


get_ice_cream("vanilla")
print()
get_ice_cream("chocolate")