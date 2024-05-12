class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit):
        self.name =name
        self.salary = salary
        self.subunit = subunit
        print ("Employee is created")
    
    def getDetails(self):
        print (f"The name of this employee is {self.name}")
        print (f"The salary of this employee is {self.salary}")
        print (f"The subunit of this employee is {self.subunit}")

    def getSalary(self,signature):
        print (f"Salary for this employee in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print ("Good Morning, Sir")
    
    @staticmethod
    def time():
        print ("The time is 9 am in the morning")

harry = Employee("Harry", 100, "Youtube")
# harry = Employee() --> This throws an error
harry.getDetails()