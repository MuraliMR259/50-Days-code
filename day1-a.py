# using for loop
n=int(input("Enter the valueL:"))
result =1
for i in range(1,n+1):
    result = result*i
print(result)

#using function

def fact(num):
    if num == 0:
        return 1
    return num*fact(num-1)
print(fact(5))