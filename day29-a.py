a=[3,6,5,10,7,20]
for i in range(0,len(a),2):
    #temp=a[i]
    #a[i]=a[i+1]
    #a[i+1]=temp
    a[i],a[i+1]=a[i+1],a[i]
    
print(a)
