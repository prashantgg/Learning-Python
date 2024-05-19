def square (num):
    return num*num
l = [1,2,4]
# Method1
# l2 = []
# for item in l:
#     l2.append(square(item))
# print (l2)

#Map Method
a = list(map(square,l))
print (a)