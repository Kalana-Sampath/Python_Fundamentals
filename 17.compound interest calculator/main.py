# Python compound interest calculator 

principle = 0
rate = 0
time = 0 

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle can't be less than or equal to zero")

while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Interest rate can't be less than or equal to zero")


while time <= 0:
    time = float(input("Enter the time in years: "))
    if time <= 0:
        print("Time can't be less than or equal to zero")

print(principle)
print(rate)
print(time)


total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")



#-------------------------------------------------------
# same program like above, but we can enter the zero values


principle = 0
rate = 0
time = 0 

while True:                                                     # you can write true for the condition then it run                                                            #forever
    principle = float(input("Enter the principle amount: "))       # forever, you will need explicit out of the 
    if principle < 0:                                            # while loop
        print("Principle can't be less than or equal to zero")
    else: 
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate can't be less than or equal to zero")
    else:
        break


while True:
    time = float(input("Enter the time in years: "))
    if time < 0:
        print("Time can't be less than or equal to zero")
    else:
        break

print(principle)
print(rate)
print(time)


total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")

