myDict = {
    "Fast" : "In a Quick Manner",
    "Harry" : "Youtuber",
    "Marks" : [1,2,3],
    "AnotherDict" : {"Harry" : "Coder"}
}

print (myDict)
print (myDict["Fast"])
print (myDict["Harry"])
print (myDict["Marks"])
print (myDict["AnotherDict"]["Harry"])

#Mutable
myDict["Marks"] = [5,6,10]
print (myDict["Marks"])

