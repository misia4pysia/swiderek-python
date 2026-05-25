def suma_przekatnych(tablica, wymiar):
    suma = 0

    for i in range(wymiar):
        suma += tablica[i][i] 
        suma += tablica[i][wymiar - 1 - i]  

    if wymiar % 2 == 1:
        srodek = wymiar // 2
        suma -= tablica[srodek][srodek]

    return suma