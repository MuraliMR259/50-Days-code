s="Murali dharan"
s=list(s.split(" "))
d=dict()
for i in s:
    first=i[0]
    last=i[-1]
    key=first+last
    if key in d:
        d[key].append(i[1:-1])
    else:
        d[key]=i[1:-1]
print(d)
