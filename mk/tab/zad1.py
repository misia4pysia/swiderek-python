def srednia_olimpijska():
    oceny = [9.5, 8.0, 9.0, 7.5, 9.5, 10.0, 8.5, 9.0]

    najmniejsza = min(oceny)
    najwieksza = max(oceny)

    oceny.remove(najmniejsza)
    oceny.remove(najwieksza)

    srednia = sum(oceny) / len(oceny)

    print(round(srednia, 2))


srednia_olimpijska()
  