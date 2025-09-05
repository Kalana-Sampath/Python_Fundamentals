# multithreading = Used to perform multiple tasks concurrently (multitasking)
#                  Good for I/O bound tasks like reading files or fetching data from APIs
#                  threading.Thread(target=my_function)


# without threading 

def walk_dog():
    time.sleep(8)
    print("You finish walking dog")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

def get_mail():
    time.sleep(4)
    print("You get the mail")


walk_dog()
take_out_time()
get_mail()        # these functions are running on the same thread, the main python program



# ------------------------------------------------------------------------------------------
# we have to complete the chores in order one by one because all running on the same thread
# we could accomplish all these tasks at the same time 
import threading
import time

def walk_dog():
    time.sleep(8)
    print("You finish walking dog")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

def get_mail():
    time.sleep(4)
    print("You get the mail")


chore1 = threading.Thread(target=walk_dog)
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()                            # we are executing these functions concurrently. We are multitasking



# ------------------------------------------------------------------------------------------
# With the join method, we will wait for these threads to finish before continuing with the rest of the program

import threading
import time

def walk_dog():
    time.sleep(8)
    print("You finish walking dog")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

def get_mail():
    time.sleep(4)
    print("You get the mail")


chore1 = threading.Thread(target=walk_dog)
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()  

chore1.join()
chore2.join()
chore3.join()

print("All chores are complete!")



# ------------------------------------------------------------------------------------------
# constructing a thread obejct and we have a keyword argument of target if some of these functions take 
# parameters, when we ara creating a thread and the target is that function and that function accepts 
# arguments, we need one more keyword argument and that is args. We will send this function a tupple.
# We need a set of paranthesis within this tuple. we will list our arguments.
import threading
import time

def walk_dog(first):
    time.sleep(8)
    print(f"You finish walking {first}")
    
def walk_dog(first, last):
    time.sleep(8)
    print(f"You finish walking {first} {last}")     # pass more arguments

def take_out_trash():s
    time.sleep(2)
    print("You take out the trash")

def get_mail():
    time.sleep(4)
    print("You get the mail")


# chore1 = threading.Thread(target=walk_dog, args=("Scooby",))
# chore1.start()
chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo"))     # pass the multiple parameters
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()  

chore1.join()
chore2.join()
chore3.join()

print("All chores are complete!")
