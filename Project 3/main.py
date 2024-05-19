class Library:
    books = ["Python", "CSS", "HTML", "JavaScripts", "Java", "Flutter", "Dart"]
    def ListOfBooks(self):
        bk_list = " \n * ".join(self.books)
        print (f"The books available in the Library are: \n *  {bk_list}")
    
    def BorrowBook(self, bookName):
        if bookName in self.books:
            print ("The book have been borrowed. Please return it in time.")
            self.books.remove(bookName)
        else:
            print ("Sorry The book is not available")

    def ReturnBook(self, bookName):
            self.books.append(bookName)
            print ("The book has been returned. ")

    def FineForBookCheck(self, days):
        if days > 30:
            print ("You Have Got Penalty Of Rs 100")
        else:
            print ("You don't have to pay any fine")


class Student:
    def BorrowBook(self):
        return input("Enter the name of book you want to borrow: ")
    def ReturnBook(self):
        return input("Enter the name of book you want to return: ")
    def FineForBookCheck(self):
        return int(input("Enter the amount of days you've using this book: "))

    


lib = Library()
stu = Student()
while (True):
    displaymsg = ('''\n Welcome To Prashant's Library 
                  1) List All the books avaibale in Library
                  2) Borrow a book from Library
                  3) Return a book in Library
                  4) Check Fine Money
                  5) Exit from Library''')
    print (displaymsg)
    a = int(input("Choose What You Want To Do In My Library: "))
    if (a == 1):
        lib.ListOfBooks()
    elif (a == 2):
        lib.BorrowBook(stu.BorrowBook())
    elif (a==3):
        lib.ReturnBook(stu.ReturnBook())
    elif (a==5):
        print ("Thanks For Using my Library ")
        exit()
    elif (a==4):
        lib.FineForBookCheck(stu.FineForBookCheck())

    else:
        print ("Invalid Number Entered")

