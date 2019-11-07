import math

from CsvReader import CsvReader

def addition(a, b):
    c = a + b
    return c


def subtraction(a, b):
    a = int(a)
    b = int(b)
    c = b - a
    return c


def division(a, b):
    a = int(a)
    b = int(b)
    c = b / a
    return c

def multiplication(a, b):
    a = int(a)
    b = int(b)
    c = b * a
    return c

def square_root(a):
    import math
    a = int(a)
    sqrt = math.sqrt(a)
    return a

def square(a):
    a = int(a)
    b = a**2
    return b

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def squares(self, a):
        self.result = square(a)
        return self.result

    def root(self, a):
        self.result = square_root(a)
        return self.result