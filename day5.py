bal=0
while True:
    s=input("enter amount:")
    if s==" ":
        break
    ttype,amount=s.split(" ")
    if (ttype=="D"):
        bal+=int(amount)
    else:
        bal-=int(amount)
print(bal)
