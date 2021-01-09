#!/usr/bin/python3
from random import randrange


def matrix_sum(a, b):
    c = [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]
    for k in range(0, 7):
        for i in range(0, 7):
            for j in range(0, 7):
                c[i][j] += a[i][k]*b[k][j]
    return c


m1 = []
m2 = []
for ii in range(8):
    m1.append([])
    m2.append([])
    for jj in range(8):
        m1[ii].append(randrange(2))
        m2[ii].append(randrange(2))

print(m1)
print(m2)
print(matrix_sum(m1, m2))
