def zerowanie(tablica):
    wiersze = len(tablica)
    kolumny = len(tablica[0])

    wiersze_do_zera = []
    kolumny_do_zera = []

    for i in range(wiersze):
        for j in range(kolumny):
            if tablica[i][j] == 0:
                wiersze_do_zera.append(i)
                kolumny_do_zera.append(j)

    for i in wiersze_do_zera:
        for j in range(kolumny):
            tablica[i][j] = 0

    for j in kolumny_do_zera:
        for i in range(wiersze):
            tablica[i][j] = 0