import math
list=[0,0]
while True:
    s=input("Enter the value :")
    if s==" ":
        break
    mov,val = s.split(" ")
    if mov=="UP":
        list[0]+= int(val)
    elif mov=="DOWN":
        list[0]-= int(val)
    elif mov=="LEFT":
        list[1]-= int(val)
    elif mov=="RIGHT":
        list[1]+= int(val)
    else:
        pass
print(round(math.sqrt(list[1]**2)+(list[0]**2)))