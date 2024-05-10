read = True
i = 1
with open ("log.txt") as f:

    while read:
       
        read = f.readline()

        if "python" in read.lower():
            print (read)
            print (f"The word python is present on line number {i}")
        i = i+1
   