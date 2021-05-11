s=input("enter the string :")
s=s.upper()
count=0
vowel=['A','E','I','O','U']
for i in s:
    if i in vowel:
         count+=1
print(count)
