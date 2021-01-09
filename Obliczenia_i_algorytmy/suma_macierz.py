#!/usr/bin/python3
from random import randrange


def matrix_sum(m1, m2):
    for i in range(0, len(m1)):
        for j in range(0, len(m2)):
            m1[i][j] += m2[i][j]
    return m1


m1 = []
m2 = []
for i in range(128):
    m1.append([])
    m2.append([])
    for j in range(128):
        m1[i].append(randrange(200))
        m2[i].append(randrange(200))

print(m1)
print(m2)
print(matrix_sum(m1, m2))
