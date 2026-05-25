import random


def analizuj_macierz():
    macierz = [[random.randint(-500, 500) for _ in range(100)] for _ in range(100)]

    min_wartosc = macierz[0][0]
    max_wartosc = macierz[0][0]
    min_pozycja = (0, 0)
    max_pozycja = (0, 0)

    licznik = 0

    for i in range(100):
        for j in range(100):
            wartosc = macierz[i][j]

            if wartosc < min_wartosc:
                min_wartosc = wartosc
                min_pozycja = (i, j)

            if wartosc > max_wartosc:
                max_wartosc = wartosc
                max_pozycja = (i, j)

            if wartosc > 0 and wartosc % 2 == 0 and wartosc % 7 == 0:
                licznik += 1

    print("Min:", min_wartosc, "pozycja:", min_pozycja)
    print("Max:", max_wartosc, "pozycja:", max_pozycja)
    print("Liczb spełniających warunki:", licznik)


analizuj_macierz()
