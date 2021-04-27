
# divisible 7 but not multiple 5 between 2000 to 3200 and ans is separate comma in single line
list=[]
for i in range(2000,3201):
    if(i % 7 ==0 and not i % 5 ==0):
        list.append(str(i))
print(",".join(list))
print(len(list))