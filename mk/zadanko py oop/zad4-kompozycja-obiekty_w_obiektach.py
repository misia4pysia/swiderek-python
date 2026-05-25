class Ksiazka:
    def __init__(self, tytul, autor):
        self.tytul = tytul
        self.autor = autor


class Biblioteka:
    def __init__(self):
        self.katalog_ksiazek = []

    def dodaj_do_katalogu(self, ksiazka):
        self.katalog_ksiazek.append(ksiazka)

    def wyswietl_katalog(self):
        for ksiazka in self.katalog_ksiazek:
            print(f"{ksiazka.tytul} - {ksiazka.autor}")


ksiazka1 = Ksiazka("Venom II. W otchłani chaosu", "Aleksandra Kondruciak")
ksiazka2 = Ksiazka("Flaw (less)", "Marta Łabęcka")
ksiazka3 = Ksiazka("Dwór Cierni I Róż", "Sarah J. Maas")
ksiazka4 = Ksiazka("Clone seria Studentas", "Aleksandra Negrońska")
ksiazka5 = Ksiazka("Puck Me Up", "Ludka Szydlewska")
ksiazka6 = Ksiazka("Start a Fire seria Hell", "Katarzyna Barlińska P.S. Heryteria")


biblioteka = Biblioteka()

biblioteka.dodaj_do_katalogu(ksiazka1)
biblioteka.dodaj_do_katalogu(ksiazka2)
biblioteka.dodaj_do_katalogu(ksiazka3)
biblioteka.dodaj_do_katalogu(ksiazka4)
biblioteka.dodaj_do_katalogu(ksiazka5)
biblioteka.dodaj_do_katalogu(ksiazka6)

biblioteka.wyswietl_katalog()

# Zadanie 4: Kompozycja – obiekty w obiektach
# Cel dydaktyczny: Współpraca pomiędzy wieloma różnymi klasami (przechowywanie obiektów jednej klasy w liście innej klasy).
# Treść zadania:
# 1. Skopiuj klasę Ksiazka z Zadania 1 z poprzedniej lekcji.
# 2. Stwórz nową klasę Biblioteka , która w __init__ posiada tylko jeden atrybut: pustą listę katalog_ksiazek .
# 3. W klasie Biblioteka dodaj metodę dodaj_do_katalogu(ksiazka) , która przyjmuje obiekt klasy Ksiazka i dodaje go do listy.
# 4. Dodaj metodę wyswietl_katalog() , która przejdzie pętlą for po liście książek i wypisze ich tytuły oraz autorów.
# 5. Stwórz dwa obiekty Ksiazka , stwórz obiekt Biblioteka , dodaj książki do biblioteki i wyświetl katalog.
