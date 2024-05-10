with open ("poem.txt") as f:
    content = f.read()

with open ("copy.txt") as f:
    content2 = f.read()


if content == content2:
    print ("The files are identical")
else:
    print ("The files are not identical")

