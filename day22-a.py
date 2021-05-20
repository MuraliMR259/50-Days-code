n=list(map(int,input("enter the list :").split(",")))
def summaxnumber(a):
    maxnumber=0
    heremax=0
    for i in a:
        heremax+=i
        heremax=max(0,heremax)
        maxnumber=max(heremax,maxnumber)
    return maxnumber
print(summaxnumber(n))