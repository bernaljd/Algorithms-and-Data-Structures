""" 
Author: Juan David Bernal Maldonado
Date (DD/MM/YYYY): 11/11/2026 
"""

def fibo(n):
    tab = [0 for _ in range(n + 1)]
    tab[1] = 1
    for i in range(2, n + 1):
        tab[i] = tab[i - 2] + tab[i - 1]
    return tab