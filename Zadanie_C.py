def wypisz_parzyste(liczby):

    print("Liczby parzyste:")
    for liczba in liczby:
        if liczba % 2 == 0:
            print(liczba)


dane = list(range(10))
print(f"Dane wejściowe: {dane}")

wypisz_parzyste(dane)
