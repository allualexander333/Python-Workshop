# TODO: 1. Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other.


v1 = int(input("Enter first Number:" ))
v2 = int(input("Enter second Number:" ))
v3 = int(input("Enter third Number:" ))

def notequal(v1,v2,v3):
    if(v1==v2):
        result = "Values are Equal"
        return result
    elif(v2==v3):
        result = "Values are Equal"
        return result
    elif(v1==v3):
        result = "Values are Equal"
        return result
    else:
        result = "Values are not equal"
        return result
result=notequal(v1,v2,v3)
print("The provided ",result)






