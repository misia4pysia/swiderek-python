def remove_value(tablica, wartosc):
    tab = []

    for liczba in tablica:
        if liczba != wartosc:
            tab.append(liczba)

    return len(tab)


print(remove_value([1, 2, 3, 4, 5, 6, 7, 5],5))
print(remove_value([10,10,10,10,10], 10))
print(remove_value([10,10,10,10,10], 20))
print(remove_value([], 1))