list1 = [1,2,3,10,25,85,8,55,65,245,222,4,23]


# list2 = []
# for item in list1:
#     if item%2 == 0:
#         list2.append(item)
# print (list2)


#shortcut to write the same
list2 = [item for item in list1 if item%2 == 0]
print (list2)


#Set Comprehension
t = {1,4,1,4,67}
s = {i for i in t if i>3}
print (s)