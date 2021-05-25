l=[10,{"ok":1},{"ok":2},{"ok":3 ,"ok":4},20]
res=[]
#for i in l:
#   if isinstance(i,dict):
        res.append(i)
#print(len(res))
#print(res)
res=[i for i in l if isinstance(i,dict)]
print(len(res))
