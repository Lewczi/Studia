class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (f"[Biblioteka] {self.city}, ul. {self.street} {self.zip_code} "
                f"(Czynne: {self.open_hours}, Tel: {self.phone})")


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (f"[Pracownik] {self.first_name} {self.last_name}, "
                f"Zatrudniony: {self.hire_date}, Tel: {self.phone}")


class Student:
    """
    Klasa Student dodana, aby umożliwić stworzenie kompletnego obiektu Order.
    """
    def __init__(self, first_name, last_name, index_number):
        self.first_name = first_name
        self.last_name = last_name
        self.index_number = index_number

    def __str__(self):
        return f"[Student] {self.first_name} {self.last_name} (Indeks: {self.index_number})"


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library  # To jest obiekt klasy Library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (f"   - '{self.author_name} {self.author_surname}', wyd. {self.publication_date}, "
                f"{self.number_of_pages} str.\n     Lokalizacja: {self.library}")


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee  # Obiekt Employee
        self.student = student    # Obiekt Student
        self.books = books        # Lista obiektów Book
        self.order_date = order_date

    def __str__(self):
        # Tworzymy napis opisujący wszystkie książki w zamówieniu
        books_description = "\n".join([str(book) for book in self.books])
        
        return (f"================ ZAMÓWIENIE ================\n"
                f"Data: {self.order_date}\n"
                f"Obsługa: {self.employee}\n"
                f"Wypożyczający: {self.student}\n"
                f"Lista książek:\n{books_description}\n"
                f"============================================")


# --- TWORZENIE INSTANCJI (OBIEKTÓW) ---

# 1. Stworzyć 2 biblioteki
lib_warszawa = Library("Warszawa", "Marszałkowska 1", "00-001", "08:00-20:00", "22-111-22-33")
lib_krakow = Library("Kraków", "Floriańska 15", "30-001", "09:00-17:00", "12-444-55-66")

# 2. Stworzyć 3 pracowników
emp1 = Employee("Jan", "Kowalski", "2020-01-10", "1985-05-12", "Warszawa", "Złota 44", "00-002", "500-100-100")
emp2 = Employee("Anna", "Nowak", "2019-03-15", "1990-11-20", "Kraków", "Długa 5", "30-005", "600-200-200")
emp3 = Employee("Piotr", "Wiśniewski", "2021-06-01", "1995-02-28", "Warszawa", "Wilcza 10", "00-003", "700-300-300")

# 3. Stworzyć 3 studentów
stud1 = Student("Michał", "Zieliński", "123456")
stud2 = Student("Katarzyna", "Wójcik", "654321")
stud3 = Student("Tomasz", "Mazur", "987654")

# 4. Stworzyć 5 książek
# Przypisujemy obiekty bibliotek do książek
book1 = Book(lib_warszawa, "2022", "J.K.", "Rowling", 300)
book2 = Book(lib_warszawa, "1954", "J.R.R.", "Tolkien", 450)
book3 = Book(lib_krakow, "1949", "George", "Orwell", 200)
book4 = Book(lib_krakow, "2001", "Yann", "Martel", 320)
book5 = Book(lib_warszawa, "1925", "F. Scott", "Fitzgerald", 180)

# 5. Stworzyć 2 zamówienia
# Zamówienie 1: Jan Kowalski obsługuje Michała Zielińskiego (2 książki)
order1 = Order(emp1, stud1, [book1, book2], "2023-10-27")

# Zamówienie 2: Anna Nowak obsługuje Katarzynę Wójcik (1 książka)
order2 = Order(emp2, stud2, [book3], "2023-10-28")

# --- WYŚWIETLANIE ---

print(order1)
print()
print(order2)