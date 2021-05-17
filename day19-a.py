arr=list(map(int,input("enter the arrya value : ").split(",")))
s=int(input("enter the sum number:"))
# for i in range(0,len(arr)):
#     for j in range(i+1,len(arr)):
#         if(arr[i]+arr[j]==s):
#             print("pair found at index ",i,"and ",j,"(",arr[i],"+",arr[j],")")
for i,v in enumerate(arr):
    if (s-v) in arr:
        print("pair found at index",i," and ",arr.index(s-v),"(",v,"+",s-v,")")