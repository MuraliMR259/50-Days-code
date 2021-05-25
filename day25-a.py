def rod(price,n):
    if n==0:
        return 0
    maxvalue=-1
    for i in range(1,n+1):
        cost=price[i-1]+rod(price,n-i)
        if maxvalue<cost:
            maxvalue=cost
    return maxvalue
price=[1,5,8,9,10,17,17,20]
n=5
print("profis is :"+str(rod(price,n)))
