# Write a python program to find factorial of a number using Recursion


def fact(n):
    if(n==1):
        return 1
    else:
        return n*fact(n-1)
n  =  int(input("Enter the number:"))
print("Factorial is:",fact(n))