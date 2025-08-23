# generate a random number

import random 

# print(help(random))                  # to see the all the methods

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

number = random.randint(1, 6)             # random hole integers , with range 1 to 6
number = random.randint(low, high)       # use the variable as a range
number  = random.random()                 # to get the floating point number you want to use, random 
random.choice(options)                    # place the sequence within the choice method

print(number)

#-------------------------------------------
option = random.choice(options)             # using the chose methods we can chose the option

print(option)

#-------------------------------------------
random.shuffle(cards)                       # using the shuffle method we can shuffle the sequence

print(cards)



