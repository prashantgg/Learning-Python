def conversion (value):
    con = value * 2.54
    return con

v = int(input("Enter the value: "))
print ("The value of the given incehs in cm is: ", conversion(v))