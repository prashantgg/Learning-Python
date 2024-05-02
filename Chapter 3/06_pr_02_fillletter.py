letter = '''Dear Name,
You are Selected
Date
'''
name = input("Enter your name: ")
date = input("Enter Date: ")
letter = letter.replace("Name", name)
letter = letter.replace ("Date", date)
print (letter)


