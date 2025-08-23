# 2D List - list made up a list

fruits =        ["apple", "orange", "banana", "coconut"]
vegetables =    ["celery", "carrots", "potatoes"]
meats =         ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

# to declare a 2D array can done below as well 

groceries = [["apple", "orange", "banana", "coconut"], 
             ["celery", "carrots", "potatoes"], 
             ["chicken", "fish", "turkey"]]

print(groceries)              # access the all the list
print(groceries[0][0])        # access the one list item in 2d list, row number[], column number[]


# --------------------------------------------------
# ----------- if you want to iterate the elements from the 2D list -------
# ----- you can use nested loop as well ----------------------------------

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()

# you can also use 2D sets and tuples as well 


# ----------------- Exercise -------------------------------------------
# ----------------- 2D keypad (like mobile phone) ----------------------

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()

# if you need a grid or matrix of data, a 2D collection would work perfect 





