# Match-case statement (switch): An alternative to using many "elif" statements
#                                Execute some code if a value matches a 'case'
#                                Benefits: cleaner and syntax is more readable


def day_of_week(day):
    match day:
        case 1:
            return "It is Sunday"
        case 2:
            return "It is Monday"
        case 3:
            return "It is Tuesday"
        case 4:
            return "It is Wednesday"
        case 5:
            return "It is Thursday"
        case 6:
            return "It is Friday"
        case 7:
            return "It is Saturday"
        case _:
            return "Not a valid day"        # case _  - mean wild card, mean no matching cases, or else statement

print(day_of_week(1))
print(day_of_week(2))
print(day_of_week(7))
print(day_of_week("pizza"))



#----------------------------------------------------------
# ----------------- pass a string -------------------------

def is_weekend(day):
    match day:
        case "Sunday":
            return True
        case "Monday":
            return False
        case "Tuesday":
            return False
        case "Wednesday":
            return False
        case "Thursday":
            return False
        case "Friday":
            return False
        case "Saturday":
            return True
        case _:
            return False 

print(is_weekend("Monday"))
print(is_weekend("Sunday"))



# there is a way we can modify match case too 
# -- use the or logical operator ( | )

def is_weekend(day):
    match day:
        case "Sunday" | "Saturday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return False 

print(is_weekend("Monday"))
print(is_weekend("Sunday"))
print(is_weekend("Pizza"))