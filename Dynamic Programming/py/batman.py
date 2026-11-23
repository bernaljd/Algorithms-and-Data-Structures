"""  
Author: Juan David Bernal Maldonado
Date (DD/MM/YYYY): 22/11/2026
"""

from sys import stdin

mem = {}

def solve(i, j, E, p, v):
    if (i, j, E) in mem:
        ans = mem[(i, j, E)]
    else:
        V = len(v)
        P = len(p)
        if E < 0:
            ans = False
        elif j == V:
            ans = True
        elif i == P:
            ans = False
        elif p[i][1] >= v[j][0] and p[i][0] in v[j][1]:
            ans = solve(i + 1, j + 1, E - p[i][2], p, v) or solve(i + 1, j, E, p, v)
        else:
            ans = solve(i + 1, j, E, p, v)
        mem[(i, j, E)] = ans
    return ans


def main():
    P, V, E = map(int, stdin.readline().split())
    while (P, V, E) != (0, 0, 0):
        global mem
        mem = {}
        powers = []
        for _ in range(P):
            s, a, c = stdin.readline().split()
            powers.append((s, int(a), int(c)))
        villains = []
        for _ in range(V):
            n, d, dp = stdin.readline().split()
            villains.append((int(d), list(dp.split(','))))
        print("Yes") if solve(0, 0, E, powers, villains) else print("No")

        P, V, E = map(int, stdin.readline().split())

main()