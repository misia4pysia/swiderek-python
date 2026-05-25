def czy_anagram(slowo1, slowo2):
    s1 = slowo1.replace(" ", "").lower()
    s2 = slowo2.replace(" ", "").lower()

    if len(s1) != len(s2):
        return False

    licznik = {}

    for znak in s1:
        if znak not in licznik:
            licznik[znak] = 0
        licznik[znak] += 1

    for znak in s2:
        if znak not in licznik:
            return False
        licznik[znak] -= 1

    for wartosc in licznik.values():
        if wartosc != 0:
            return False

    return True


with open("slowa.txt", "r") as plik:
    for linia in plik:
        s1, s2 = linia.strip().split()
        print(s1, s2, "->", czy_anagram(s1, s2))
