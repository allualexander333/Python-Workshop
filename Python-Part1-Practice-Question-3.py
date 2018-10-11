# 3. Write a Python program to find the digits which are absent in a given mobile number


a1 = []
a = int(input("Enter a mobile number (only 10 digit): "))
c = 0
while (c <= 9):
    a1.append(a % 10) 
    a = int ( a / 10 )
    c = c + 1

n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in a1:
    for j in n:
        if i == j:
            k=int(i)
            b[k] = True
l = 0
for m in b:
    if m == False:
       print(n[l],"is not present in the number")
    l += 1
