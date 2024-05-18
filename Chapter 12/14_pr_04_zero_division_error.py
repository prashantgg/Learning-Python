try:
    a = int(input("Enter first no: "))
    b = int(input("Enter second no: "))
    c = a/b
    print (int(c)) 
except ZeroDivisionError:
    print ("Infinite")
