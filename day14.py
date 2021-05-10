#a=[1,2,3,4]
#print(a[::-1])

s=123
num=s
reverse=0
while num>0:
    re=num%10
    reverse=(reverse*10)+re
    num=num//10
print(reverse)
