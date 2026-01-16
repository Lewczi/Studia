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