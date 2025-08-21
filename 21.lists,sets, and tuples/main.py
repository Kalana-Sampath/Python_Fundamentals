# collection = single "variable" used to store multiple values
#   List    = [] ordered and changeable. Duplicates OK
#   Set     = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple   = () ordered and unchangeble. Duplicate OK. Faster


# ------------------------------------------------------------
# --------------------- List [] -------------------------

fruits = ["apple", "orange", "banana", "coconut"]

print(fruits)
print(fruits[0])    # you can use the index operator to get the element 
print(fruits[:3])   # you can add start , end and steps index as well / [start : end : steps]
print(fruits[::2])


# you can iterate over them using,  for loop

for x in fruits:        
    print(x)

for fruit in fruits:        # use the singular name as x is more meanningfull 
    print(fruit) 


#----------------------------------------------------
# deferent method avilable in collection 

print(dir(fruits))            # get the all the attributes and methods

print(help(fruits) )          # if you want a description of each method


print(len(fruits))              # if you need a length (how many elements are within the collection)
print("apple" in fruits )       # using a -in- operator we can find a value within a collection
fruits[0] = "pineapple"           # we can change our value after create our list

for fruit in fruits:
    print(fruit)



# ---- available method in List -------------------

fruits.append("pineapple")       # add a element to the end of the list

for fruit in fruits:
    print(fruit)


fruits.remove("apple")             # to remove a element 
print(fruits)


fruits.insert(0, "pineapple")       # insert a element
print(fruits)


fruits.sort()                       # to sort a list
print(fruits)


# -------- in reverse alplabetical order first you need to sort and reverse -----------------

fruits.sort()
fruits.reverse()                    # to revers a list
print(fruits)


fruits.clear()                        # to clear a list 
print(fruits)


print(fruits.index("apple"))           # we can return a index of value

print(fruits.count("banana"))          # you could find amount of time that a value found a within a list 



# ------------------------------------------------------------
# --------------------- Set {} -------------------------

fruits = {"apple", "orange", "banana", "coconut"}

print(fruits)
print(dir(fruits))            # to get the all the attribute and methods

print(help(fruits) )          # if you want a description of each method


print(len(fruits))              # length of the set

print("pineapple" in fruits)    # check that element in the set

#  --- we can not use the indexing in set, because it is unordered

fruits.add("pineapple")
print(fruits)                   # we can add element

                                
fruits.remove("")       # we can remove element                                
print(fruits)


fruits.pop()            # pop method remove, what ever element in first, but it going to be random
print(fruits)


fruits.clear()          # clear the set
print(fruits)



# ------------------------------------------------------------
# --------------------- Tuple () -------------------------

fruits = ("apple", "orange", "banana", "coconut", "coconut")

print(fruits)
print(dir(fruits))            # to get the all the attribute and methods

print(help(fruits) )          # if you want a description of each method


print(len(fruits))              # length of the set

print("pineapple" in fruits)    # check that element in the set



# ------- only two method we can access to (diffrent from list and set)----------------------

print(fruits.index("apple"))
print(fruits.count("coconut"))


# with in a collection those elements are iterable 
for fruit in fruits:
    print(fruit)
