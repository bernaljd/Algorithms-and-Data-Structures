def kp_opt1(V, W, X):
    N = len(V)
    tab = [[0 for _ in range(X + 1)] for _ in range(2)]
    n, x, prev, curr = 1, 0, 0, 1
    while n != N + 1:
        if x == X + 1: 
            n, x, prev, curr = n + 1, 0, 1 - prev, 1 - curr # Hace complemento, alternamente se usa prev = curr, curr = prev
        else:
            if W[n - 1] > x:
                tab[curr][x] = tab[prev][x]
            else:
                tab[curr][x] = max(tab[prev][X],
                                   tab[prev[x - W[n - 1]] + V[n - 1]])       
        x = x + 1
    return tab[prev][X]                        