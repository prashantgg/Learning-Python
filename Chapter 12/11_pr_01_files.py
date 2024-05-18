
def readFile(filename):
    try:
         with open (filename, "r") as a:
            a = a.read ()
            print (a)
    except Exception as e:
        print (f"Sorry the following error occured as there is no {filename}: {e}")
        

readFile("1.txt")
readFile("2.txt")
readFile("3.txt")


