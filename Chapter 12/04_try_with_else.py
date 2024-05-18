try:
    i = int (input("Enter a number: "))
    c = 1/i
except Exception as e:
    print (f"Following error occured: {e}")

else:
    print ("We were successful")