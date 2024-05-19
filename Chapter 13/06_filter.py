def greater_than_5(num):
    if num>5:
        return True
    else:
        return False

lam = lambda num: num>65
l = [1,2,3,4,5,65,85,65,5,56,55,85]
a = list(filter(greater_than_5,l))
b = list(filter(lam,l))
print(a)
print(b)

