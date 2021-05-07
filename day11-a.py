s1=input("enter the character :")
s2=input("enter the another character :")
a=set(s1)
b=set(s2)
count=0
for i in a:
    if i in b:
        count+=1
print(count)