class Employee:
    company = "Visa"
    eCOde = 120

class Freelancer:
    company = "Fiber"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1

class Programmmer(Employee,Freelancer):
    name = "Prashant"

p = Programmmer()
print (p.company) # It'll print visa becayse the Employee class is being called at first in Programmer Class
p.upgradeLevel()
print (p.level)
