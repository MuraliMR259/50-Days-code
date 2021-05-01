s=(input("Enter the Value:"))
list=[i for i in s.split(",") if int(i)%2!=0]
print(list)
print(",".join(list))