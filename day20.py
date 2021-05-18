a=list(map(int,input("enter the numbers :").split(",")))
k=0
for i in a:
     if i:
         a[k]=i
         k+=1
for i in range(k,len(a)):
    a[i]=0
print(a)