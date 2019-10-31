# Write a program to demonstrate working with dictionaries in python


a={
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd'
}
def two():
    print((input("Enter value to check:")) in a.items())
def four():
    a.clear()
while(True):
    print("1.Print dictionary")
    print("2.Check if value exists")
    print("3.Find size of dictionary")
    print("4.Clear dictionary")
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

