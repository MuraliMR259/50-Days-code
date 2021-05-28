arr=['4457467382','3375648392','2275675678','1187686759','1']
arr.sort(key=lambda x:(len(x),x))
print(" ".join(arr))
