# Write a program to create, append, and remove lists in python


a=list()
def one():
    a.append(int(input("Enter the value to append:")))
def two():
    a.insert(int(input("Enter the index:")),int(input("Enter the value:")))
def three():
    a.pop()
def four():
    print(a)
def five():
    a.sort()
def six():
    a.clear()
def seven():
    a.remove(int(input("Enter the element to remove:")))
def eight():
    print(len(a))
def nine():
    exit()
while(True):
    print("1.Add at end")
    print("2.Add at specific index")
    print("3.Pop from the list")
    print("4.Print the list")
    print("5.Sort the list")
    print("6.Clear the list")
    print("7.Remove element from list")
    print("8.Print length of list")
    print("9.Exit")
    n = int(input("Enter your choice: "))
    s = {
        1: "one()",
        2: "two()",
        3: "three()",
        4: "four()",
        5: "five()",
        6: "six()",
        7: "seven()",
        8: "eight()",
        9: "exit()"
    }
    eval(s[n])