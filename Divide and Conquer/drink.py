"""  
Author: Juan David Bernal Maldonado
Date (DD/MM/YYYY): 20/11/2026
"""

from sys import stdin

def solve(l, r, m, A):
    ans = None
    mid = (l + r) // 2
    if l >= r:
        ans = l
    elif A[mid] <= m:
        ans = solve(mid + 1, r, m, A)
    else:
        ans = solve(l, mid, m, A)
    return ans

def main():
    n = stdin.readline()
    while n != '':
        n = int(n)
        shops = list(map(int, stdin.readline().split()))
        q = int(stdin.readline())
        coins = [int(stdin.readline()) for _ in range(q)]

        for i in range(q):
            print(solve(0, n, coins[i], shops))

        n = stdin.readline()

main()