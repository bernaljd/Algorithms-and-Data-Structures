""" 
Author: Juan David Bernal Maldonado
Date(DD/MM/YYYY): 07/10/2026
"""

from sys import stdin 

def minmax(l, arr):
    ans = -1
    for ant in range(len(arr)):
        tmp = min(l - arr[ant], arr[ant])
        ans = max(tmp, ans)
    return ans

def maxmax(l, arr):
    ans = -1
    for ant in range(len(arr)):
        tmp = max(l - arr[ant], arr[ant])
        ans = max(tmp, ans)
    return ans

def main():
    cases = int(stdin.readline().strip())
    for _ in range(cases):
        l, n = map(int, stdin.readline().strip().split())
        ants = list()
        while len(ants) < n:
            ants.extend(map(int, stdin.readline().strip().split()))

        print(minmax(l, ants), maxmax(l, ants))
    
main()