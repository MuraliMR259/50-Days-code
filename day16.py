def makeangram(s1,s2):
    res=0
    j=s1+s2
    un=set(j)
    for i in un:
        if(s1.count(i)==s2.count(i)):
            continue
        elif(s1.count(i)>s2.count(i)):
            res+=s1.count(i)-s2.count(i)
        elif(s1.count(i)<s2.count(i)):
            res+=s2.count(i)>s1.count(i)
    return res
s1=input("enter the s1")
s2=input("enter the s2")
print(makeangram(s1,s2))
