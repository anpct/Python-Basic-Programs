n=int(input("Enter the max value:"))
for i in range(0, n+1):
    for j in range(0, i):
        print("*", end="")
    print("\n")
for k in range(n-1, 0, -1):
    for l in range(0, k):
        print("*", end="")
    print("\n")