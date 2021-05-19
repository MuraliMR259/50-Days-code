n = int(input("enter the integer :"))
s=input("enter the string :")
a='abcdefghijklmnopqrstuvwxyz'
b=reversed(a)
d=dict(zip(a,b))

before=s[:n-1]
after=s[n-1:]
mirror=''
for i in range(0,len(after)):
    mirror+=d[after[i]]
print(before+mirror)
print(d)
