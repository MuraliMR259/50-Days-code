s="hi am sam my number is 4364324567"
s=list(s)
digit=0
letter=0
for i in range(len(s)):
    if s[i].isdigit():
        digit+=1
    elif s[i].isalpha():
        letter+=1
print("digit:",str(digit))
print("letter :",str(letter))