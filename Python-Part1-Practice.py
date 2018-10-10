# TODO: 1. Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other.

import math
import random

v1 = int(input("Enter first Number:" ))
v2 = int(input("Enter second Number:" ))
v3 = int(input("Enter third Number:" ))

def notequal(v1,v2,v3):
    if(v1==v2):
        result = "Values are Equal"
        return result
    elif(v2==v3):
        result = "Values are Equal"
        return result
    elif(v1==v3):
        result = "Values are Equal"
        return result
    else:
        result = "Values are not equal"
        return result
result=notequal(v1,v2,v3)
print("The provided ",result)


#2. Write a Python program that accept a positive number and subtract from this number the sum of its digits and so on. Continues this operation until the number is positive.

def repeat_times(n):
  s = 0
  n_str = str(n)
  while (n > 0):
    n -= sum([int(i) for i in list(n_str)])
    n_str = list(str(n))
    s += 1
  return s
print(repeat_times(9))
print(repeat_times(21))


