def drugi_najwiekszy_element():
    liczby = [10, 20, 4, 45, 99, 4, 20]

    najwieksza = None
    druga_najwieksza = None

    for liczba in liczby:
        if najwieksza is None or liczba > najwieksza:
            druga_najwieksza = najwieksza
            najwieksza = liczba
        elif liczba != najwieksza and (druga_najwieksza is None or liczba > druga_najwieksza):
            druga_najwieksza = liczba

    print(druga_najwieksza)


drugi_najwiekszy_element()
