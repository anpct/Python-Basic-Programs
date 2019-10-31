def alt(inp, a, b):
    s = {
        '+': a+b,
        '-': a-b,
        '*': a*b,
        '/': a/b,
        '%': a%b,
        '^': a**b
    }
    return s.get(inp)


print(alt(input("Enter the operator:"), int(input("Enter number 1:")), int(input("Enter number 2:"))))