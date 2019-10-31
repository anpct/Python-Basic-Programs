# Write a Python class to implement pow(x, n)


class p:
    def calc(self,x,n):
        return (x**n)

if __name__=="__main__":
    pob=p()
    print(pob.calc(int(input("Enter x:")),int(input("Enter n:"))))