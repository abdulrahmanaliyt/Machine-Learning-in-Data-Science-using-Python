from mypack import arith as ar

# Using the alias 'ar'
ar.add(6, 4)
a = ar.sub(6, 4)
print('The subtraction of two no is :', a)

i = 0
while i != 18:
    print("-", end=" ")
    i = i + 1
print("")

# Importing everything directly from mypack.arith
from mypack.arith import *

add(10, 5)
result = sub(10, 5)
print("The subtraction of two no is :", result)
