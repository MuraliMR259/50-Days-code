s=input()
l=list(map(int,s))
res=0
for i in l:
    res+=i*i*i
    if(str(res==s)):
        print("Armstorng number")
    else:
        print("not armstorng number")
