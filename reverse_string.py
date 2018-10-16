#Please write a program which accepts a string from console and print it in reverse order.

s1=str(input("Enter a string : "))
a=len(s1)
while(a>0):
    print(s1[a-1],end='')
    a=a-1