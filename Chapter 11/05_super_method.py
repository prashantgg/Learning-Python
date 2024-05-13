class Person:

    def __init__(self):
        print ("Initializing Personn...\n")

    def takeBreath(self):
        print ("I am breathing")

class Employee(Person):

    def takeBreath(self):
        super().takeBreath()
        print ("I am a employee so i am breathing.")

    def __init__(self):
        super().__init__()
        print ("Initializing Employee...\n")

class Programmer (Employee):

    def __init__(self):
        super().__init__()
        print ("Initializing Programmer...\n")

    def takeBreath(self):
        super().takeBreath()
        print ("I am a programmer so i am breathing++.")
    
   
# p = Person()
# p.takeBreath()

# e = Employee()
# e.takeBreath()

pr = Programmer()
# pr.takeBreath()


    
