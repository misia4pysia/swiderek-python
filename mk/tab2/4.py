def mnozenie_macierzy(A, B, C, n, m, k):
    for i in range(n):
        for j in range(k):
            C[i][j] = 0
            for x in range(m):
                C[i][j] += A[i][x] * B[x][j]