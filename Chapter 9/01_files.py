#Use open function to read the content of the file

# f = open('sample.txt', 'r')
# f = open('sample.txt', 'r')
f = open('sample.txt', 'r')  #by default the mode is r
data = f.read() # reads first 8 characted from the text
print (data)
f.close() 