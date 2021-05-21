a=list(map(int,input("Enter the list :").split(",")))
def cons(a):
    mx=max(a)
    mi=min(a)
    if mx-mi!=len(a)-1:
        return False
    visit=[]
    for i in a:
        if i in visit:
            return False
        visit.append(i)
    return True
if(cons(a)):
    print("consecutive list")
else:
    print(" not consecutive list")
