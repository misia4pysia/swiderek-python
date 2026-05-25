from datetime import datetime


def agreguj_dane():
    dane = {}

    with open("temperatury_miasta.csv", "r") as plik:
        for linia in plik:
            try:
                miasto, data_str, temp_str = linia.strip().split(",")

                data = datetime.strptime(data_str, "%Y-%m-%d")

                if data <= datetime(2020, 1, 1):
                    continue

                temp_str = temp_str.replace(",", ".")
                temperatura = float(temp_str)

                if miasto not in dane:
                    dane[miasto] = [0, 0]

                dane[miasto][0] += temperatura
                dane[miasto][1] += 1

            except (ValueError, IndexError):
                continue

    srednie = []

    for miasto, (suma, licznik) in dane.items():
        if licznik > 0:
            srednia = suma / licznik
            srednie.append((miasto, srednia))

    srednie.sort(key=lambda x: x[1], reverse=True)

    with open("raport.txt", "w") as plik:
        for miasto, sr in srednie:
            plik.write(f"{miasto};{sr:.2f}\n")


agreguj_dane()
