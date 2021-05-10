def fact(n):
    res=1
    for i in range(1,n+1):
        res*=i
    return res

        
num=input("enter the num :")
l=list(num)
total=0
for i in l:
    total+=fact(int(i))
print(total)
    
if(num==str(total)):
    print("number is storng")
else:
    
    print("number is not storng")
