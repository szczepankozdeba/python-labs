#!/usr/bin/python3
from random import randrange
import numpy as np


m1 = []
for ii in range(8):
    m1.append([])
    for jj in range(8):
        m1[ii].append(randrange(2))

det = np.linalg.det(m1)

print(m1)
print(det)