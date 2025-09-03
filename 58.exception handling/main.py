# exception = An event that interrupts the flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#             1.try,  2.except,  3.finally


try: 
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can not divide by zero IDIOT!")
except ValueError:
    print("Enter only numbers please!")


# -------- some peple catch all exception ------------------

try: 
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can not divide by zero IDIOT!")
except ValueError:
    print("Enter only numbers please!")
except Exception:
    print("Something went wrong!")
finally:                                   # finally code always execute regradless if there's an exception or not
    print("Do some clenup here")                 
  