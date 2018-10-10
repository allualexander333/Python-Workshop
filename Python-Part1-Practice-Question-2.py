#2. Write a Python program that accept a positive number and subtract from this number the sum of its digits and so on. Continues this operation until the number is positive.

def positive(n):
    if(n>=0):
      print("The numbers are given below ")
      s = 0
      n_str = str(n)
      while (n > 0):
        n = n - sum([int(i) for i in list(n_str)])
        print (n)
        n_str = list(str(n))
        s = s + 1
      return s
    else:
        print("the entered number is not positive")
v1 = int(input("Enter a positive Number:" ))
count = positive(v1)
print("no of iteration used is ",count)