def szyfr_cezara(tekst):
    # ($k = (\text{długość} \% 25) + 1$
    k = (len(tekst) % 25) + 1
    e = ""
    
    for znak in tekst:
        # $E(c) = \text{chr}((A(c) - 65 + k) \% 26 + 65)$
        e += chr((ord(znak) - 65 + k) % 26 + 65)
    
    return e



def szyfr_przestawieniowy(tekst):
    while len(tekst) % 5 != 0:
        tekst += "X"
    
    klucz = [2, 0, 4, 1, 3]
    wynik = ""
    
    for i in range(0, len(tekst), 5):
        blok = tekst[i:i+5]
        nowy_blok = ""
        
        for indeks in klucz:
            nowy_blok += blok[indeks]
        
        wynik += nowy_blok
    
    return wynik



plik = open("wiadomosc.txt", "r")
tekst = plik.read().strip()
plik.close()

po_cezarze = szyfr_cezara(tekst)
wynik_koncowy = szyfr_przestawieniowy(po_cezarze)

print("Tekst po szyfrowaniu:", wynik_koncowy)