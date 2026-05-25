class Zwierze:
    def __init__(self, imie):
        self.imie = imie

    def daj_glos(self):
        print("Nieznany dźwięk")


class Pies(Zwierze):
    def __init__(self, imie, rasa):
        super().__init__(imie)
        self.rasa = rasa

    def daj_glos(self):
        print(f"Hau! Hau! Jestem {self.imie} i moja rasa to {self.rasa}")


pies1 = Pies("Jackie", "Border Collie")

pies1.daj_glos()

 # Zadanie 1: Dziedziczenie – rodzina zwierząt
# Cel dydaktyczny: Zrozumienie, jak jedna klasa może dziedziczyć cechy od innej (wykorzystanie super() ).
# Treść zadania:
# 1. Stwórz klasę bazową Zwierze , która w __init__ przyjmuje atrybut imie . Dodaj do niej metodę daj_glos() , która wypisze "Nieznany dźwięk".
# 2. Stwórz klasę Pies , która dziedziczy po klasie Zwierze .
# 3. W klasie Pies stwórz własny konstruktor __init__ , który przyjmuje imie oraz rasa . Użyj funkcji super() , aby przekazać imie do klasy bazowej.
# 4. Nadpisz (zdefiniuj ponownie) metodę daj_glos() w klasie Pies , aby wypisywała: "Hau! Hau! Jestem [imię] i moja rasa to [rasa]".
# 5. Przetestuj działanie, tworząc obiekt klasy Pies i wywołując metodę daj_glos() .
