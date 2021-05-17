n=int(input("enter the number :"))
b=bin(n)
b=b[2:]
if(b==b[::-1]):
    print("True")
else:
    print("False")