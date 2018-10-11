# 3. Write a Python program to find the digits which are absent in a given mobile number


mobile = []
a = int(input("Enter a mobile number (only 10 digit): "))
count = 0
while (count <= 9):
    mobile.append(a % 10) 
    a = int ( a / 10 )
    count = count + 1

temp1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
empty = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in mobile:
    for j in temp1:
        if i == j:
            k=int(i)
            empty[k] = True
l = 0
print("Below are the number which are not there in your mobile number")
for m in empty:
    if m == 0:
       print(temp1[l],"\t")
    l += 1
