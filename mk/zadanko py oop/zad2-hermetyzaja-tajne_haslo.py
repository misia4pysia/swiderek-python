class Sejf:
    def __init__(self):
        self.__zawartosc = "100 sztabek złota"
        self.__pin = "1234"

    def otworz(self, podany_pin):
        if podany_pin == self.__pin:
            print(self.__zawartosc)
        else:
            print("Dostęp odmówiony!")


moj_sejf = Sejf()

moj_sejf.otworz("1234")
moj_sejf.otworz("4321")


# Zadanie 2: Hermetyzacja – tajne hasło
# Cel dydaktyczny: Ukrywanie danych wewnątrz obiektu za pomocą atrybutów prywatnych i tworzenie tzw. getterów/setterów.
# Treść zadania:
# 1. Stwórz klasę Sejf . W konstruktorze ustaw atrybut prywatny __zawartosc (np. przypisz mu wartość "100 sztabek złota") oraz atrybut prywatny __pin (np.
# "1234").
# 2. Zauważ, że wpisanie print(moj_sejf.__zawartosc) wyrzuci błąd.
# 3. Napisz publiczną metodę otworz(podany_pin) . Metoda ta ma sprawdzić, czy podany_pin zgadza się z __pin .
# 4. Jeśli PIN jest poprawny, metoda ma zwrócić (lub wypisać) __zawartosc . Jeśli błędny – wypisać "Dostęp odmówiony!".