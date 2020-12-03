#(a+bi)+(c+di) = (a+c) + (b+d)i
#(a+bi)(c+di) = (ac-db) + (ad + bc)i

class Complex:

    def __init__(self, r, i):
        self.real = r
        self.imaginary = i

    def __add__(c1, c2):
        real = c1.real + c2.real
        imaginary = c1.imaginary + c2.imaginary
        return Complex(real, imaginary)

    def __mul__(self, c):
        mulReal = self.real*c.real - self.imaginary*c.imaginary
        mulImaginary = self.real*c.imaginary + self.imaginary*c.real
        return Complex(mulReal, mulImaginary)

    def __str__(self):
        if self.imaginary < 0:
            return f"{self.real} - {-self.imaginary}i"
        else:
            return f"{self.real} + {self.imaginary}i"





c1 = Complex(3, 2)
c2 = Complex(1, 7)
print(c1 + c2)
print(c1*c2)

c3 = Complex(3, 2)
c4 = Complex(4, -5)
print(c3 + c4)
print(c3 * c4)
