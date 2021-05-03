#differt to map and filter funnction
# l=[1,2,3,4,5]
# a=list(map(lambda x:x==2,l))
# print(a)
# b=list(filter(lambda x:x==2,l))
# print(b)
l=list(map(int,input("Enter the number :").split(",")))
a=list(map(lambda x:x**2,filter(lambda x:x%2==0,l)))
print(a)