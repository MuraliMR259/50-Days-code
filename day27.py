a=[1,19,-4,35,38,25,120]
mi=1000
for i in range(len(a)-1):
    if abs(a[i]-a[i+1])<mi:
        mi=abs(a[i]-a[i+1])
print(mi)

#for i in range(len(a)):
#    for j in range(i+1,len(a)):
#        if abs(a[i]-a[j])<mi:
#            mi=abs(a[i]-a[j])
#print(mi)
