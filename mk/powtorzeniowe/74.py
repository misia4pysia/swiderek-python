def max_zysk(ceny):
    if len(ceny) == 0:
        return 0

    min_cena = ceny[0]
    max_zysk = 0

    for cena in ceny:
        if cena < min_cena:
            min_cena = cena

        zysk = cena - min_cena
        if zysk > max_zysk:
            max_zysk = zysk

    return max_zysk


print(max_zysk([8, 10, 7, 5, 7, 15]))
print(max_zysk([1, 2, 8, 1]))
print(max_zysk([]))    