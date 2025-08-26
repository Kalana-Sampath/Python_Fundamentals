# ARBITRARY arguments
# *args =   allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#            * unpacking operator 
#            1. positional  2. default  3. keyword  4. ARBITRARY


# when we use the unpacking operator, the arguments that we pass into this function those are pack them into a 
# tuple

def add(*args):
      print(type(args))
    total = 0
    for arg in args:
        total += arg
    return total
    
print(add(1,2,3))


# -------------------------------------------------------
# -------------- another example ------------------------

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Kalana", "Sampath")

 
 
# -------------------------------------------------------
# the arguments that we pass into this function those are pack them into a dictionary

def print_address(**kwargs):
    print(type(kwargs))
    for value in kwargs.values():            # values method
        print(value)
    for key in kwargs.keys():                # keys method
        print(key)
    for key, value in kwargs.items():        # item method
        print(f"{key}: {value}")
    
print_address(street="123 Fake St.",
              city="Detroit",
              state="MI",
              zip="54321")                # we can pass varying amount of keyword arguments.

 
# ----------------------------------------------------------
# ------- Exercise -  use *args and **kwargs together ------
    
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")
    
    print(f"{kwargs.get('street')}")                                              # street in one line and city, 
    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")     # state and zip in another line  


    # if the aprartment is none (apt) then
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('street')}")

shipping_label("Kalana", "Sampath", 
               street="123 Fake St.",
               apt="100",
               city="Detroit",
               state="MI",
               zip="54321"
               )

