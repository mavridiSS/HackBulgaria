class Fraction:

    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator can't be zero.")
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        if self.numerator == 0:
            return "{}".format(self.numerator)
        else:
            return "{} / {}".format(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        a = self.numerator * other.denominator
        b = other.numerator * self.denominator
        c = self.denominator * other.denominator
        return Fraction(a + b, c)

    def __sub__(self, other):
        a = self.numerator * other.denominator
        b = other.numerator * self.denominator
        c = self.denominator * other.denominator
        return Fraction(a - b, c)

    def __mul__(self, other):
        a = self.numerator * other.numerator
        b = self.denominator * other.denominator
        return Fraction(a, b)

    def __eq__(self, other):
        a = self.numerator / self.denominator
        b = other.numerator / other.denominator
        return a == b
