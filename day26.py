a=[8,8,8,2,2,4,3,3,6,5]
#list.sort(reverse=True)
s=set(a)
count=[]
d=[]
for i in s:
    d.append(a.count(i))
    count.append([a.count(i),i])

d=set(d)

res=[]
for i in d:
    temp=[]
    for j in count:
        if(j[0]==i):
            temp.append(j)
    temp=sorted(temp)
    res.extend(temp[::-1])

final=[]
for i in res:
    final.extend(i[0]*str(i[1]))

print(final[::-1])
