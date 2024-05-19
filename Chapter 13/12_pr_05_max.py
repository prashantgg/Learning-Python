from functools import reduce
num = lambda a,b: a if a>b else b
l1 = [2,4,5,6]
check = reduce (num, l1)
print (check)