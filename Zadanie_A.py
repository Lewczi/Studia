def wypisz_imiona(imiona):
    """
    Funkcja przyjmuje listę imion i wypisuje każde z nich.
    """
    for imie in imiona:
        print(f"Imie: {imie}")

# --- TEST ---
if __name__ == "__main__":
    moja_lista = ["Ania", "Tomek", "Kasia", "Piotr", "Zosia"]
    print("--- Wynik zadania A ---")
    wypisz_imiona(moja_lista)