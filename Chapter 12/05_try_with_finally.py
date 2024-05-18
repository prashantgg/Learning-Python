try:
    i = int (input("Enter a number: "))
    c = 1/i
except Exception as e:
    print (f"Following error occured: {e}")
    exit()

finally:
    print ("We are done")

#print ("We are done") This is not used because when the except occurs this will not be printed as the program is exited
