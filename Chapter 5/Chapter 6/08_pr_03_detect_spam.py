content = input ("Enter content:  ")
spam1 = ("make a lot of money")
spam2 = ("Click this")
spam3 = ("Subscribe this")
spam4 = ("buy now")
if (spam1 in content):
    print ("Spam word detected")
elif (spam2 in content):
    print ("Spam word detected")
elif (spam3 in content):
    print ("Spam word detected")
elif (spam4 in content):
    print ("Spam word detected")
else:
    print ("Spam word is not detected")

