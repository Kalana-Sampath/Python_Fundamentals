# for loops = execute a block of code a fixed number of times.
#             You can iterate over a range, string, sequence, etc.

for x in range(1, 11):
    print(x)

for x in reversed(range(1, 11)):   # to count backwords, wnat to use revesed function
    print(x)

print("HAPPY NEW YEAR!")

for x in range(1, 11, 2):   # using steps, you can count by two
    print(x)

print("HAPPY NEW YEAR!")


#-----------------------------------------------------------------

credit_card = "1234-5678-9012-3456"

for x in credit_card:    # you can iterate a string using for loop as well 
    print(x)


#-------------------------------------------------------------
# continue and break

for x in range(1, 21):
    if x == 13:
        continue              # skip the number 13, to skip the over and iteration you can use the continue
    else:
    print(x)


for x in range(1, 21):
    if x == 13:
        break              # using the break keyword you can brek the loop entirely 
    else:
        print(x)



# There is a lot of overlaps where you could use either a while loop or for loop
# while loop is better if you nedd to execute something possibly infinite amount of times, 
# such as when you are accepting user input, 


