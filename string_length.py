
n1 =int(input("Enter the first number :"))
n2 =int(input("Enter the second number :"))

if n1 > n2:
    big = n1
    small = n2
    print("Common divisors are")
    if n1 % n2 == 0:
        print(n2)
    i = 1
    while (i <= int(n2/2)):
        if ((big % i == 0) and (small % i == 0)):
            print(i)
        i = i + 1
else:
    big = n2
    small = n1
    print("Common divisors are")
    if n2 % n1 == 0:
        print(n1)
    i = 1
    while (i <= int(n1/2)):
        if ((big % i == 0) and (small % i == 0)):
            print(i)
        i = i + 1