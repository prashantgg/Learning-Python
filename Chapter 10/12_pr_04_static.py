class Calculation:
    def __init__(self,a,b):
        self.num1 = a
        self.num2 = b

    def addition(self):
        print(f"The addition of {self.num1} and {self.num2} is {self.num1 + self.num2}")
    def subtraction(self):
        print(f"The subtraction of {self.num1} and {self.num2} is {self.num1 - self.num2}")
    def multiplication(self):
        print(f"The multiplication of {self.num1} and {self.num2} is {self.num1 * self.num2}")
    def division(self):
        print(f"The addition of {self.num1} and {self.num2} is {self.num1 / self.num2}")
    
    @staticmethod
    def greet():
        print ("*****Hello User Welcome to the best calcualtor of the world****** ")
    
calc = Calculation(5,6)


calc.greet()
calc.addition()
calc.subtraction()
calc.multiplication()
calc.division()
