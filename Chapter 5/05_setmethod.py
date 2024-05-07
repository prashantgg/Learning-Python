# Creating an empty set
b = set()
b.add(1)
b.add(5)
b.add (8)
b.add (9)
b.add (10)
b.add (15)

print (type(b))
print (b) 

# b.add ([1,2,3]) shows error
# print (b)

b.add ((4,5,5)) #it can be added as tuple cannot be changed
print(b)

# b.add ({"harry" : "Coder"}) #Shows error as list or dictinary can be changed
# print (b)

print (len(b)) #Prints the length of the sets

#Removal of an Item
b.remove((4,5,5))
print (b)


#Remove the random element from the set and display it
b.pop()
print (b)


#Empties the set
# b.clear()
# print (b)


print(b.union({3,4})) #print the final element taking all values 
print (b.intersection ({6,8,9})) #print the common values in both set

print (b)
