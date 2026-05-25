def max_transaction(ceny):
    max_zysk = 0

    for i in range(len(ceny)):
        for j in range(i + 1, len(ceny)):
            zysk = ceny[j] - ceny[i]
            if zysk > max_zysk:
                max_zysk = zysk

    return max_zysk


print(max_transaction([224, 236, 247, 258, 259, 225]))