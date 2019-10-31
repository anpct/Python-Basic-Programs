a=tuple((0,1,2,3,4,5,6,7,8,9))
def two():
    print(int(input("Enter value to check:")) in a)
def four():
    print(a.index(int(input("Enter the value:"))))
while(True):
    print("1.Print tuple")
    print("2.Check if value exists")
    print("3.Find size of tuple")
    print("4.Retrieve index")
    print("5.Exit")
    n = int(input("Enter your choice: "))
    s = {
        1: "print(a)",
        2: "two()",
        3: "print(len(a))",
        4: "four()",
        5: "exit()"
    }
    eval(s[n])

