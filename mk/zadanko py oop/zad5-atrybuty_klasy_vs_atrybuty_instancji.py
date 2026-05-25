class Pracownik:
    liczba_pracownikow = 0

    def __init__(self, imie, stanowisko):
        self.imie = imie
        self.stanowisko = stanowisko

        Pracownik.liczba_pracownikow += 1


pracownik1 = Pracownik("Magda", "Kierownik")
pracownik2 = Pracownik("Kuba", "Konserwator")
pracownik3 = Pracownik("Krzysiek", "Programista")

print("liczba pracownikow:", Pracownik.liczba_pracownikow)


# Zadanie 5: Atrybuty klasy vs Atrybuty instancji
# Cel dydaktyczny: Zrozumienie zmiennych współdzielonych przez wszystkie obiekty danej klasy.
# Treść zadania:
# 1. Stwórz klasę Pracownik .
# 2. Bezpośrednio w ciele klasy (przed __init__ ) zdefiniuj atrybut klasy liczba_pracownikow = 0 .
# 3. W konstruktorze __init__ przypisz pracownikowi imie oraz stanowisko . Dodatkowo, przy każdym wywołaniu konstruktora, zwiększ wartość
# Pracownik.liczba_pracownikow o 1.
# 4. Stwórz trzech różnych pracowników.
# 5. Na koniec wypisz Pracownik.liczba_pracownikow , aby udowodnić, że program sam policzył stworzone obiekty i wynik wynosi 3.
