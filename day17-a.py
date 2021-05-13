n=input("enter the number :")
odd=0
even=0
for i in range(len(n)):
    if(i%2==0):
        even+=int(n[i])
    else:
        odd+=int(n[i])
if((odd-even)==0):
    print("yes")
else:
    print("no")
