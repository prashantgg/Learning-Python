a = int(input("Enter 1st no: "))
b = int(input("Enter 2nd no: "))
c = int(input("Enter 3rd no: "))

def greatest():
    if a > b and a>c:
        return a
    elif b>a and b >c:
        return b
    else:
        return c
    
print ("Greatest among three number is :", greatest())


    