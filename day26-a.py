a=[8,4,2,1]
count=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if(a[i]>a[j]):
            #count.append([a[i],a[j]])
            count+=1
print(count)
