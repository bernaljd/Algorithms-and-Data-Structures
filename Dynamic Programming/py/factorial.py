""" 
Author: Juan David Bernal Maldonado
Date (DD/MM/YYYY): 11/11/2026 
"""

from sys import stdin 

def fact(x, tab):
    tab.append(1)
    for i in range(1, x + 1):
        tab.append((tab[i - 1]) * i)
    return tab[x]

