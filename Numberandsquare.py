#With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.

a=[]
s=[]
m=[]
n1=int(input("Enter a number:\t"))
i=1
n=n1
while(i<=n):
    l=i*i
    a.append(i)
    s.append(l)
    i=i+1
i=0
print("{",end=' ')
while(i<n):
    if(i!=(n-1)):
        print(" ",a[i],":",s[i]," ",end=',')
        i=i+1
    else:
        print(" ",a[i],":",s[i]," }",end=' ')
        i=i+1    

    