s="Hello Murali Welcome"
s.lower()
vowel=['a','e','i','o','u']
res=[]
for i in range(len(s)):
   if s[i] in vowel:
      res.append(i)
print(res)
