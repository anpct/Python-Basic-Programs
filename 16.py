# Write a script named copyfile.py. This script should prompt the user for the names of
# two text files. The contents of the first file should be input and written to the second
# file


fname1 = input("Enter the first file name: ")
fname2 = input("Enter the first file name: ")
f1=open("d:\{}.txt".format(fname1), 'r')
f2=open("d:\{}.txt".format(fname2), 'w')
f2.write(f1.read())
f1.close()
f2.close()