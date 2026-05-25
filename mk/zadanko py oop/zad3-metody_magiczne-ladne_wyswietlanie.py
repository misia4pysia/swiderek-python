class Uczen:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.oceny = []

    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)

    def policz_srednia(self):
        if len(self.oceny) == 0:
            return 0

        suma = sum(self.oceny)
        srednia = suma / len(self.oceny)

        return round(srednia, 2)

    def __str__(self):
        return f"Uczeń: {self.imie} {self.nazwisko}, Średnia ocen: {self.policz_srednia()}"


uczen1 = Uczen("Magda", "Kaczorowska")

uczen1.dodaj_ocene(6)
uczen1.dodaj_ocene(5)
uczen1.dodaj_ocene(4)

print(uczen1)

# Zadanie 3: Metody magiczne – ładne wyświetlanie ( __str__ )
# Cel dydaktyczny: Nadpisywanie metod wbudowanych Pythona, aby obiekty "współpracowały" z funkcją print() .
# Treść zadania:
# 1. Stwórz klasę Uczen . Konstruktor ma przyjmować imie i nazwisko oraz tworzyć pustą listę oceny .
# 2. Dodaj metodę dodaj_ocene(ocena) .
# 3. Dodaj metodę policz_srednia() , która zwraca średnią ocen (pamiętaj o zabezpieczeniu przed dzieleniem przez 0, jeśli lista jest pusta).
# 4. Zdefiniuj w klasie metodę __str__(self) . Ma ona zwracać ładnie sformatowany tekst (string), np.: "Uczeń: [Imię] [Nazwisko], Średnia ocen: [Średnia]".
# 5. Stwórz ucznia, dodaj mu trzy oceny i wypisz obiekt zwykłym print(uczen) .
