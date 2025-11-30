class Property:
    def __init__(self, area, rooms, price, address):
        """
        Konstruktor klasy bazowej Property.
        """
        self.area = area       # Powierzchnia
        self.rooms = int(rooms) # Liczba pokoi (wymuszamy int)
        self.price = price     # Cena
        self.address = address # Adres

class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        """
        Konstruktor klasy House.
        Używa super() do wywołania konstruktora klasy rodzica.
        """
        super().__init__(area, rooms, price, address)
        self.plot = int(plot)  # Rozmiar działki (int)

    def __str__(self):
        return (f"Dom: Adres: {self.address}, Powierzchnia: {self.area} m2, "
                f"Pokoje: {self.rooms}, Cena: {self.price}, Działka: {self.plot} m2")

class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        """
        Konstruktor klasy Flat.
        """
        super().__init__(area, rooms, price, address)
        self.floor = floor     # Piętro

    def __str__(self):
        return (f"Mieszkanie: Adres: {self.address}, Powierzchnia: {self.area} m2, "
                f"Pokoje: {self.rooms}, Cena: {self.price}, Piętro: {self.floor}")

# --- Tworzenie obiektów i wyświetlanie ---

# 1. Stworzenie obiektu klasy House
# Argumenty: area, rooms, price, address, plot
dom = House(150, 5, 850000, "ul. Leśna 10, Warszawa", 600)

# 2. Stworzenie obiektu klasy Flat
# Argumenty: area, rooms, price, address, floor
mieszkanie = Flat(65, 3, 550000, "al. Jerozolimskie 100/5, Warszawa", 4)

# 3. Wyświetlenie obiektów (automatycznie wywoła metodę __str__)
print(dom)
print(mieszkanie)