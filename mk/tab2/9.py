def czy_symetryczna(tablica, n):
    for i in range(n):
        for j in range(i + 1, n):
            if tablica[i][j] != tablica[j][i]:
                return False
    return True