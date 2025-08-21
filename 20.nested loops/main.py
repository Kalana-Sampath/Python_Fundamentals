# nested loop = A loop within another loop (outer, inner)
#               outer loop:
#                   inner loop:

for x in range(3):   # inner loop run 3 times
    for y in range(1, 10):      
        print(y, end="")       # all the character print in one line  
    print()                    # each outer loop print in separate line
    

#----------------------------------------------------------------
# ------------- create a rectangle according the symbol ---------

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()
 

