a=list(map(int,input("Enter the list 1 :").split(",")))
b=list(map(int,input("Enter the list 2:").split(",")))
temp=a+b
temp=sorted(temp)
x=(temp[:5])
y=(temp[5:])
print(x)
print(y)
