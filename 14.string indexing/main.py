# indexing = accessing elements of a squence using [] (indexing operator)
#            [start : end : step]

credit_number = "1234-5678-9012-3456"

print(credit_number[0])
print(credit_number[4])

# get the first four digit
print(credit_number[0:4])   # starting index is inclusive and ending index is exclusive therefore use the 4 as
                            # last digit 
print(credit_number[:4])    # also same above, python assume the start with 0 index

print(credit_number[5:])    # last 12 digit (if you need up to the end, not need to add ending index)

print(credit_number[-1])    # negative index is start from last element

# using steps can count by element, like count by 3s or count by 4s

print(credit_number[::2])  # count by every 2 nd character


#----------------------------------------------------------------------------------------------
# ---- Practical Example - create a program for get the last four digits from credit card number

last_digits = credit_number[-4:]
print(f"xxxx-xxxx-xxxx-{last_digits}")


credit_number = credit_number[::-1]     # backwords the string 
credit_number1 = credit_number[-1:-12:-1]   # backwords to specific point

print(credit_number)
print(credit_number1)



#-----------------------------------------------------------------

credit_number1 = credit_number[-1:-12:-1]  ✅
credit_number1 = credit_number[-1:-12]❌

Why it works:

Normally, with positive step (+1), slicing only works left → right (increasing indices).
But here you gave step = -1, so slicing goes right → left (decreasing indices).



