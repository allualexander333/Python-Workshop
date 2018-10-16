#Please write a program which accepts a string from console and print the characters that have even indexes.

s1=str(input("Enter a string : "))
s=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
t=[]
i=0
l=len(s1)
while(i<l):
    for j in s:
        if(s1[i]==j):
            t.append(s1[i])
    i=i+1
for k in t:
    print(k,end='')
