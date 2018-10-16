#Please write a program which count and print the numbers of each character in a string input by console.

s=['s','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
b=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
s1=str(input("Enter the string : "))
for i in s1:
    t=0
    for j in s:
        t=t+1
        if i==j:
            b[t-1]=b[t-1]+1
i=1
while( i<=26):
    if b[i]!=0:
        print(s[i]," : ",b[i])
        i=i+1;
    else:
        i=i+1

