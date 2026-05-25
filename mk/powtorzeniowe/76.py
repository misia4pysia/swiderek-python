def find_range(tablica, find_value):
    poczatek = -1
    koniec = 0

    for indeks in range(len(tablica)):
        if tablica[indeks] == find_value:
            if poczatek == -1:
                poczatek = indeks
            koniec = indeks

    if poczatek == -1:
        return [-1, 0]

    return [poczatek, koniec]


print(find_range([5, 7, 7, 8, 8, 8], 8))
print(find_range([1, 3, 6, 9, 13, 14], 4))