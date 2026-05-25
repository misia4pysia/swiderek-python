def sprawdz_palindrom():
    slowo = input("Podaj słowo: ")
    lista_znakow = list(slowo)

    czy_palindrom = True

    for i in range(len(lista_znakow) // 2):
        if lista_znakow[i] != lista_znakow[len(lista_znakow) - 1 - i]:
            czy_palindrom = False
            break

    if czy_palindrom:
        print("To palindrom")
    else:
        print("To nie palindrom")


sprawdz_palindrom()
