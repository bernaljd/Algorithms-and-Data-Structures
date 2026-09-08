"""
Author: Juan David Bernal Maldonado
Date (DD/MM/YY): 02/09/26
"""

from sys import stdin 

def divideConquer(arr, cumSum, l, r):
    if l > r:
        ans = ""
    else:
        bestNode = None
        bestDiff = float('inf')
        bestJ = -1

        i = l
        while i <= r:
            j = i
            while j + 1 <= r and arr[j + 1] == arr[i]:   # avanzar hasta el fin del bloque
                j += 1

            left = cumSum[j] - cumSum[l]        # todo antes del bloque (excluye el bloque entero, incluida la raíz)
            if j < r:
                right = cumSum[r + 1] - cumSum[j + 1]
            else:
                right = 0

            diff = abs(right - left)

            if diff <= bestDiff:
                bestNode = arr[j]
                bestDiff = diff
                bestJ = j

            i = j + 1   # saltar al siguiente bloque distinto

        izq = divideConquer(arr, cumSum, l, bestJ - 1)
        der = divideConquer(arr, cumSum, bestJ + 1, r)

        raiz = str(bestNode)
        if izq and der:
            ans = raiz + "(" + izq + "," + der + ")"
        elif izq:
            ans = raiz + "(" + izq + ")"
        elif der:
            ans = raiz + "(" + der + ")"
        else:
            ans = raiz

    return ans

def cumulativeSum(arr):
    ans = [0]
    for i in range(0, len(arr)):
        ans.append(arr[i] + ans[i])
    return ans

def main():
    T = int(stdin.readline().strip())
    for i in range(T):
        n = int(stdin.readline().strip())
        nodes = list(map(int, stdin.readline().strip().split()))
        nodes.sort()
        cumSum = cumulativeSum(nodes)

        ans = divideConquer(nodes, cumSum, 0, n - 1)
        print("Case #%d: " % (i + 1), end="")
        print(ans)

main()