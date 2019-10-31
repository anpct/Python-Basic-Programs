# Write a program to create, concatenate and print a string and accessing sub-string
# from a given string


def op(s,k):
    o={
        1: "len(s)",
        2: "s",
        3: "s[::-1]",
        5: "s.upper()",
        6: "s.lower()",
        8: "exit()"
    }
    return o.get(k)


s = input("Enter the string:")
while(True):
    print("1.Print length")
    print("2.Print string")
    print("3.Print reverse")
    print("4.Print substring")
    print("5.Print uppercase")
    print("6.Print lowercase")
    print("7.Concatinate")
    print("8.exit")
    k = int(input("Enter the option:"))
    if(k==4):
        i = int(input("Enter the start index:"))
        j = int(input("Enter the end index:"))
        ans = s[i:j:]
        print(ans)
    elif(k==7):
        sd=input("Enter string to concatenate:")
        s=s+sd
    else:
        print(eval(op(s, k)))

