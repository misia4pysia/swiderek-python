def matrix(macierz):
    for indeks in range(len(macierz)):
        wiersz = macierz[indeks]

        if indeks % 2 == 0:
            for liczba in wiersz:
                print(liczba)
        else:
            for liczba in reversed(wiersz):
                print(liczba)


macierz = [[1, 2, 3,4],
[5, 6, 7, 8],
[0, 6, 2, 8],
[2, 3, 0, 2]]

matrix(macierz)