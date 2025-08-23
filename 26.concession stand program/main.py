# Concession stand program

# A concession stand, or refreshment stand (American English, Canadian English), snack kiosk or snack bar 
# (British English, Irish English) is a place where patrons can purchase snacks or food at a cinema, 
# amusement park, zoo, aquarium, circus, fair, stadium, beach, swimming pool, concert, sporting event, 
# or other entertainment venue. 

menu = {
    "popcorn": 3.50,
    "nachos": 4.00,
    "hot dog": 2.75,
    "pretzel": 3.00,
    "candy": 1.50,
    "soda": 2.00,
    "water": 1.25,
    "ice cream": 2.50
}

cart = []
total = 0

print("----------MENU-------------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("---------------------------")


while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)


print("-------- YOUR ORDER ---------")
for food in cart: 
    total += menu.get(food)
    print(food, end=" / ")

print()
print(f"Total is: ${total:.2f}")


    