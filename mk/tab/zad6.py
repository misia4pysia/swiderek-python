def suma_przekatnej():
    macierz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    suma = 0

    for i in range(len(macierz)):
        suma += macierz[i][i]

    print(suma)


suma_przekatnej()
