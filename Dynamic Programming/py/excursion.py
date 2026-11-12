"""  
Author: Juan David Bernal Maldonado
Date (DD/MM/YYYY): 11/11/2026
"""

from sys import stdin

def solve(n, A, tab):
    N = len(A)
    if n == N:
        tab[n] = 0
    elif A[n] + n <= N:
        tab[n] = max(solve(n + 1, A, tab), A[n] + solve(A[n] + n, A, tab))
    elif A[n] + n > N:
        tab[n] = solve(n + 1, A, tab)
    return tab[n]

def main():
    line = int(stdin.readline())
    i = 0
    while line != "":
        if i > 0:
            n = int(stdin.readline())
        else:
            n = int(line)
        people = list(map(int, stdin.readline().split()))
        print(solve(0, people, [0 for _ in range(n + 1)]))
        i += 1
        line = stdin.readline()

main()