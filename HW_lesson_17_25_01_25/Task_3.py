# Task _3
# Basic arithmetic logic for fractions


import math


class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator
        self._reduce()

    def _reduce(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def __add__(self, other):
        new_numerator = (self.numerator * other.denominator +
                         other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = (self.numerator * other.denominator -
                         other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other):
        return (self.numerator == other.numerator and
                self.denominator == other.denominator)

    def __lt__(self, other):
        return (self.numerator * other.denominator < other.numerator
                * self.denominator)

    def __le__(self, other):
        return (self.numerator * other.denominator <= other.numerator
                * self.denominator)

    def __gt__(self, other):
        return (self.numerator * other.denominator > other.numerator
                * self.denominator)

    def __ge__(self, other):
        return (self.numerator * other.denominator >= other.numerator
                * self.denominator)

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    z = x + y
    print(z)  # 3/4
    print(x - y)  # 1/4
    print(x * y)  # 1/8
    print(x / y)  # 2/1
    print(x == Fraction(1, 2))  # True
    print(x < y)  # False
    print(x > y)  # True
