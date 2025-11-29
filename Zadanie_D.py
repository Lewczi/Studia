def wypisz_co_drugi(liczby):
   
    co_drugi = liczby[::2]
    
    print("Co drugi element:")
    for element in co_drugi:
        print(element)

dane = list(range(10, 20))
print(f"Dane wejściowe: {dane}")

wypisz_co_drugi(dane)