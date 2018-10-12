# 4. Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.

import itertools  
var1 = ['a','e','i','o','u']
var2 = var1

for i in var1:
    for j=i+1 in var2:
        print(i)