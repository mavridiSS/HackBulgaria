class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __float__(self):
        return float(self.numerator) / float(self.denominator)

    def __str__(self):
        return "{} / {}".format(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        a = float(self.numerator) / float(self.denominator)
        b = float(other.numerator) / float(other.denominator)
        return float(Fraction(a*b, 1))

    def __sub__(self, other):
        a = float(self.numerator) / float(self.denominator)
        b = float(other.numerator) / float(other.denominator)
        return float(Fraction(a-b, 1))

    def __mul__(self, other):
        a = self.numerator * other.numerator
        b = self.denominator * other.denominator
        return Fraction(a, b)

    def __eq__(self, other):
        a = float(self.numerator) / float(self.denominator)
        b = float(other.numerator) / float(other.denominator)
        return a == b

a = Fraction(1, 2)
b = Fraction(2, 1)

print(a * b)
# a - b
# a * b
