class Produkt:
    def __init__(self, nazwa, cena, ilosc_w_magazynie):

        if cena < 0 or ilosc_w_magazynie < 0:
            raise ValueError("Cena i ilość nie mogą być ujemne!")

        self.nazwa = nazwa
        self.cena = cena
        self.ilosc_w_magazynie = ilosc_w_magazynie

    def kup(self, ilosc):

        if ilosc <= 0:
            print("ilosc musi byc wieksza od zera")
            return

        if ilosc <= self.ilosc_w_magazynie:

            koszt = ilosc * self.cena

            self.ilosc_w_magazynie -= ilosc

            print(f"zakupiono produkt: {self.nazwa}")
            print(f"calkowity koszt: {koszt} zł")

        else:
            print("Niewystarczająca ilość w magazynie!")


# Błąd
produkt1 = Produkt("Telefon", -1000, 5)

# Poprawny produkt
produkt2 = Produkt("Laptop", 3000, 10)

produkt2.kup(2)
produkt2.kup(20)


# Zadanie 6: Sklep i walidacja danych (Zgłaszanie błędów/Wyjątki)
# Cel dydaktyczny: Sprawdzanie poprawności danych wewnątrz metod klasy i rzucanie wyjątków (błędów) lub wyświetlanie ostrzeżeń.
# Treść zadania:
# 1. Stwórz klasę Produkt z atrybutami nazwa , cena oraz ilosc_w_magazynie .
# 2. Zabezpiecz konstruktor: jeśli przy tworzeniu obiektu podana cena lub ilosc_w_magazynie jest mniejsza od 0, użyj instrukcji raise ValueError("Cena i
# ilość nie mogą być ujemne!") .
# 3. Dodaj metodę kup(ilosc) . Metoda ma sprawdzić czy chcemy kupić poprawną ilość (większą od zera) i czy w ogóle mamy tyle sztuk w magazynie.
# 4. Jeśli tak, zmniejsz ilosc_w_magazynie i wypisz całkowity koszt (ilość * cena). Jeśli nie, wypisz komunikat "Niewystarczająca ilość w magazynie!".
# 5. Przetestuj program. Spróbuj stworzyć produkt z ujemną ceną (aby zobaczyć błąd), a następnie stwórz poprawny produkt i przetestuj udane oraz nieudane
# zakupy