def transpozycja(tablica, wymiar):
    for i in range(wymiar):
        for j in range(i + 1, wymiar):
            temp = tablica[i][j]
            tablica[i][j] = tablica[j][i]
            tablica[j][i] = temp