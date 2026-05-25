import random


def sortowanie_babelkowe(tablica):
    porownania = 0
    zamiany = 0
    n = len(tablica)

    for i in range(n):
        for j in range(0, n - i - 1):
            porownania += 1
            if tablica[j] > tablica[j + 1]:
                tablica[j], tablica[j + 1] = tablica[j + 1], tablica[j]
                zamiany += 1

    return porownania, zamiany


def sortowanie_przez_wstawianie(tablica):
    porownania = 0
    zamiany = 0

    for i in range(1, len(tablica)):
        klucz = tablica[i]
        j = i - 1

        while j >= 0:
            porownania += 1
            if tablica[j] > klucz:
                tablica[j + 1] = tablica[j]
                zamiany += 1
                j -= 1
            else:
                break

        tablica[j + 1] = klucz

    return porownania, zamiany


def eksperyment():
    losowa = [random.randint(1, 10000) for _ in range(5000)]
    rosnaca = sorted(losowa)
    malejaca = sorted(losowa, reverse=True)

    przypadki = {
        "Losowa": losowa,
        "Rosnaca": rosnaca,
        "Malejaca": malejaca
    }

    print("Przypadek | Algorytm | Porownania | Zamiany")

    for nazwa, tab in przypadki.items():
        p1, z1 = sortowanie_babelkowe(tab.copy())
        p2, z2 = sortowanie_przez_wstawianie(tab.copy())

        print(nazwa, "| Babelkowe |", p1, "|", z1)
        print(nazwa, "| Wstawianie |", p2, "|", z2)


eksperyment()
