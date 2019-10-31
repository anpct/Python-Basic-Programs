import math
def t(a,b,c):
    if(c==math.sqrt(((b**2)+(a**2)))):
        print("Its right angle triangle")
    else:
        print("Not right angle triangle")
a=int(input("Enter 1st side:"))
b=int(input("Enter 2nd side:"))
c=int(input("Enter 3rd side:"))
t(a,b,c)
