# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program reusable separate files


print(help("modules"))      # bulit in modules
print(help("math"))         # use tha module name to get which there details


import math
import math as m        # aother way to use imporet is using alies, you will no longer need to module name 'math'
from math import pi     # aother way to use imporet is using function, you will no longer need to module name 'math'

print(math.pi)
print(m.pi)
print(pi)


# warnning - some times use the "from math import ....." method can be impact to the get the wrong output
#       - ------ example -------- -

from math import e

a, b, c, d, e = 1, 2, 3, 4, 5

print(e ** a)
print(e ** b)
print(e ** c)  
print(e ** d)
print(e ** e)        # this time all answer are get the 2 nd e as a 'e' value, then output wrong 

    # there fore use the "import math" method is more useful



# --------------------------------------------
# ----- create the own module ----------------
# import the own module

import example

result = example.pi
result1 = example.square(3)
result2 = example.cube(3)
result3 = example.circumference(3)
result4 = example.area(3)

print(result)
print(result1)
print(result2)
print(result3)
print(result4)

