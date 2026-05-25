def obrot_90(tablica, wynik, wymiar):
    for i in range(wymiar):
        for j in range(wymiar):
            wynik[j][wymiar - 1 - i] = tablica[i][j]