def przesuniecie_cykliczne():
    lista = [1, 2, 3, 4, 5]
    k = 2

    for i in range(k):
        element = lista.pop()
        lista.insert(0, element)

    print(lista)


przesuniecie_cykliczne()
