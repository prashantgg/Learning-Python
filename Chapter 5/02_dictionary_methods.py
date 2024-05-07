myDict = {
    "fast" : "In a Quick Manner",
    "harry" : "Youtuber",
    "marks" : [1,2,3],
    "anotherdict" : {"Harry" : "Coder"},
    1 : 2
}

print (myDict.keys()) #Prints the keys of the dictionary
print (myDict.values()) #Prints the values of the dictionary
print (type(myDict))
print (myDict.items()) #Prints the key and values of dictionart in tuple form
print (myDict)
myDict.update({"Me":"Coder",
               "You": "No One",
               1 : 4})  #Used for adding value in dictionary
print (myDict)

print (myDict.get("harry")) 

''' Alternately print (mydict["Harry"]) 
could have be used but it will throw
an error if the key is not present and 
if .get method is used it will written none.'''

