def remove_duplicates(tablica):
    tab = []

    for liczba in tablica:
        if liczba not in tab:
            tab.append(liczba)

    return len(tab)


print(remove_duplicates([0,0,1,1,2,2,3,3,4,4,4]))
print(remove_duplicates([1, 2, 2, 3, 4, 4])) 