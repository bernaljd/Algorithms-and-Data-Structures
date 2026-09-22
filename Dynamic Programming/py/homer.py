""" 
Author: Juan David Bernal Maldonado
Date: 21/09/2026
"""

from sys import stdin

def homer(m, n, t):
    tab = [-1] * (t + 1)
    tab[0] = 0
    for i in range(1, t + 1):
        if i >= m and tab[i - m] != -1:
            tab[i] = max(tab[i], tab[i - m] + 1)
        if i >= n and tab[i - n] != -1:
            tab[i] = max(tab[i], tab[i - n] + 1)
    bestEat = 0
    maxTime = 0
    for i in range(t + 1):  
        if tab[i] != -1:
            maxTime = i
            bestEat = tab[i]
    leftOver = t - maxTime
    return (bestEat, leftOver)

def main():
    line = stdin.readline().strip()
    while(line != ''):
        m, n, t = map(int, line.split())
        ans = homer(m, n, t)
        if ans[1] == 0:
            print(ans[0])
        else:
            print(ans[0], ans[1])
        line = stdin.readline().strip()

main()