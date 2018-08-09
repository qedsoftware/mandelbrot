import math

class Complex(object):
    def __init__(self, real, imag):
        self.a = real
        self.b = imag
    def __str__(self):
        return f"{self.a}, {self.b}"
    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)
    def __mul__(self, other):
        return(self.a*other.a-self.b*other.b, self.a*other.b+self.b*other.a)