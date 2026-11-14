"""  
Author: Juan David Bernal Maldonado
Date (DD/MM/YYYY): 11/11/2026
"""

from sys import stdin

def solve(A):
    N = len(A)
    tab = [0 for _ in range(N + 1)]
    for n in range(N - 1, -1, -1):
        if A[n] + n <= N:
            tab[n] = max(tab[n + 1], A[n] + tab[A[n] + n])
        else:
            tab[n] = tab[n + 1]
    return tab[0]

def main(): 
    line = stdin.readline() 
    while line != "": 
        stripped = line.strip() 
        if stripped != "": 
            n = int(stripped) 
            people = list(map(int, stdin.readline().split())) 
            print(solve(people)) 
        line = stdin.readline()
main()