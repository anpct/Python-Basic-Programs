# Write a program that inputs a text file. The program should print all of the unique
# words in the file in alphabetical order


a=list()
b=list()
fname=input("Enter file name: ")
f=open("d:\{}.txt".format(fname), "r")
for i in f.read().split():
    a.append(i);
a.sort()
for j in a:
    if j not in b:
        b.append(j)
print(a)
print(len(a))
print(b)
print(len(b))
