class rev:
    def calc(self,s):
        str=""
        a=list()
        a.append(s.split())
        for i in range(len(a[0])-1, -1, -1):
            str=str+a[0][i]
            str=str+" "
        print(str)
if __name__=="__main__":
    ob=rev()
    ob.calc(input("Enter here:"))
