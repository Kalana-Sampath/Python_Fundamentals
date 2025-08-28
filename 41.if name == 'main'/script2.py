
from script1 import *

def favorite_drink(drink):
    print(f"Your favorite drink is {drink}")

def main():
    print("This is script2")
    favorite_food("sushi")
    favorite_drink("coffee")
    print("Goodbye!")

# sometimes from another Python script, you want to borrow something, but you don't want to run the main body of 
# code directly 
# script 2 can be run as a standalone program, but i can not import it without this body of code running.

if __name__ == "__main__":
    main()
