#encoding and decoding

choice=int(input(" 1.Ascii value of a character.\n 2.String encoding.\n 3.String decoding\n Enter the choice : "))
if(choice==1):
    m=str(input("Enter a character : "))
    print(ord(m))

elif(choice==2):
    s1=str(input("Enter a string : "))
    c=int(input("Conversion code : "))
    s=[]
    l=len(s1)
    i=0
    while(i<l):
        s.append(int(ord(s1[i])-c))
        i=i+1
    for j in s:
        print(chr(j),end='')
elif(choice==3):
    s1=str(input("Enter the encoded string : "))
    c=int(input("Enter the decoding code : "))
    s=[]
    l=len(s1)
    i=0
    while(i<l):
        s.append(int(ord(s1[i])+c))
        i=i+1
    for j in s:
        print(chr(j),end='')
else:
    print("Wrong choice")
