# default arguments = A default value for certain parameters
#                     default is used when that argument is omitted
#                     make your functions more flexible, reduces # of arguments
#                     1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary


def net_price(list_price, discount, tax):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500, 0, 0.05))
    
# ------- in more times discount and tax is same, means those two parameters have default values 

def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500))


# ------- if somebody has a discount. this function would also accept up to two additional arguments
# -- if function pass the discount the use that one rather than the default one

def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500, 0.1))
print(net_price(500, 0.1, 0))


# -----------------------------------------------------------------------
# ----------------- Exercise --------------------------------------------
#      - count up timer -

import time

def count(end, start=0):            # if you use default argument, you want use after the positional argument
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!")

count(10)
count(30, 15)