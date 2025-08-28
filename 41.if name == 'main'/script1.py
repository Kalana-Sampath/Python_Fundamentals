#  if __name == "__main_": (this script can be imported OR run standalone)
#  Functions and classes in this module can be reused without the main block of code executing 
#  Good practice (code is modular,
#                 helps readability,
#                 leaves no global variables,
#                 avoid unintended execution)

def favorite_food(food):
    print(f"Your favorite food is {food}")

def main():
    print("This is script1")
    favorite_food("pizza")
    print("Goodbye!")

if __name__ == "__main__":
    main()
