# variable scope = where a variable is visible and accessible 
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

def func1():
    a = 1
    print(a)
    
def func2():
    b = 2
    print(b)

func1()
func2()

# in function1 has no idea with variable b, as well as the function 2 has no idea with variable a
# that is where viable scope comes in (where a variable is visible and accessible) 

# Function's can not see inside of other functions, but they can see inside of their own function. 


# -----------------------------------------------------
# we could create different version of the same variable.

def func1():
    x = 1
    print(x)
    
def func2():
    x = 2
    print(x)

func1()
func2()

# we have two different version of x. A local version of x found within function one and local version of function
# two found within function two. 

# Whenever we utilize a variable, we will first look to see if there's any local instance of that variable. If there
# is not, we would move to enclosed scope, 

# one example - we have a function declared within another function. 

def func1():
    x = 1

    def func2():
        print(x)        
    func2()             # if the invoke the func2 then, fisrt look the local variable, if the local x not defined(found),
                        # then use the enclosed variabe 
                        # it use the order -> (LEGB) Local -> Enclosed -> Global -> Built-in
     
func1()                



#  -------------- move to the global scope -----------------------
# global meanning outside of any function ------------------------

def func1():
    print(x)

def func2():
    print(x)        

x = 3               # if there is no local version as well as no enclosed version, we would move on to the 
                    # global version
             
func1() 
func2()



#  -------------- move to the built-in scope -----------------------
# built-in meanning inbuild function -------------------------------

from math import e

def func1():
    print(e)

func1()

