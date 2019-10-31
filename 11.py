for i in range(1,20):
    flag=1
    for j in range(2,int(i/2)):
        if(i%j==0):
            flag=0
    if(flag==1):
        print(i)

