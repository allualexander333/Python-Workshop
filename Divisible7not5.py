#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5

a = []
n1=int(input("How many number you want to check?"))
i=0
while(i<n1):
    s1=int(input("Enter the number :"))
    if(s1%7 == 0 and s1%5!=0):
        a.append(s1)
    i=i+1
print("Numbers which are divisible by 7 but are not a multiple of 5 are given below")

print(a)
