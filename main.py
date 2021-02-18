

class Rational:

    def __init__(self, numerator, denominator):

        self.denominator = denominator
        if self.denominator == 0:
            if numerator != 0:
                raise ZeroDivisionError
        self.numerator = numerator
        if self.numerator == 0:
            self.denominator = 0

    # create str method
    def ...(...):
        ...

    def __repr__(self):
        return "Rational(" + str(self.numerator) + "," + str(self.denominator) + ")"

    # create float overloading
    def ...(...):
        ....

    def __reduce__(self):
        a = self.numerator
        b = self.denominator
        while self.numerator != 0 and self.denominator != 0:
            if self.numerator > self.denominator:
                self.numerator = self.numerator % self.denominator
            else:
               self.denominator = self.denominator % self.numerator

        return Rational(a // self.numerator, b // self.numerator)

    # create add method
    def ...(..., other):


        if other == 0:
            ...

        if isinstance(other, Rational):

            if other == Rational(0, 0):
                ...

            ...

        else:
            return NotImplemented



ch = Rational(1, 5)
ch2 = Rational(1, 5)
ch3 = Rational(0, 5)
try:
    ch4 = Rational(5, 0)
except ZeroDivisionError:
    print("ERROR")

#print(ch.__str__(), end=' = ')
#print(ch.__repr__())
#print(ch2.__str__(), end=' = ')
#print(ch2.__repr__())
#print()
#print(Rational(2, 2))
#print(Rational(2, 20).__reduce__())
#r = ch + ch2
#print(r)


