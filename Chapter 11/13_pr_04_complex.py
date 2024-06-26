class Complex:
    def __init__(self, r,i):
        self.real = r
        self.imaginary = i
    
    def __add__(self,c ):
        return Complex (self.real + c.real, self.imaginary + c.imaginary)
    
    def __mul__(self,c ):
        return Complex (self.real*c.real - self.imaginary*c.imaginary, self.real*c.imaginary + self.imaginary*c.real)
    
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

c1 = Complex (1,4)
c2 = Complex (8,5)
sum = c1 + c2
print (sum)
multi = c1*c2
print (multi)
