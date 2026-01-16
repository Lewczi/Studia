from Student import Student

student_passed = Student("Anna Kowalska", [60, 70, 80])


student_failed = Student("Jan Nowak", [30, 40, 45])

# Wyświetlenie wyników
print(f"Student: {student_passed.name}, Zdał: {student_passed.is_passed()}")
print(f"Student: {student_failed.name}, Zdał: {student_failed.is_passed()}")