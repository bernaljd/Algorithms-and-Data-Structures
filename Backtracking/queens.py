
from sys import stdin

def check(s, r):
    ans = True
    c = len(s)
    for i in range(c):
        if s[i] == r: ans = False
        if (s[i] - r) == abs(i - c): ans = False
    return ans

def solve(s, sols):
    if len(s) == 8:
        sols.append(s.copy())
    else:
        for i in range(1,9):
            if check():
                s.append(i)
                solve(s, sols)
                s.pop()

def main():
    sols = list()
    solve([], sols)
    line = stdin.readline().strip()
    case = 1
    while(line != ''):
        l = list(map(int, line.split()))
        ans = 8
        for S in sols:
            movs = 0
            for c in range(8):
                if l[c] != S[c]: movs += 1
            ans = min(ans, movs)
        print('Case {}: {}'.format(case, ans))
        line = stdin.readline().strip()
        case += 1
main()