def punkt_siodlowy(tablica):
    wiersze = len(tablica)
    kolumny = len(tablica[0])

    for i in range(wiersze):
        for j in range(kolumny):
            element = tablica[i][j]

            
            najmniejszy = True
            for x in range(kolumny):
                if tablica[i][x] < element:
                    najmniejszy = False

            
            najwiekszy = True
            for y in range(wiersze):
                if tablica[y][j] > element:
                    najwiekszy = False

            if najmniejszy and najwiekszy:
                print("punkt siodlowy:", i, j)
                return

    print("brak punktu siodlowego")