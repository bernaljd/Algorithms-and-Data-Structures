""" 
Author: Juan David Bernal Maldonado
Date (DD/MM/YYYY): 11/11/2026 
"""

def fact(x):
    tab = [0 for _ in range(x + 1)]
    tab[0] = 1
    for i in range(1, x + 1):
        tab[i] = tab[i - 1] * i
    return tab[x]