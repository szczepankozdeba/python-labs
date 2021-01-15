import math

class ComplexNumber:
    def __init__(self, re, im):
        self.re = re
        self.im  = im
    def get_re(self):
        return self.re

    def get_im(self):
        return self.im

    def abs(self):
        return math.sqrt(self.re * self.re + self.im * self.im)

    def conj(self):
        self.im = -self.im

x = ComplexNumber(2, 3)



