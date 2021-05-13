l=list(map(int,input("enter the list :").split(",")))
pos1=int(input("enter pos1 :"))
pos2=int(input("enter pos2 :"))
#l[pos1-1],l[pos2-1]=l[pos2-1],l[pos1-1]

temp=l[pos1-1]
l[pos1-1]=l[pos2-1]
l[pos2-1]=temp
print(l)
