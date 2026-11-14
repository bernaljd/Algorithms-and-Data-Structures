""" 
Autor: Juan David Bernal Maldonado
Fecha (DD/MM/YYYY): 14/11/2026 
"""

def lcs(A, B):
    N = len(A)
    M = len(B)
    # las columnas son rango interno, las filas son el rango externo
    tab = [[None for _ in range(M + 1)] for _ in range(N + 1)]
    for n in range(N, -1, -1):
        for m in range(M, -1, -1):
            if n == N or m == M:
                tab[n][m] = 0
            elif A[n] == B[m]:
                tab[n][m] = 1 + tab[n + 1][m + 1]
            else:
                tab[n][m] = max(tab[n + 1][m], tab[n][m + 1])
    return tab[0][0]

A = ['A', 'L', 'G', 'O', 'R', 'I', 'T', 'M', 'O']
B = ['L', 'O', 'G', 'A', 'R', 'I', 'T', 'M', 'O']
print(lcs(A, B))