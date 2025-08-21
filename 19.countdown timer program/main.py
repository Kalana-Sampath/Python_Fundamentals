import time 

time.sleep(3)

print("TIME'S UP!")

#----------------------------------------------------

my_time = int(input("Enter the time in seconds: "))

for x in range(0, my_time):
    time.sleep(1)               # after each iteration we will sleep one second 

print("TIME'S UP!")


#---------------------------------------------------
my_time = int(input("Enter the time in seconds: "))

for x in range(0, my_time):
    print(x)                    # x is our counter
    time.sleep(1)               # after each iteration we will sleep one second 

print("TIME'S UP!")


# ------ count the backwords ----------------------

my_time = int(input("Enter the time in seconds: "))

for x in reversed(range(0, my_time)):
    print(x)                    # x is our counter
    time.sleep(1)               # after each iteration we will sleep one second 

print("TIME'S UP!")


# ---------- another technique is used to steps -------------------------


my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):                     # start with my_time as well
    print(x)                                        # x is our counter
    time.sleep(1)                                   # after each iteration we will sleep one second 

print("TIME'S UP!")


#-------------------------- digital clock (counter) -------------------------------

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):                     # start with my_time as well
    seconds = x % 60                  # With our digital clock, we can't go above 60 for either seconds or minutes
    minutes = int(x / 60) % 60
    hours = int(x / 3600)               # want a date then add % 24 as well
    print(f"{hours:02}:{minutes:02}:{seconds:02}")      # zero format with 2 digits                    
    time.sleep(1)                                       # after each iteration we will sleep one second 

print("TIME'S UP!")

