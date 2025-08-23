# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA":"Washigtion D.C",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

print(dir(capitals))
print(help(capitals))
 
print(capitals.get("USA"))      # to get the value from dictionary (associate value)


# we can also use if statement

if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital doesn't exist")


capitals.update({"Germany": "Berlin"}) # to update the dictionary, we can update new key value pair or 
                                         # we can update existing key, value pairs
capitals.update({"USA": "Detroit"})
capitals.pop("China")                    # to remove the key value pairs
capitals.popitem()                       # to remove the latest key value pairs 
capitals.clear()                         # to remove the dictionary

print(capitals)

keys = capitals.keys()                   # to get the all of the keys in dictionaries, not the values

print(keys)

# iterate all the keys
for key in capitals.keys():
    print(key)

# ---- there is also the values method -----------

values = capitals.values()                 # to get the all of the values from the dictionary 
print(values)                              # return a obeject as a reesemble to list

# iterate all the values
for value in capitals.values():
    print(value)

items = capitals.items()                # to get the all the items
print(items)                            # items retrun a dictionary object which return a 2D list of tuples

# iterate all the items
for key, value in capital.items():
    print(f"{key}: {value}")

