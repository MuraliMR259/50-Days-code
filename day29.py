arr=[2,7,5,3,0,8,1]
count=[]
for i in range(len(arr)):
    temp=0
    for j in range(i+1,len(arr)):
        if(arr[i]<arr[j]):
            temp+=1
    count.append(temp)
print(count)
