def duplicate(n):

    new=[]
    for i in n:
        if i not in new:
            new.append(i)
    return new
a=[1,2,3,4,5,12,3,4,5,6]
print(duplicate(a))
