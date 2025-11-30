def czy_parzysta(liczba:int) -> bool:
    return liczba % 2 == 0

sprawdz = czy_parzysta(10)
if sprawdz:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")

