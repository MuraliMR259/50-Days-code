l=list(map(str,input("Enter the number :").split(",")))
temp=[]
for i in l:
    if(int(i,2)%5==0):
       temp.append(i)
print(",".join(temp))