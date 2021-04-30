l=[]
for i in range(1000,3001):
    temp=str(i)
    if(int(temp[0]) % 2==0 and int(temp[1])% 2==0 and int(temp[2]) % 2==0 and int(temp[3])% 2==0):
        l.append(temp)
print(",".join(l))
