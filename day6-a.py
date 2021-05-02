import re
value=[]
s=input("Enter the value")
l=s.split(",")
for i in l:
    if len(i)<6 or len(i)>12:
        continue
    else:
        pass
    if not re.search("[a-z]]",i):
        continue
    elif not re.search("[0-9]]", i):
        continue
    elif not re.search("[A-Z]]", i):
        continue
    elif not re.search("[@#$]]", i):
        continue
    else:
        pass
    value.append(i)
print(",".join(value))
