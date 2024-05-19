class format:
    def __init__(self, name, marks, phone):
        self.name = name
        self.marks = marks
        self.phone = phone
    
    def format1(self):
        return ("The name of the student is {0}, his marks are {1} and phone number is {2}".format((self.name), (self.marks), (self.phone)))

name = input("Enter the name of the user: ")
marks = int(input("Enter the marks of the user: "))
phone = int(input("Enter the phone of the user: "))
obj = format(name, marks, phone)
a = obj.format1()
print(a)

