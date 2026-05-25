def dfs(tablica, i, j, wiersze, kolumny):
    if i < 0 or j < 0 or i >= wiersze or j >= kolumny:
        return
    if tablica[i][j] == 0:
        return

    tablica[i][j] = 0

    dfs(tablica, i + 1, j, wiersze, kolumny)
    dfs(tablica, i - 1, j, wiersze, kolumny)
    dfs(tablica, i, j + 1, wiersze, kolumny)
    dfs(tablica, i, j - 1, wiersze, kolumny)


def liczba_wysp(tablica):
    wiersze = len(tablica)
    kolumny = len(tablica[0])
    licznik = 0

    for i in range(wiersze):
        for j in range(kolumny):
            if tablica[i][j] == 1:
                licznik += 1
                dfs(tablica, i, j, wiersze, kolumny)

    return licznik