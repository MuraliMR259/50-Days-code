def fun(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        n1=0
        n2=1
        i=2
        while(i<n+1):
            temp=n2
            n2=n1+n2
            n1=temp
            i+=1
        return n2
n=int(input("enter the number"))
print(fun(n))