class Calculator:
    

    def __init__(self, num):
        self.a = num
    
    def square(self):
        return( self.a*self.a)
    def cube(self):
        return (self.a*self.a*self.a)
    def square_root(self):
        return ( self.a ** 0.5)
    
    def print(self):
        print (f"The square of no {self.a} is {self.square()}")
        print (f"The cube of no {self.a} is {self.cube()}")
        print (f"The square root of no {self.a} is {self.square_root()}")

a = int(input("Enter a number: "))
num = Calculator(a)
num.print()


# class Calculation:
#     def __init__(self,a,b):
#         self.num1 = a
#         self.num2 = b

#     def addition(self):
#         print(f"The addition of {self.num1} and {self.num2} is {self.num1 + self.num2}")
#     def subtraction(self):
#         print(f"The subtraction of {self.num1} and {self.num2} is {self.num1 - self.num2}")
#     def multiplication(self):
#         print(f"The multiplication of {self.num1} and {self.num2} is {self.num1 * self.num2}")
#     def division(self):
#         print(f"The addition of {self.num1} and {self.num2} is {self.num1 / self.num2}")
    
# calc = Calculation(5,6)

# calc.addition()
# calc.subtraction()
# calc.multiplication()
# calc.division()



