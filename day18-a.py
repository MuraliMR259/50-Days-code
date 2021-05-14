a,b=map(int,input("enter the number").split(","))
while(b):
    #temp=a
    #a=b
    #b=temp%b
    a,b=b,a%b
print(a)
