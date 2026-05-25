def maks_w_wierszach(tablica, wynik):
    for i in range(len(tablica)):
        maks = tablica[i][0]
        for j in range(len(tablica[i])):
            if tablica[i][j] > maks:
                maks = tablica[i][j]
        wynik.append(maks)