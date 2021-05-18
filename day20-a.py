from random import randrange
a=list(map(int,input("enter the numbers :").split(",")))
for i in range(len(a)):
    j=randrange(i,len(a))
    a[i],a[j]=a[j],a[i]
print(a)