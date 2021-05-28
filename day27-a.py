from itertools import combination
arr=[3,4,1,9,56,7,9,12]
m=5
x=[]
l=combination(arr,5)
for i in l:
    i=sorted(i)
    x.append(i[-1]-i[0])
print(min(x))
