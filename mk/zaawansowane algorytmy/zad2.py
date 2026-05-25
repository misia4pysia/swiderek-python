from datetime import datetime, timedelta


def analizuj_logi():
    czasy = {}

    with open("logi_serwera.csv", "r", encoding="utf-8") as plik:
        for linia in plik:
            try:
                dane = linia.strip().split(";")

                id_u = dane[0]
                data_log = datetime.strptime(dane[1], "%d-%m-%Y %H:%M:%S")
                data_wylog = datetime.strptime(dane[2], "%d-%m-%Y %H:%M:%S")

                roznica = data_wylog - data_log

                if id_u not in czasy:
                    czasy[id_u] = timedelta()

                czasy[id_u] += roznica

            except (ValueError, IndexError):
                continue  

    for id_u, czas in czasy.items():
        sekundy = int(czas.total_seconds())
        h = sekundy // 3600
        m = (sekundy % 3600) // 60
        s = sekundy % 60
        print(f"{id_u}: {h}:{m}:{s}")


analizuj_logi()
