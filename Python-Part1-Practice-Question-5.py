# 5. Write a Python program to find common divisors between two numbers in a given pair.

a =int(input("Enter first number"))
b =int(input("Enter second number"))
if a > b:
    g = a
    l = b
    if a % b == 0:
        print(b,"is a common divisor")
    i = 1
    while (i <= int(b/2)):
        if ((g % i == 0) and (l % i == 0)):
            print(i,"is a common divisor")
        i = i + 1
else:
    g = b
    l = a
    if b % a == 0:
        print(a,"is a common divisor")
    i = 1
    while (i <= int(a/2)):
        if ((g % i == 0) and (l % i == 0)):
            print(i,"is a common divisor")
        i = i + 1