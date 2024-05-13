class Person:
    name = "Prashant"
    country = "Nepal"

    def takeBreath(self):
        print ("I am breathing")

class Employee(Person):
    company = "Google"

    def getSalary (self):
        print (f"Salary is {self.salary}")

    def takeBreath(self):
        print ("I am a employee so i am breathing.")

class Programmer (Employee):
    company = "Fiver"

    def getSalary (self):
        print (f"No Salary to programmer")

    def takeBreath(self):
        print ("I am a programmer so i am breathing++.")
p = Person()
# print (p.company()) # throws an error
p.takeBreath()
e = Employee()
e.takeBreath()
print (e.company)
pr = Programmer()
pr.takeBreath()
print (pr.company)
print (pr.country)

    
