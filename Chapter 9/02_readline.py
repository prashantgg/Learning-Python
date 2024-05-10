
f = open('sample.txt')  
#read first line
data = f.readline()
print (data, end="")

#read second line
data = f.readline()
print (data, end="")

#read third line
data = f.readline()
print (data, end="")

#read fourth line.... and so on......
data = f.readline()
print (data)

f.close() 