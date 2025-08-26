# Iterables = An object/collection that can return its elements one at a time,
#             allowing it to be iterated over in a loop 

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)

#each element that we are given from our iterable, the name should be descriptive of what we are given


#------- you could iterate backwords by enclosing our iterable within the reverese function.

numbers = [1, 2, 3, 4, 5]

for number in reversed(numbers):
    print(number)


#--------------------------------
# tuples and sets also iterable

#--------------------------------
# ------- iterable to string 

name = "Kalana Sampath"

for character in name:
    print(character, end=" ")
    
    
#--------------------------------
# ------- iterable to dictionaries  

my_dictionary = {"A": 1, "B": 2, "C": 3}

for key in my_dictionary:     # in default dictionary return the all the keys, not the values
    print(key)


for value in my_dictionary.values():        # this will return the all the values
    print(value)

for key, value in my_dictionary.items():      # this will return the both keys and values
    print(key, value)




