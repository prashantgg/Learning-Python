def checking():
    with open ("poem.txt", "r") as f:
        return f.read()
   

check = checking()
print (check)

# finding = check.find ("Twinkle")
# print (finding)


if "Twinkle" in check:
    print ("The word is present")
else:
    print ("The word is not present")


