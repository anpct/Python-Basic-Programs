"""
Write a program that accepts the lengths of three sides of a triangle as inputs. The
program output should indicate whether or not the triangle is a right triangle (Recall
from the Pythagorean Theorem that in a right triangle, the square of one side equals
the sum of the squares of the other two sides)
"""


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
