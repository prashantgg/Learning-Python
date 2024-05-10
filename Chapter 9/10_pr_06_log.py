with open ("log.txt") as f:
    read = f.read()

if "python" in read.lower():
    print ("The word python is present")
else:
    print ("The word python is not present")