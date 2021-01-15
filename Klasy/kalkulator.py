
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

    def multiply(self, a):
        return ComplexNumber(self.re * a.re - self.im * a.im, self.re * a.im + self.im * a.re)

    def substract(self, a):
        return ComplexNumber(self.re - a.re, self.im - a.im)

    def sumary(self, a):
        return ComplexNumber(self.re + a.re, self.im + a.im)

while 1:

    print("podaj liczby")
    a = input("podaj  re pierwszej liczby: ")
    b = input("podaj im pierwszej liczby: ")
    a1 = input("podaj  re drugiej liczby: ")
    b1 = input("podaj im drugiej liczby: ")

    C1 = ComplexNumber(float(a), float(b))
    C2 = ComplexNumber(float(a1), float(b1))


    print("Wybierz operacje:\n1.dodawanie\n2.odejmowanie\n3.sprzężenie\n4.moduł\n5.mnożenie\n")
    operation = input(" operacja:  ")

    if operation == '1':
        s = C1.sumary(C2)
        print("suma: ", s.get_re(), " + ", s.get_im(), "i", "\n")

    elif operation == '2':
        s = C1.substract(C2)
        print("różnica: ", s.get_re(), " + ", s.get_im(), "i", "\n")

    elif operation == '3':
         s = C1.conj()
         print("sprzężenie pierwszej liczby: ", s.get_re(), " + ", s.get_im(), "i", "\n")

    elif operation == '4':
        print("moduł pierwszej liczby: ", C1.abs(), "i", "\n")

    elif operation == '5':
        s = C1.multiply(C2)
        print("iloczyn liczb: ", s.get_re(), " + ", s.get_im(), "i", "\n")

    else:
        print("nie ma takiego działania, wybierz jeszcze raz\n")