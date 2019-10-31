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
