#!/usr/bin/python3


def scalar_product(a, b):
    temp = 0
    for i in range(1, 4):
        temp += a[i] * b[i]
    return temp


a = [1, 2, 12, 4]
b = [2, 4, 2, 8]
print(scalar_product(a, b))
