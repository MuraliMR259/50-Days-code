l=[3,1,2,4,5,9,13,14,12]
odd=[]
even=[]
for i in range(len(l)):
    if i%2==0:
        even.append(l[i])
        even.sort()
    else:
        odd.append(l[i])
        odd.sort(reverse=True)

print(odd)
print(even)
print(even+odd)
