
def pomnoz_petla(liczby):
    wynik = []
    for liczba in liczby:
        wynik.append(liczba * 2)
    return wynik


def pomnoz_lista_skladana(liczby):
    return [liczba * 2 for liczba in liczby]


dane = [1, 2, 3, 4, 5]

wynik_1 = pomnoz_petla(dane)
print(f"Wersja pętla for: {wynik_1}")

wynik_2 = pomnoz_lista_skladana(dane)
print(f"Wersja lista składana: {wynik_2}")