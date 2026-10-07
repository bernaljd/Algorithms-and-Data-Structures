"""  
Author: Juan David Bernal
Date: 22/09/2026
"""

from sys import stdin

def isSafe():
    

def backtrack(board, col, N, sol):
    if col == N:
        sol.append(["".join(row) for row in board])
    else:
        for row in range(N):
            if isSafe():
                pass


def main():
    N = int(stdin.readline().strip())
    board = [['.' for _ in range(N)] for _ in range(N)]
    ans = []

    ans = backtrack(board, 0, N, ans)
    
main()