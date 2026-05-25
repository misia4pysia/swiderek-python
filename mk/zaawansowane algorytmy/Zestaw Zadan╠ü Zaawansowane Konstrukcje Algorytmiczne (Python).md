
**Czas pracy:** 90 minut

**Cel:** Symulacja warunków egzaminacyjnych, optymalizacja kodu i obsługa błędów.

---

#### Zadanie 1: Kryptografia hybrydowa (Cezar + Przestawienia)

**Opis:** Napisz program symulujący dwuetapowe szyfrowanie tekstu pobranego z pliku `wiadomosc.txt` (plik zawiera tylko wielkie litery alfabetu łacińskiego).

**Etapy algorytmu:**

1. **Szyfr Cezara:** Przesuń każdy znak o klucz $k$.
    
    - $k$ oblicz jako resztę z dzielenia długości tekstu przez 25, powiększoną o 1 ($k = (\text{długość} \% 25) + 1$).
        
    - Zastosuj wzór: $E(c) = \text{chr}((A(c) - 65 + k) \% 26 + 65)$.
        
2. **Szyfr Przestawieniowy:** Podziel zaszyfrowany w kroku 1 tekst na bloki 5-znakowe.
    
    - Jeżeli ostatni blok jest krótszy, uzupełnij go znakami 'X'.
        
    - W każdym bloku dokonaj permutacji znaków według klucza indeksów: `[2, 0, 4, 1, 3]` (tzn. znak z indeksu 2 idzie na początek, z 0 na drugie miejsce itd.).
        

**Wymagania:** Użyj funkcji `ord()`, `chr()`, pętli oraz wycinków (slicing).

---

#### Zadanie 2: Analiza logów z obsługą błędów (Inżynieria Czasu)

**Opis:** Posiadasz plik `logi_serwera.csv` z danymi: `Id_Uzytkownika;Data_Logowania;Data_Wylogowania`. Format daty to `DD-MM-YYYY HH:MM:SS`. Plik jest uszkodzony (zawiera błędne daty, np. 29-02-2023, oraz śmieciowe dane).

**Polecenie:**

Stwórz program, który obliczy łączny czas spędzony w systemie przez każdego użytkownika.

1. Wykorzystaj moduł `datetime` i metodę `strptime`.
    
2. Oblicz różnicę czasu (`timedelta`) dla każdego wpisu.
    
3. **Kluczowe:** Zastosuj blok `try...except`. Program nie może się zatrzymać po napotkaniu błędu!
    
    - Błędne wpisy (np. złe daty) mają być przechwycone (`ValueError`, `IndexError`) i zignorowane (lub cicho zalogowane), a program ma liczyć dalej.
        
4. Wypisz wynik w formacie: `ID: Łączna liczba godzin:minut:sekund`.
    

---

#### Zadanie 3: Empiryczne badanie złożoności sortowania

**Opis:** Przeprowadź eksperyment porównujący wydajność dwóch algorytmów sortowania o złożoności $O(n^2)$: **Sortowania Bąbelkowego** (Bubble Sort) oraz **Sortowania przez Wstawianie** (Insertion Sort).

**Polecenie:**

1. Zaimplementuj oba algorytmy samodzielnie (nie używaj `sort()` ani `sorted()`).
    
2. Wygeneruj trzy tablice po 5000 liczb całkowitych:
    
    - Losową.
        
    - Posortowaną rosnąco (optymistyczna).
        
    - Posortowaną malejąco (pesymistyczna).
        
3. Dodaj do algorytmów liczniki operacji dominujących (porównań i zamian).
    
4. Wyświetl tabelę porównującą liczbę operacji dla obu algorytmów w każdym z trzech przypadków.
    

---

#### Zadanie 4: Macierz losowa i poszukiwanie ekstremów

**Opis:** Wygeneruj dwuwymiarową tablicę (macierz) o wymiarach 100x100. Wypełnij ją liczbami pseudolosowymi z zakresu [-500, 500] używając _list comprehensions_.

**Polecenie:**

1. **Znajdź min/max:** Napisz algorytm, który znajdzie wartość największą i najmniejszą oraz poda ich współrzędne (wiersz, kolumna).
    
    - _Uwaga:_ Zabrania się używania wbudowanych funkcji `min()` i `max()` na listach. Musisz użyć zagnieżdżonych pętli i instrukcji warunkowych.
        
2. **Analiza:** Policz, ile w macierzy jest liczb, które spełniają **jednocześnie** trzy warunki:
    
    - Są parzyste.
        
    - Są dodatnie (>0).
        
    - Są podzielne przez 7.
        

---

#### Zadanie 5: Weryfikacja anagramów (Histogramy)

**Opis:** W pliku `slowa.txt` znajdują się pary słów. Napisz funkcję `czy_anagram(slowo1, slowo2)`, która sprawdzi, czy słowa są anagramami.

**Wymagania:**

1. **Zakaz sortowania:** Nie wolno używać `sorted(s1) == sorted(s2)`.
    
2. **Implementacja:** Musisz wykorzystać zliczanie znaków.
    
    - Zlicz wystąpienia liter w pierwszym słowie (inkrementacja).
        
    - Odejmij wystąpienia na podstawie drugiego słowa (dekrementacja).
        
    - Sprawdź, czy słownik/tablica jest pusta (same zera).
        
3. Przed sprawdzeniem znormalizuj tekst (usuń białe znaki, zamień na małe litery).
    

---

#### Zadanie 6: Praca Klasowa – Agregacja danych pogodowych

**Opis:** Przetwórz plik `temperatury_miasta.csv` (kolumny: `Miasto`, `Data`, `Temperatura`), który jest "zanieczyszczony" (puste wiersze, przecinki zamiast kropek w liczbach zmiennoprzecinkowych).

**Polecenie:**

Napisz skrypt realizujący logikę zapytania SQL `GROUP BY`:

1. Wczytaj dane z pliku. Zastosuj `try...except` do konwersji temperatury na `float` (obsłuż zamianę przecinka na kropkę).
    
2. Filtrowanie: Weź pod uwagę tylko pomiary wykonane po **2020/01/01**.
    
3. Agregacja: Zgrupuj dane po mieście i oblicz **średnią temperaturę** dla każdego miasta. Użyj słownika.
    
4. Wyjście: Zapisz do nowego pliku raport posortowany **malejąco** według średniej temperatury.