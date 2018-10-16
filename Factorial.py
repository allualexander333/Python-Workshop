#Write a program which can compute the factorial of a given numbers.

f1= int(input("Enter a number:"))
i=1
n=f1
a=1
while(i<=n):
    a=a*i
    i=i+1
print("factorial is:",a)