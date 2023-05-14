class ComplexNumber:
    def __init__(self, real_part, imag_part):
        self.real = real_part
        self.imag = imag_part

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real}+{self.imag}i"
        else:
            return f"{self.real}{self.imag}i"


c1 = ComplexNumber(1, 2)
c2 = ComplexNumber(3, -4)

print(c1 + c2)
print(c1 * c2)
