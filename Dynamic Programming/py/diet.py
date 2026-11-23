"""  
Author: Juan David Bernal Maldonado
Date (DD/MM/YYYY): 22/11/2026
"""

from sys import stdin

E = None
mem = None

def solve(i, C, A, N):
    if (i, C) in mem:
        ans = mem[(i, C)]    
    else:
        if C <= 0:
            ans = E - C
        elif i == N:
            ans = float('inf')
        else:
            ans = min(solve(i + 1, C - A[i], A, N), solve(i + 1, C, A, N))
        mem[(i, C)] = ans
    return ans

def main():
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        global E, mem
        E = n
        mem = {}
        p = int(stdin.readline())
        courses = list(map(int, stdin.readline().split()))
        ans = solve(0, n, courses, p)
        print(ans) if ans != float('inf') else print("NO SOLUTION")
main()