lst=[1,2,3,4,5,6]
#a=sorted(lst)
#if a == lst:
#    print("yes")
#else:
#    print("NO")


res="yes"
for i in range(1,len(lst)):
    if lst[i]<lst[i-1]:
        res="NO"
        break
print(res)
