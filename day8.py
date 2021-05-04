a=0
b=5
try:
    print(a/b)
except TypeError:
    print("str include")
except ZeroDivisionError:
    print("zero is include")