
from Library import Library
from Employee import Employee
from Student import Student
from Book import Book
from Order import Order

lib_warszawa = Library(
    "Warszawa",
    "Marszałkowska 1",
    "00-001",
    "08:00-20:00",
    "22-111-22-33")
lib_krakow = Library(
    "Kraków",
    "Floriańska 15",
    "30-001",
    "09:00-17:00",
    "12-444-55-66")


emp1 = Employee(
    "Jan",
    "Kowalski",
    "2020-01-10",
    "1985-05-12",
    "Warszawa",
    "Złota 44",
    "00-002",
    "500-100-100")
emp2 = Employee(
    "Anna",
    "Nowak",
    "2019-03-15",
    "1990-11-20",
    "Kraków",
    "Długa 5",
    "30-005",
    "600-200-200")
emp3 = Employee(
    "Piotr",
    "Wiśniewski",
    "2021-06-01",
    "1995-02-28",
    "Warszawa",
    "Wilcza 10",
    "00-003",
    "700-300-300")


stud1 = Student("Michał", "Zieliński",)
stud2 = Student("Katarzyna", "Wójcik", )
stud3 = Student("Tomasz", "Mazur",)


book1 = Book(lib_warszawa, "2022", "J.K.", "Rowling", 300)
book2 = Book(lib_warszawa, "1954", "J.R.R.", "Tolkien", 450)
book3 = Book(lib_krakow, "1949", "George", "Orwell", 200)
book4 = Book(lib_krakow, "2001", "Yann", "Martel", 320)
book5 = Book(lib_warszawa, "1925", "F. Scott", "Fitzgerald", 180)


order1 = Order(emp1, stud1, [book1, book2], "2023-10-27")

order2 = Order(emp2, stud2, [book3], "2023-10-28")



print(order1)
print()
print(order2)
