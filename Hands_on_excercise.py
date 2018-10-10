"""Intro to python - part1 - Hands-on - Exercise"""

import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print("type=",type(pi),"value=",pi)


# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
if i<50:
    print ( "i is less than 50")
elif i>50:
    print('i is greater than 50')
else:
    print ("i is equal to 50")


# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
if picked_fruit=="orange":
    print("color is Orange")
elif picked_fruit=="strawberry":
    print("color is Pink")
else:
    print("Color is Yellow")

# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.

value1=int(input("Enter a Number:" ))
value2=int(input("Enter another Number:" ))

def multiply(value1,value2):
    result = value1*value2
    return result
result=multiply(value1,value2)
print("Multiply of value1 and value2 is=",result)

# TODO: Now call the function a few times to calculate the following answers

print("12 x 96 =",multiply(12,96))

print("48 x 17 =",multiply(48,17))

print("196523 x 87323 =",multiply(196523,87323))