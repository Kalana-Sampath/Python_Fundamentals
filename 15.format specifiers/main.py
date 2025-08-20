# format specifiers = {value:flags} format a value based on what 
#                     flags are inserted

# .(number) = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify 
# :> = right justify
# :^ = center align 
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# : = insert a space before positive numbers
# :, = comma separator


price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is ${price1:.2f}")   # .2f mean 2 decimal, florting point numbers
print(f"Price 2 is ${price2:.2f}")
print(f"Price 3 is ${price3:.2f}")

# to allocate the display value after the collan 

print(f"Price 1 is ${price1:10}")   
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:10}")

# if you add 0 before the number then it would be zero pattern

print(f"Price 1 is ${price1:010}")   
print(f"Price 2 is ${price2:010}")
print(f"Price 3 is ${price3:010}")


# to left justify 

print(f"Price 1 is ${price1:<10}")  # then all of the spaces left after
print(f"Price 2 is ${price2:<10}")
print(f"Price 3 is ${price3:<10}")

# right justify also same

# center the number 

print(f"Price 1 is ${price1:^10}")  # then all of the spaces divided to left and right 
print(f"Price 2 is ${price2:^10}")
print(f"Price 3 is ${price3:^10}")

# want to add a positive sign before the number

print(f"Price 1 is ${price1:+}")  # add postive value with positive sign and negative value with negative sign
print(f"Price 2 is ${price2:+}")  
print(f"Price 3 is ${price3:+}")

print(f"Price 1 is ${price1: }")  # these also same the above, but not display positive sign
print(f"Price 2 is ${price2: }")  
print(f"Price 3 is ${price3: }")


# comma separator 

price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

print(f"Price 1 is ${price1:,}")   # each thoused places separate with tha comma
print(f"Price 2 is ${price2:,}")  
print(f"Price 3 is ${price3:,}")

# you can add some combination of flex also 

print(f"Price 1 is ${price1:+,.2f}")   # each thoused places separate with tha comma
print(f"Price 2 is ${price2:+,.2f}")  
print(f"Price 3 is ${price3:+,.2f}")

