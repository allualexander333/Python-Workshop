#Please write a program to shuffle and print the list

from random import shuffle

n1=int(input("how many digit you want to shuffle:"))
s=[]
m=[]
for i in range(0,n1):
    s1 = int(input("enter digit:"))
    s.append(s1)

total=int(input("how much combination:"))

for j in range(0,total):
    l=shuffle(s)
    print(s)

