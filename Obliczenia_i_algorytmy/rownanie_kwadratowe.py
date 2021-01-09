#!/usr/bin/python3
import numpy as np


def roots(a,b,c):
    delta = (b**2)-(4*a*c)
    if(delta<0):
        return "delta mniejsza od 0 "
    delta = np.sqrt(delta)
    x1 = (-b+delta)/(2*a)
    x2 = (-b-delta)/(2*a)
    return x1, x2


a = float(input("podaj a:"))
b = float(input("podaj b:"))
c = float(input("podaj c:"))
print("pierwiastki równania kwadatowego:")
print(roots(a, b, c))
