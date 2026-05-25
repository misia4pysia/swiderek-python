def spirala(tablica, n):
    liczba = 1
    gora = 0
    dol = n - 1
    lewo = 0
    prawo = n - 1

    while gora <= dol and lewo <= prawo:

        for i in range(lewo, prawo + 1):
            tablica[gora][i] = liczba
            liczba += 1
        gora += 1

        for i in range(gora, dol + 1):
            tablica[i][prawo] = liczba
            liczba += 1
        prawo -= 1

        for i in range(prawo, lewo - 1, -1):
            tablica[dol][i] = liczba
            liczba += 1
        dol -= 1

        for i in range(dol, gora - 1, -1):
            tablica[i][lewo] = liczba
            liczba += 1
        lewo += 1