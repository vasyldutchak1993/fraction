from math import gcd


class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")

        if denominator < 0:
            numerator *= -1
            denominator *= -1

        common = gcd(numerator, denominator)
        self.numerator = numerator // common
        self.denominator = denominator // common

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __rsub__(self, other):
        return Fraction(other, 1) - self

    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return Fraction(self.numerator * other.numerator,
                        self.denominator * other.denominator)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return Fraction(self.numerator * other.denominator,
                        self.denominator * other.numerator)

    def __rtruediv__(self, other):
        return Fraction(other, 1) / self

    def __eq__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)

    def __abs__(self):
        return Fraction(abs(self.numerator), self.denominator)

    def __float__(self):
        return self.numerator / self.denominator
