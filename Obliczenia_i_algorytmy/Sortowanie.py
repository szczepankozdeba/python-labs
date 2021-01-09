#!/usr/bin/python3
from random import randrange


def sort(tab):
    for j in range(0, len(tab)):
        t_max = tab[j]
        max_j = j
        for k in range(j, len(tab)):
            if t_max < tab[k]:
                t_max = tab[k]
                max_j = k
        tab[max_j] = tab[j]
        tab[j] = t_max
    return tab


tab_r = []

for i in range(1,50):
    tab_r.append(randrange(100))
print(tab_r)
print(sort(tab_r))
print(tab_r.sort())
